import re
import timeit


def LoadData(datafiles,LineNum):

    # Read file and put lines into list
    with open(datafiles, "r") as log:
         # Store the data into list
        file = []
        for line in log:
            file.append(line)
            
        #match the log type with our existing findings 
        for i in range(LineNum):
        	#Log type 1
            if re.search(r'\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d', file[i]):
                pass
            #Log type 2
            elif re.search(r'(\w\w:\w\w:\w\w.\w\w\w:\s%)', file[i]):
                pass
            #Log type 3
            elif re.search(r'\d\d:\s\w\w\w\s\d\d\s\w\w:\w\w:\w\w.\w\w\w:\s%', file[i]):
                pass
            #Log type 4
            elif re.search(r'\w\w:\w\w:\w\w.\w\w\w:\s\[', file[i]):
                pass
            #Log type 5
            elif re.search(r'\d\d\d\d\d\d\d\d\d\d\d\d', file[i]):
                pass
            #new type findings
            else:
                print (file[i])
                break
            return

def main():

    #Start run time
    start = timeit.default_timer()

    # Setup the lines of log events and choose log file
    line =700000

    #log files should be at the same folder
    #syslg = 'obfuscated_syslogHead1000'
    #syslg = 'logfile'
    syslg = 'Piece_1'
    LoadData(syslg,line)

    # Stop of the run time
    stop = timeit.default_timer()
    print (stop - start)


# call the main method
main();
