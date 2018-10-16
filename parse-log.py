#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:36:31 2017

@author: sibrihen
"""
import re

# The log file should be in the same folder
LOG_FILE = "logfile"

def main():
    with open(LOG_FILE) as file:
        for line in file:
            if 'From' in line:
            
                # Split the server and host parts
                originator_collector = line.split(' From ')
               
                # Parse the collector part into : timestamp, hostname
                collector = split_on_nth_occ(originator_collector[0], 3)
                collector_ts = collector[0]
                collector_host = collector[1]
                
                # Parse the originator part message into : timestamp, host, message 
                originator = split_on_nth_occ(originator_collector[1], 1, ': ')
                originator_host = originator[0]



                is_type_two = re.search(r'(\w\w:\w\w:\w\w.\w\w\w:\s%)', originator[1])
                
                # Check if we have a message of type 2
                if is_type_two:    
                    originator = split_on_nth_occ(originator[1], 1, ': %')
                else:
                    originator = split_on_nth_occ(originator[1], 2, ' ')
                
                # Get originators timestamp and message content
                originator_ts = originator[0]
                originator_msg = originator[1]
            
                print('Collector timestamp : ' + collector_ts)
                print('Collector hostname : ' + collector_host)
                print('--------------------------------------')
                print('Originator timestamp : ' + originator_ts)
                print('Originator hostname : ' + originator_host)
                print('Originator message : ' + originator_msg)
                
            else:
                # Repeat message
                # TODO
                break
    
            
# Splits the given text on the n-th occurence of the separator
# Example split_on_nth_occ('a b c', 3, separator=' ') = ['a', 'bc']
def split_on_nth_occ(text, n, separator=' '):
    groups = text.split(separator)
    return separator.join(groups[:n]), separator.join(groups[n:])
    
# Call the main method
main()
