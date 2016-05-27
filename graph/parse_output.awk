BEGIN { 
    maxidx=1; 
} 

{ 
    app=$1;
    url=$2;
    conc=$3;
    min=$4; 
    avg=$5; 
    max=$6; 

    #print $1 "\t" $3 "\t" $4; 

    if (url in urls) {
        idx=urls[url];
    }
    else {
        urls[url]=maxidx; 
	urls_list[maxidx] = url;
	maxidx++;
    }
  
    id = urls[url];
  
    print app "\t" id "\t" conc "\t" min "\t" avg "\t" max; 

}
END {
    for(i=1; i<length(urls_list); i++)
        print i "\t" urls_list[i];
}
