#! /bin/bash

awk -F, -fparse_output.awk ../output.csv > output_parsed.txt

