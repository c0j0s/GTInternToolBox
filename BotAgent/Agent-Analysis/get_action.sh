#!/bin/bash
for filename in intentOnly-English/*.json; do
    {
    	cat "$filename" | {
    		jp -c .responses[].action 2> /dev/null; 
    	}
    } || {
    	echo "No value"
    }
done
