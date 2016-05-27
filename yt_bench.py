import commands
import re

concurrencies = [1, 5, 10]
timelimit = 120
server_ip = '10.10.12.165'
apps = { 'aspx': '/webservicesnet/index.aspx' ,
         'asp' : '/webservices/index.asp' }

with open('queries.txt') as f:
	queries = f.read().splitlines()

out = open('output.csv', 'w') 
out.truncate()

# exteract
def extractText(text, regStr):
	p = re.compile(regStr)
	txt = p.search(text).group(1)
	return txt
		 
# returns time in milliseconds
def parseTime(timeStr):
	# remove whitespace
	timeStr = timeStr.strip()
	# timeStr is a string like "0.0306 s"
	p = re.compile(r'(.*) s')
	sec = p.search(timeStr).group(1)
	return float(sec)*1000

def runbench():
	for app,path in apps.items():
		for conc in concurrencies:
			idx = 0
			for query in queries:
				idx = idx + 1
				
				# merge locals and globals into a single container - for string interpolation below
				context = dict(locals())
				context.update(globals())
				
				# construct the url
				url = "http://{server_ip}{path}?{query}".format(**context)
				
				cmd = "boom -c {conc} -n 100 '{url}'".format(**locals())
				print app, conc, idx

				ret = commands.getoutput(cmd)

				#print ret
				avgStr = extractText(ret, r'Average(.*)')
				avg_ = parseTime(avgStr)

				minStr = extractText(ret, r'Fastest(.*)')
				min_ = parseTime(minStr)

				maxStr = extractText(ret, r'Slowest(.*)')
				max_ = parseTime(maxStr)

				# app,query,concurrency,min_,avg_,max_
				out.write("{app},{query},{conc},{min_},{avg_},{max_}\n".format(**locals()))


# entry point
runbench()
