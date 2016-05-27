#! /bin/bash

gnuplot -e "inputfilename='conc_1.dat'; outputfilename='conc_1.png'; titlename='Legacy vs .net - YT XML service | concurrency: 1'" foo.gplot
gnuplot -e "inputfilename='conc_5.dat'; outputfilename='conc_5.png'; titlename='Legacy vs .net - YT XML service | concurrency: 5'" foo.gplot
gnuplot -e "inputfilename='conc_10.dat'; outputfilename='conc_10.png'; titlename='Legacy vs .net - YT XML service | concurrency: 10'" foo.gplot
