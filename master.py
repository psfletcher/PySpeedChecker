#Master File
#Plan is to run this python script once a mintue by CRON
#So it needs to close each time, with no loops or passing params
#if i can work out how to keep the script always running that would change.
#So the plan
#Check time / mintues
#add if statements to do something in that minute as needed
#This will include ping once a mintue
#speed test to 6 different fixed site at 0,10,20,30,40,50 etc


#!/usr/bin/python
import time
import os
import os.path
import speedtest
import pyping
import datetime

#Static Constants
Home_Path = "/home/psfletcher/"
SpeedTest_CSVHeader = 'Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload\n'
Ping_CSVHeader = 'StartTime,EndTime,Destination,min_rtt,avg_rtt,max_rtt,packet_loss,dest_IP,Status\n'
Test_Type = "SpeedTester"
Ping_Test_Type = "Ping"
Test_File_Type = ".csv"
Test_Location = "0000"

#Dynamic Constants
OP_Year = time.strftime("%Y")
OP_Month = time.strftime("%m")
OP_Day = time.strftime("%d")




def WriteToFileIncHeader(fileinfo,csvinfo,writeinfo):
    if os.path.isfile(fileinfo) and os.access(fileinfo, os.R_OK):
        print "File exists and is readable"
        file = open(fileinfo, "a")
        file.write(writeinfo+"\n")
        file.close()
    else:
        print "Either file is missing or is not readable"
        file = open(fileinfo, "w")
        file.write(csvinfo)
        file.write(writeinfo + "\n")
        file.close()


def func_speedtester(Server):
    servers = [Server]

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    #print s.results.csv()
    return s.results.csv()


def func_ping(Ping_server):
    ping_hostname = Ping_server
    timeoutput_start = '%sZ' % datetime.datetime.utcnow().isoformat()
    p = pyping.ping(ping_hostname)
    timeoutput_finish = '%sZ' % datetime.datetime.utcnow().isoformat()
    if p.ret_code == 0:
        ping_status = "Online"
    else:
        ping_status = "Offline"
    output_csv = timeoutput_start + ',' + timeoutput_finish + ',' + p.destination + ',' + p.min_rtt + ',' + p.avg_rtt + ',' + p.max_rtt + ',' + str(p.packet_lost) + ',' + p.destination_ip + ',' + ping_status
    return output_csv

###########################################################
# Ping Tests ran every mintue / every run
###########################################################

Test_Location = 'google-public-dns-a.google.com'
ping_info = func_ping(Test_Location)
file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Ping_Test_Type + '-' + str(Test_Location) + Test_File_Type)
print ping_info
print file_Output
WriteToFileIncHeader(file_Output, Ping_CSVHeader, ping_info)

Test_Location = 'scan.co.uk'
ping_info = func_ping(Test_Location)
file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Ping_Test_Type + '-' + str(Test_Location) + Test_File_Type)
print ping_info
print file_Output
WriteToFileIncHeader(file_Output, Ping_CSVHeader, ping_info)

Test_Location = '137.221.201.171'
ping_info = func_ping(Test_Location)
file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Ping_Test_Type + '-' + str(Test_Location) + Test_File_Type)
print ping_info
print file_Output
WriteToFileIncHeader(file_Output, Ping_CSVHeader, ping_info)

###########################################################
# Speed Tests every 10 mintues - Hourly Schedule Below
###########################################################

localtime = time.localtime(time.time())
print localtime[4] #this is mintues in the tuple
if (localtime[4] == 00):
    print "0"
    Test_Location = 1153
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)
elif (localtime[4] == 10):
    print "10"
    Test_Location = 4379
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)
elif (localtime[4] == 20):
    print "20"
    Test_Location = 8713
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)
elif (localtime[4] == 30):
    print "30"
    Test_Location = 1234
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)
elif (localtime[4] == 40):
    print "40"
    Test_Location = 1685
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)
elif (localtime[4] == 59):
    print "50"
    Test_Location = 6523
    data = func_speedtester(Test_Location)
    print data
    file_Output = (Home_Path + OP_Year + '-' + OP_Month + '-' + OP_Day + '-' + Test_Type + str(Test_Location) + Test_File_Type)
    print file_Output
    WriteToFileIncHeader(file_Output, SpeedTest_CSVHeader, data)