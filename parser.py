import numpy as np
import pandas as pd
import re
import timeit
import matplotlib.pyplot as plt
import random

def ExtractLineIntoMessage(LineOfLog):

    p1  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\slast\smessage\srepeated\s\d+\stimes?$)'
    p2  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\*\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s.+$)'
    p3  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s\[.+\]:\s%\S+:\s.+)'
    p4  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:$)'
    p5  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s[\s\S]+)'
    p6  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:$)'
    p7  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*:\s%\S+:\s.+)'
    p8  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s.+)'
    p9  = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s.+)'
    p10 = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d+:\s.+)'
    p11 = r"(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d\s\[\S+\]\s.+)"
    p12 = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s.+$)'
    p13 = r'(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+\s?:\s.+)'
    
    Original_Server=""
    Timestamp=""
    Date=""
    Special_Tag=""
    Module=""
    Additonal_Date_Information=""
    Additonal_Module_Information=""
    Main_Content=""
    
    repeat_time=0
           
    if None != re.search(p1,LineOfLog):
        repeat_time=re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\slast\smessage\srepeated\s(\d+)\stimes?$",LineOfLog)[0]
        Type = "Type_1"        
        
    elif None != re.search(p2,LineOfLog): 
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d+:\s\*\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s.+$",LineOfLog)[0]
        Timestamp = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d+):\s\*\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s.+$",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\*(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d):\s%\S+:\s.+$",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\*\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%(\S+):\s.+$",LineOfLog)[0]
        Main_Content= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\*\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s(.+)$",LineOfLog)[0]
        Type = "Type_2" 
                
    elif None != re.search(p3,LineOfLog):
        Original_Server = re.findall(r"From\s(.+?):",LineOfLog)[0]
        Date = re.findall(r"From\s.+?:\s(.+?):\s\[",LineOfLog)[0]
        Special_Tag= re.findall(r"From\s.+?:\s.+?:\s(\[.+?\]):\s%",LineOfLog)[0]
        Module= re.findall(r"From\s.+?:\s.+?:\s\[.+?\]:\s%(.+?):\s",LineOfLog)[0]
        Main_Content= re.findall(r"From\s.+?:\s.+?:\s\[.+?\]:\s%.+?:\s(.+?)$",LineOfLog)[0]
        Type = "Type_3" 
            
    elif None != re.search(p4,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:$",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d):\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:$",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:$",LineOfLog)[0]
        Additonal_Date_Information= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d):\s%\S+:$",LineOfLog)[0]
        Additonal_Module_Information= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%(\S+):$",LineOfLog)[0]
        Type = "Type_4" 
    
    elif None != re.search(p5,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s[\s\S]+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d):\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s[\s\S]+",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s[\s\S]+",LineOfLog)[0]
        Additonal_Date_Information= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d):\s%\S+:\s[\s\S]+",LineOfLog)[0]
        Additonal_Module_Information= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%(\S+):\s[\s\S]+",LineOfLog)[0]
        Main_Content= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s([\s\S]+)$",LineOfLog)[0]
        Type = "Type_5" 
    
    elif None != re.search(p6,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:$",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d):\s%\S+:$",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%(\S+):$",LineOfLog)[0]
        Type = "Type_6" 
    
    elif None != re.search(p7,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*:\s%\S+:\s.+",LineOfLog)[0]
        Timestamp = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*:\s%\S+:\s.+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*):\s%\S+:\s.+",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*:\s%(\S+):\s.+",LineOfLog)[0]
        Main_Content= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d.*:\s%\S+:\s(.+)$",LineOfLog)[0]
        Type = "Type_7" 
            
    elif None != re.search(p8,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s.+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d):\s%\S+:\s.+",LineOfLog)[0]
        Module = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%(\S+):\s.+",LineOfLog)[0]
        Main_Content = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d\d\d:\s%\S+:\s(.+)$",LineOfLog)[0]
        Type = "Type_8" 
    
    elif None != re.search(p9,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s.+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d)\s.+",LineOfLog)[0]
        Main_Content = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s(.+)$",LineOfLog)[0]
        Type = "Type_9" 
            
    elif None != re.search(p10,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d+:\s.+",LineOfLog)[0]
        Timestamp = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d+:\s.+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d+):\s.+",LineOfLog)[0]
        Main_Content = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d\.\d+:\s(.+)$",LineOfLog)[0]
        Type = "Type_10" 
    
    elif None != re.search(p11,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d\s\[\S+\]\s.+",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d)\s\[\S+\]\s.+",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d\s\[(\S+)\]\s.+",LineOfLog)[0]
        Main_Content = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d\d/\d\d/\d\d\d\d\s\d\d:\d\d:\d\d\s\[\S+\]\s(.+)$",LineOfLog)[0]
        Type = "Type_11" 
    
    elif None != re.search(p12,LineOfLog):
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s.+$",LineOfLog)[0]
        Timestamp = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d+):\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s.+$",LineOfLog)[0]
        Date = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s(\w\w\w\s\d\d\s\d\d:\d\d:\d\d):\s%\S+:\s.+$",LineOfLog)[0]
        Module= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%(\S+):\s.+$",LineOfLog)[0]
        Main_Content= re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+:\s\w\w\w\s\d\d\s\d\d:\d\d:\d\d:\s%\S+:\s(.+)$",LineOfLog)[0]    
        Type = "Type_12"                
            
    elif None != re.search(p13,LineOfLog):        
        Original_Server = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s(\S+):\s\d+\s?:\s.+",LineOfLog)[0]
        Timestamp = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s(\d+)\s?:\s.+",LineOfLog)[0]
        Main_Content = re.findall(r"\w\w\w\s\d\d\s\d\d:\d\d:\d\d\s\S+\sFrom\s\S+:\s\d+\s?:\s(.+)$",LineOfLog)[0]                    
        Type = "Type_13" 
            
    else:
        Type = "New Type"
       
    contentofmessage = [Original_Server, Timestamp, Date, Special_Tag, Module, Additonal_Date_Information, Additonal_Module_Information, Main_Content]
    processing_result=[contentofmessage, Type, repeat_time]
    
    return processing_result



def LoadData(datafiles,LineNum):

    Type_1=0
    Type_2=0
    Type_3=0
    Type_4=0
    Type_5=0
    Type_6=0
    Type_7=0
    Type_8=0
    Type_9=0
    Type_10=0
    Type_11=0
    Type_12=0
    Type_13=0
       
    
    # Put the the data segments into dataframe
    df = pd.DataFrame(columns=['Original Server', 'Timestamp', 'Date', 'Special Tag', 'Module', 'Additonal Date Information', 'Additonal Module Information', 'Main Content'])

    
    
    # Read file and put lines into list
    with open(datafiles, "r") as log:
         # Store the data into list
        file = []
        for line in log:
            file.append(line)
        j=0
        #match the log type with our existing findings 
        for i in range(LineNum):
        	  #Log type 1    
            key= file[i]
            
            processing_result=ExtractLineIntoMessage(key)
            
            Type_of_message= processing_result[1]
        
            
            if Type_of_message=="Type_1":
                repeated_time=int(processing_result[2])
                previous_message=df.loc[j-1]
                while repeated_time:
                    repeated_time=repeated_time-1
                    df.loc[j]=previous_message
                    j=j+1
                                    
                Type_1 += 1
                
                
            elif Type_of_message=="Type_2":                
                Type_2 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_3":
                Type_3 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_4":
                Type_4 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_5":
                Type_5 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_6":
                Type_6 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_7":
                Type_7 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_8":
                Type_8 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_9":
                Type_9 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_10":
                Type_10 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_11":
                Type_11 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_12":
                Type_12 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            elif Type_of_message=="Type_13":
                Type_13 += 1
                df.loc[j] = processing_result[0]
                j += 1
                
            else:
                print ("New Type Found!!!!!!"+" at Line "+str(i))
                print (key)
            
                  
            
            
        
        x='CSV output/new'+str(random.randint(1, 100000))+'type.csv'               
            
        df.to_csv(x, sep='\t', encoding='utf-8')
            
    
    if LineNum==Type_1+Type_2+Type_3+Type_4+Type_5+Type_6+Type_7+Type_8+Type_9+Type_10+Type_11+Type_12+Type_13:
        print ("Type 1= "+str(round(Type_1*100/LineNum,8))+"%")
        print ("Type 2= "+str(round(Type_2*100/LineNum,8))+"%")
        print ("Type 3= "+str(round(Type_3*100/LineNum,8))+"%")
        print ("Type 4= "+str(round(Type_4*100/LineNum,8))+"%")
        print ("Type 5= "+str(round(Type_5*100/LineNum,8))+"%")
        print ("Type 6= "+str(round(Type_6*100/LineNum,8))+"%")
        print ("Type 7= "+str(round(Type_7*100/LineNum,8))+"%")
        print ("Type 8= "+str(round(Type_8*100/LineNum,8))+"%")
        print ("Type 9= "+str(round(Type_9*100/LineNum,8))+"%")
        print ("Type 10= "+str(round(Type_10*100/LineNum,8))+"%")
        print ("Type 11= "+str(round(Type_11*100/LineNum,8))+"%")
        print ("Type 12= "+str(round(Type_12*100/LineNum,8))+"%")
        print ("Type 13= "+str(round(Type_13*100/LineNum,8))+"%")


        
        print ("Type 1= "+str(Type_1))
        print ("Type 2= "+str(Type_2))
        print ("Type 3= "+str(Type_3))
        print ("Type 4= "+str(Type_4))
        print ("Type 5= "+str(Type_5))
        print ("Type 6= "+str(Type_6))
        print ("Type 7= "+str(Type_7))
        print ("Type 8= "+str(Type_8))
        print ("Type 9= "+str(Type_9))
        print ("Type 10= "+str(Type_10))
        print ("Type 11= "+str(Type_11))
        print ("Type 12= "+str(Type_12))
        print ("Type 13= "+str(Type_13))
        
        print (Type_1+Type_2+Type_3+Type_4+Type_5+Type_6+Type_7+Type_8+Type_9+Type_10+Type_11+Type_12+Type_13)

    else:
        print ("Count is not Correct!!!")



            
    return





def main():        
    
    #Start run time
    start = timeit.default_timer()

    # Setup the lines of log events and choose log file
    
    #line =7130893
    #line =700000
    #line =10000
    line =130893
    
    #log files should be at the same folder
    #syslg = 'obfuscated_syslogHead1000'
    syslg = 'Piece_11_of_11'
    #syslg = 'obfuscated_syslog1311270005'
    #syslg = '13_typical_type'

    LoadData(syslg,line)

    # Stop of the run time
    stop = timeit.default_timer()
    print (stop - start)
    


# call the main method
main();