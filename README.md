# web_bench

Recently I wanted to run some benchmarks to evaluate and present the performance of a new system vs a legacy one.

This stress test is quite configurable (uses a series of urls found in a configuration file "queries.txt").
It makes use of the Boom! (https://github.com/tarekziade/boom) tool that conveniently reports a set of benchmark
values including min, avg and max response times.

Now, since I wanted to present those findings in a concise and elegant way, I used gnuplot to generate some
nice pictures.

I run my tests with 3 different concurrency levels (1,5 and 10) so I created 3 different graphs that
diplay the avergage (as a usual bar) and the min/max values as "candlesticks" (e.g. small horizontal
line segments representing min and max).

The entire project is written in python, awk and simple bash scripts.

Hope you find it useful in your benchmarking attempts !
