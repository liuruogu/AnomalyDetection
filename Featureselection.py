import numpy as np
import pandas as pd
import re
import timeit


# Get and the store the data into dataframe
class DataProcess:

    def LoadData(self,datafiles,LineNum):

        # Put the the data segments into dataframe
        df = pd.DataFrame(columns=['Ctime','Cname','Otime','Oname','Module', 'Msg'])

        # Read file and put lines into list
        with open(datafiles, "r") as log:
            file = []
            # store the current number of lines
            j = 0

            # Store the data into list
            for line in log:
                file.append(line)

            # Parse the data from syslogs
            for i in range(LineNum):
                # Split the server and host parts

                # 1st type of log msg
                if 'From' in file[i]:
                    originator_collector = file[i].split(' From ')

                    # Parse the collector part into : timestamp, hostname
                    collector = split_on_nth_occ(originator_collector[0], 3)
                    collector_ts = collector[0]
                    collector_host = collector[1]

                    # Parse the originator part message into : timestamp, host, message
                    originator = split_on_nth_occ(originator_collector[1], 1, ': ')
                    originator_host = originator[0]

                    # 2nd type of log msg
                    is_type_two = re.search(r'(\w\w:\w\w:\w\w.\w\w\w:\s%)', originator[1])
                    # Check if we have a message of type 2
                    if is_type_two:
                        originator = split_on_nth_occ(originator[1], 1, ': %')
                    else:
                        originator = split_on_nth_occ(originator[1], 2, ' ')
                                    # Get originators timestamp and message content
                    #print(originator)
                    originator_ts = originator[0]
                    msg = originator[1]

                    #extract module
                    if msg[0] == '[':
                        originator = split_on_nth_occ(msg, 1, ']')
                        originator_module = originator[0][1:]
                        originator_msg = originator[1]
                    else:
                        originator = split_on_nth_occ(msg, 1, ':')
                        originator_module = originator[0]
                        originator_msg = originator[1]
                        
                    message = [collector_ts, collector_host, originator_ts, originator_host, originator_module, originator_msg]
                    df.loc[j] = message 

                # Handle the 3rd type of log msg
                elif 'last' in file[i]:
                    repeat_msg = file[i].split(' last ')
                    originator_msg = repeat_msg[1]
                    # Get the number of "how many time the last message repeat"
                    repeat_times = [int(s) for s in originator_msg.split() if s.isdigit()][0]

                    # Insert the repeated message into csv file
                    for k in range(repeat_times):
                        df.loc[j+k] = message
                        # print(message)
                    j = j+k
                j += 1

            # Export to csv file
            df.to_csv('out.csv', sep='\t', encoding='utf-8')

        return


def main():

    #Start run time
    start = timeit.default_timer()

    # Setup the lines of log events and choose log file
    line = 1000

    FE = DataProcess()

    #log files should be at the same folder
    #sys1000 = 'obfuscated_syslogHead1000.txt'
    sys1000 = 'logfile'
    sys1g = 'sys1g'
    FE.LoadData(sys1000,line)

    # Stop of the run time
    stop = timeit.default_timer()
    print (stop - start)

# Splits the given text on the n-th occurence of the separator
# Example split_on_nth_occ('a b c', 3, separator=' ') = ['a', 'bc']
def split_on_nth_occ(text, n, separator=' '):
    groups = text.split(separator)
    #print(separator.join(groups[:n]), separator.join(groups[n:]))
    return separator.join(groups[:n]), separator.join(groups[n:])

# call the main method
main();
