#!/usr/bin/python3
import time, threading, os
from nmap import PortScanner
from tkinter import *
import MODULES.Enumeration, MODULES.write2report, MODULES.functions



nm = PortScanner()

def preScan(self):

    # ###### TEMP ASSIGNMENT #####

    # # QUICK SCAN 
    # self.quickPortScan = {'nmap': {'command_line': '/snap/nmap/2864/usr/bin/nmap -oX - -T4 -Pn 192.168.102.145', 'scaninfo': {'tcp': {'method': 'connect', 'services': '1,3-4,6-7,9,13,17,19-26,30,32-33,37,42-43,49,53,70,79-85,88-90,99-100,106,109-111,113,119,125,135,139,143-144,146,161,163,179,199,211-212,222,254-256,259,264,280,301,306,311,340,366,389,406-407,416-417,425,427,443-445,458,464-465,481,497,500,512-515,524,541,543-545,548,554-555,563,587,593,616-617,625,631,636,646,648,666-668,683,687,691,700,705,711,714,720,722,726,749,765,777,783,787,800-801,808,843,873,880,888,898,900-903,911-912,981,987,990,992-993,995,999-1002,1007,1009-1011,1021-1100,1102,1104-1108,1110-1114,1117,1119,1121-1124,1126,1130-1132,1137-1138,1141,1145,1147-1149,1151-1152,1154,1163-1166,1169,1174-1175,1183,1185-1187,1192,1198-1199,1201,1213,1216-1218,1233-1234,1236,1244,1247-1248,1259,1271-1272,1277,1287,1296,1300-1301,1309-1311,1322,1328,1334,1352,1417,1433-1434,1443,1455,1461,1494,1500-1501,1503,1521,1524,1533,1556,1580,1583,1594,1600,1641,1658,1666,1687-1688,1700,1717-1721,1723,1755,1761,1782-1783,1801,1805,1812,1839-1840,1862-1864,1875,1900,1914,1935,1947,1971-1972,1974,1984,1998-2010,2013,2020-2022,2030,2033-2035,2038,2040-2043,2045-2049,2065,2068,2099-2100,2103,2105-2107,2111,2119,2121,2126,2135,2144,2160-2161,2170,2179,2190-2191,2196,2200,2222,2251,2260,2288,2301,2323,2366,2381-2383,2393-2394,2399,2401,2492,2500,2522,2525,2557,2601-2602,2604-2605,2607-2608,2638,2701-2702,2710,2717-2718,2725,2800,2809,2811,2869,2875,2909-2910,2920,2967-2968,2998,3000-3001,3003,3005-3007,3011,3013,3017,3030-3031,3052,3071,3077,3128,3168,3211,3221,3260-3261,3268-3269,3283,3300-3301,3306,3322-3325,3333,3351,3367,3369-3372,3389-3390,3404,3476,3493,3517,3527,3546,3551,3580,3659,3689-3690,3703,3737,3766,3784,3800-3801,3809,3814,3826-3828,3851,3869,3871,3878,3880,3889,3905,3914,3918,3920,3945,3971,3986,3995,3998,4000-4006,4045,4111,4125-4126,4129,4224,4242,4279,4321,4343,4443-4446,4449,4550,4567,4662,4848,4899-4900,4998,5000-5004,5009,5030,5033,5050-5051,5054,5060-5061,5080,5087,5100-5102,5120,5190,5200,5214,5221-5222,5225-5226,5269,5280,5298,5357,5405,5414,5431-5432,5440,5500,5510,5544,5550,5555,5560,5566,5631,5633,5666,5678-5679,5718,5730,5800-5802,5810-5811,5815,5822,5825,5850,5859,5862,5877,5900-5904,5906-5907,5910-5911,5915,5922,5925,5950,5952,5959-5963,5987-5989,5998-6007,6009,6025,6059,6100-6101,6106,6112,6123,6129,6156,6346,6389,6502,6510,6543,6547,6565-6567,6580,6646,6666-6669,6689,6692,6699,6779,6788-6789,6792,6839,6881,6901,6969,7000-7002,7004,7007,7019,7025,7070,7100,7103,7106,7200-7201,7402,7435,7443,7496,7512,7625,7627,7676,7741,7777-7778,7800,7911,7920-7921,7937-7938,7999-8002,8007-8011,8021-8022,8031,8042,8045,8080-8090,8093,8099-8100,8180-8181,8192-8194,8200,8222,8254,8290-8292,8300,8333,8383,8400,8402,8443,8500,8600,8649,8651-8652,8654,8701,8800,8873,8888,8899,8994,9000-9003,9009-9011,9040,9050,9071,9080-9081,9090-9091,9099-9103,9110-9111,9200,9207,9220,9290,9415,9418,9485,9500,9502-9503,9535,9575,9593-9595,9618,9666,9876-9878,9898,9900,9917,9929,9943-9944,9968,9998-10004,10009-10010,10012,10024-10025,10082,10180,10215,10243,10566,10616-10617,10621,10626,10628-10629,10778,11110-11111,11967,12000,12174,12265,12345,13456,13722,13782-13783,14000,14238,14441-14442,15000,15002-15004,15660,15742,16000-16001,16012,16016,16018,16080,16113,16992-16993,17877,17988,18040,18101,18988,19101,19283,19315,19350,19780,19801,19842,20000,20005,20031,20221-20222,20828,21571,22939,23502,24444,24800,25734-25735,26214,27000,27352-27353,27355-27356,27715,28201,30000,30718,30951,31038,31337,32768-32785,33354,33899,34571-34573,35500,38292,40193,40911,41511,42510,44176,44442-44443,44501,45100,48080,49152-49161,49163,49165,49167,49175-49176,49400,49999-50003,50006,50300,50389,50500,50636,50800,51103,51493,52673,52822,52848,52869,54045,54328,55055-55056,55555,55600,56737-56738,57294,57797,58080,60020,60443,61532,61900,62078,63331,64623,64680,65000,65129,65389'}}, 'scanstats': {'timestr': 'Thu Jan 19 12:54:36 2023', 'elapsed': '4.89', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'192.168.102.145': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '192.168.102.145'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'user-set'}, 'tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'microsoft-ds', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}, 3306: {'state': 'open', 'reason': 'syn-ack', 'name': 'mysql', 'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}}}}}

    # # FULL SERVICE SCAN
    # self.serviceScan = {'nmap': {'command_line': '/snap/nmap/2864/usr/bin/nmap -oX - -A -T4 -Pn -p80,445,3306 192.168.102.145', 'scaninfo': {'tcp': {'method': 'connect', 'services': '80,445,3306'}}, 'scanstats': {'timestr': 'Thu Jan 19 12:58:10 2023', 'elapsed': '46.63', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'192.168.102.145': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '192.168.102.145'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'user-set'}, 'tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.29', 'extrainfo': '(Ubuntu)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.29', 'script': {'http-server-header': 'Apache/2.4.29 (Ubuntu)', 'http-title': 'APEX Hospital'}}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'netbios-ssn', 'product': 'Samba smbd', 'version': '4.7.6-Ubuntu', 'extrainfo': 'workgroup: WORKGROUP', 'conf': '10', 'cpe': 'cpe:/a:samba:samba'}, 3306: {'state': 'open', 'reason': 'syn-ack', 'name': 'mysql', 'product': 'MySQL', 'version': '5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:mariadb:mariadb:5.5.5-10.1.48-mariadb-0ubuntu0.18.04.1', 'script': {'mysql-info': '\n  Protocol: 10\n  Version: 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1\n  Thread ID: 35\n  Capabilities flags: 63487\n  Some Capabilities: Support41Auth, LongColumnFlag, IgnoreSigpipes, DontAllowDatabaseTableColumn, SupportsTransactions, LongPassword, FoundRows, InteractiveClient, ConnectWithDatabase, Speaks41ProtocolOld, Speaks41ProtocolNew, IgnoreSpaceBeforeParenthesis, SupportsLoadDataLocal, ODBCClient, SupportsCompression, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults\n  Status: Autocommit\n  Salt: XY9Pd)<2$](O8g~cWi+8\n  Auth Plugin Name: mysql_native_password'}}}, 'hostscript': [{'id': 'smb2-time', 'output': '\n  date: 2023-01-19T17:57:33\n  start_date: N/A'}, {'id': 'smb-os-discovery', 'output': '\n  OS: Windows 6.1 (Samba 4.7.6-Ubuntu)\n  Computer name: apex\n  NetBIOS computer name: APEX\\x00\n  Domain name: \\x00\n  FQDN: apex\n  System time: 2023-01-19T12:57:31-05:00\n'}, {'id': 'smb2-security-mode', 'output': '\n  311: \n    Message signing enabled but not required'}, {'id': 'clock-skew', 'output': 'mean: 1h40m00s, deviation: 2h53m13s, median: 0s'}, {'id': 'smb-security-mode', 'output': '\n  account_used: guest\n  authentication_level: user\n  challenge_response: supported\n  message_signing: disabled (dangerous, but default)'}]}}}

    # # VULN SCAN 
    # self.vulnersScan = {'nmap': {'command_line': '/snap/nmap/2864/usr/bin/nmap -oX - -sV --script vulners -p 80,445,3306 192.168.102.145', 'scaninfo': {'tcp': {'method': 'connect', 'services': '80,445,3306'}}, 'scanstats': {'timestr': 'Thu Jan 19 12:58:18 2023', 'elapsed': '8.55', 'uphosts': '1', 'downhosts': '0', 'totalhosts': '1'}}, 'scan': {'192.168.102.145': {'hostnames': [{'name': '', 'type': ''}], 'addresses': {'ipv4': '192.168.102.145'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'syn-ack'}, 'tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http', 'product': 'Apache httpd', 'version': '2.4.29', 'extrainfo': '(Ubuntu)', 'conf': '10', 'cpe': 'cpe:/a:apache:http_server:2.4.29', 'script': {'http-server-header': 'Apache/2.4.29 (Ubuntu)', 'vulners': '\n  cpe:/a:apache:http_server:2.4.29: \n    \tCVE-2022-31813\t7.5\thttps://vulners.com/cve/CVE-2022-31813\n    \tCVE-2022-23943\t7.5\thttps://vulners.com/cve/CVE-2022-23943\n    \tCVE-2022-22720\t7.5\thttps://vulners.com/cve/CVE-2022-22720\n    \tCVE-2021-44790\t7.5\thttps://vulners.com/cve/CVE-2021-44790\n    \tCVE-2021-39275\t7.5\thttps://vulners.com/cve/CVE-2021-39275\n    \tCVE-2021-26691\t7.5\thttps://vulners.com/cve/CVE-2021-26691\n    \tCNVD-2022-73123\t7.5\thttps://vulners.com/cnvd/CNVD-2022-73123\n    \tCNVD-2022-03225\t7.5\thttps://vulners.com/cnvd/CNVD-2022-03225\n    \tCNVD-2021-102386\t7.5\thttps://vulners.com/cnvd/CNVD-2021-102386\n    \tEXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB\t7.2\thttps://vulners.com/exploitpack/EXPLOITPACK:44C5118F831D55FAF4259C41D8BDA0AB\t*EXPLOIT*\n    \tEDB-ID:46676\t7.2\thttps://vulners.com/exploitdb/EDB-ID:46676\t*EXPLOIT*\n    \tCVE-2019-0211\t7.2\thttps://vulners.com/cve/CVE-2019-0211\n    \t1337DAY-ID-32502\t7.2\thttps://vulners.com/zdt/1337DAY-ID-32502\t*EXPLOIT*\n    \tFDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8\t6.8\thttps://vulners.com/githubexploit/FDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8\t*EXPLOIT*\n    \tCVE-2021-40438\t6.8\thttps://vulners.com/cve/CVE-2021-40438\n    \tCVE-2020-35452\t6.8\thttps://vulners.com/cve/CVE-2020-35452\n    \tCVE-2018-1312\t6.8\thttps://vulners.com/cve/CVE-2018-1312\n    \tCVE-2017-15715\t6.8\thttps://vulners.com/cve/CVE-2017-15715\n    \tCNVD-2022-03224\t6.8\thttps://vulners.com/cnvd/CNVD-2022-03224\n    \t8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2\t6.8\thttps://vulners.com/githubexploit/8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2\t*EXPLOIT*\n    \t4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332\t6.8\thttps://vulners.com/githubexploit/4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332\t*EXPLOIT*\n    \t4373C92A-2755-5538-9C91-0469C995AA9B\t6.8\thttps://vulners.com/githubexploit/4373C92A-2755-5538-9C91-0469C995AA9B\t*EXPLOIT*\n    \t0095E929-7573-5E4A-A7FA-F6598A35E8DE\t6.8\thttps://vulners.com/githubexploit/0095E929-7573-5E4A-A7FA-F6598A35E8DE\t*EXPLOIT*\n    \tCVE-2022-28615\t6.4\thttps://vulners.com/cve/CVE-2022-28615\n    \tCVE-2021-44224\t6.4\thttps://vulners.com/cve/CVE-2021-44224\n    \tCVE-2019-10082\t6.4\thttps://vulners.com/cve/CVE-2019-10082\n    \tCVE-2019-0217\t6.0\thttps://vulners.com/cve/CVE-2019-0217\n    \tCVE-2022-22721\t5.8\thttps://vulners.com/cve/CVE-2022-22721\n    \tCVE-2020-1927\t5.8\thttps://vulners.com/cve/CVE-2020-1927\n    \tCVE-2019-10098\t5.8\thttps://vulners.com/cve/CVE-2019-10098\n    \t1337DAY-ID-33577\t5.8\thttps://vulners.com/zdt/1337DAY-ID-33577\t*EXPLOIT*\n    \tCVE-2022-30556\t5.0\thttps://vulners.com/cve/CVE-2022-30556\n    \tCVE-2022-29404\t5.0\thttps://vulners.com/cve/CVE-2022-29404\n    \tCVE-2022-28614\t5.0\thttps://vulners.com/cve/CVE-2022-28614\n    \tCVE-2022-26377\t5.0\thttps://vulners.com/cve/CVE-2022-26377\n    \tCVE-2022-22719\t5.0\thttps://vulners.com/cve/CVE-2022-22719\n    \tCVE-2021-34798\t5.0\thttps://vulners.com/cve/CVE-2021-34798\n    \tCVE-2021-33193\t5.0\thttps://vulners.com/cve/CVE-2021-33193\n    \tCVE-2021-26690\t5.0\thttps://vulners.com/cve/CVE-2021-26690\n    \tCVE-2020-9490\t5.0\thttps://vulners.com/cve/CVE-2020-9490\n    \tCVE-2020-1934\t5.0\thttps://vulners.com/cve/CVE-2020-1934\n    \tCVE-2019-17567\t5.0\thttps://vulners.com/cve/CVE-2019-17567\n    \tCVE-2019-10081\t5.0\thttps://vulners.com/cve/CVE-2019-10081\n    \tCVE-2019-0220\t5.0\thttps://vulners.com/cve/CVE-2019-0220\n    \tCVE-2019-0196\t5.0\thttps://vulners.com/cve/CVE-2019-0196\n    \tCVE-2018-17199\t5.0\thttps://vulners.com/cve/CVE-2018-17199\n    \tCVE-2018-17189\t5.0\thttps://vulners.com/cve/CVE-2018-17189\n    \tCVE-2018-1333\t5.0\thttps://vulners.com/cve/CVE-2018-1333\n    \tCVE-2018-1303\t5.0\thttps://vulners.com/cve/CVE-2018-1303\n    \tCVE-2017-15710\t5.0\thttps://vulners.com/cve/CVE-2017-15710\n    \tCNVD-2022-73122\t5.0\thttps://vulners.com/cnvd/CNVD-2022-73122\n    \tCNVD-2022-53584\t5.0\thttps://vulners.com/cnvd/CNVD-2022-53584\n    \tCNVD-2022-53582\t5.0\thttps://vulners.com/cnvd/CNVD-2022-53582\n    \tCNVD-2022-03223\t5.0\thttps://vulners.com/cnvd/CNVD-2022-03223\n    \tCVE-2020-11993\t4.3\thttps://vulners.com/cve/CVE-2020-11993\n    \tCVE-2019-10092\t4.3\thttps://vulners.com/cve/CVE-2019-10092\n    \tCVE-2018-1302\t4.3\thttps://vulners.com/cve/CVE-2018-1302\n    \tCVE-2018-1301\t4.3\thttps://vulners.com/cve/CVE-2018-1301\n    \tCVE-2018-11763\t4.3\thttps://vulners.com/cve/CVE-2018-11763\n    \t4013EC74-B3C1-5D95-938A-54197A58586D\t4.3\thttps://vulners.com/githubexploit/4013EC74-B3C1-5D95-938A-54197A58586D\t*EXPLOIT*\n    \t1337DAY-ID-35422\t4.3\thttps://vulners.com/zdt/1337DAY-ID-35422\t*EXPLOIT*\n    \t1337DAY-ID-33575\t4.3\thttps://vulners.com/zdt/1337DAY-ID-33575\t*EXPLOIT*\n    \tCVE-2018-1283\t3.5\thttps://vulners.com/cve/CVE-2018-1283\n    \tPACKETSTORM:152441\t0.0\thttps://vulners.com/packetstorm/PACKETSTORM:152441\t*EXPLOIT*'}}, 445: {'state': 'open', 'reason': 'syn-ack', 'name': 'netbios-ssn', 'product': 'Samba smbd', 'version': '3.X - 4.X', 'extrainfo': 'workgroup: WORKGROUP', 'conf': '10', 'cpe': 'cpe:/a:samba:samba'}, 3306: {'state': 'open', 'reason': 'syn-ack', 'name': 'mysql', 'product': 'MySQL', 'version': '5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1', 'extrainfo': '', 'conf': '10', 'cpe': 'cpe:/a:mariadb:mariadb:5.5.5-10.1.48-mariadb-0ubuntu0.18.04.1', 'script': {'vulners': '\n  MySQL 5.5.5-10.1.48-MariaDB-0ubuntu0.18.04.1: \n    \tNODEJS:602\t0.0\thttps://vulners.com/nodejs/NODEJS:602'}}}}}}

    # self.fullPortScan = self.serviceScan

    ############################

    # Clearing out top and bottom window in case user clicks scan agin after enumeration.  This deletes the service buttons and re-disables the brute tab.
    try:

        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=" ")
        MODULES.functions.bottomWindowDelete(window=self.scrollWindowScannerBottom)
        
    except:
        pass

    # Disable entry boxes while scans are running
    self.entryTargetName.config(state='disabled')
    self.entryTargetIP.config(state='disabled')

    # Getting values from text boxes
    self.TargetName = self.entryTargetName.get()
    self.TargetIP = self.entryTargetIP.get()

    # Leaving TargetName blank to give it name of IP.  Thinking about x.x.x.x/24 scans
    if self.TargetName == "":
        self.TargetName = self.TargetIP
    
    # Setting up treaded function
    THREADsetThreads = threading.Thread(target=setThreads, args=(self, ), daemon=True)
    THREADsetThreads.start()
    
    
def setThreads(self):

    # Checking for documents directory
    MODULES.functions.documentsFolderPathCheck(self)

    # Creatng template creds file
    MODULES.write2report.write2Creds(self)

    # Displaying that the target folder has been created. 
    MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText=self.TargetName + " created\n\n")

    # Begin report header
    MODULES.write2report.header2html(self)
    MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Running quick nmap scan...\n\n")

    # Kicking off quick and full nmap scans
    THREADquickNmap = threading.Thread(target=quickNmap, args=(self, ), daemon=True)
    THREADquickNmap.start()
    THREADfullNmap = threading.Thread(target=fullNmap, args=(self, ), daemon=True)
    THREADfullNmap.start()


##################### quickNmap #####################

def quickNmap(self):

    try:

        # Running namp command
        MODULES.functions.quickPortScan(self)
        
    except KeyError:
        # If error occurs, update top window
        MODULES.functions.topWindowUpdate(window=self.scrollWindowScannerTop, updateText="Error!  No ports found...\n\nPlease check details and try again.")
        self.progressBar.stop()
        

##################### fullNmap #####################

def fullNmap(self):

    #time.sleep(1) # Used for testing

    # Updating status label.
    MODULES.functions.statusUpdate(self, statusText="Full port scan in progress...")
    
    # Performing nmap full port scan
    MODULES.functions.fullPortScan(self)
    MODULES.functions.statusUpdate(self, statusText="Full port scan completed...")

    # Writing the full port scan done update at bottom window.
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap full port scan done!\n")

    # Making list of all open ports found
    fullOpenPortList = ','.join(map(str, self.fullOpenPortList))

    MODULES.functions.statusUpdate(self, statusText="Service scan in progress...")
    
    # Running namp service scan
    MODULES.functions.serviceScan(self, fullOpenPortList)
    MODULES.functions.statusUpdate(self, statusText="Service scan complete...")

    # Writing the service scan done update at bottom window.
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap service scan done!\n")

    HTMLheader = "Full service scan results"

    # Function that is needed in order to create multiple labels as open ports are found.
    def applytoLabel():
        # This function is used to write results to html report
        scanSummary = []      

        for port,service in self.dicAllOpenPorts.items():

            serviceProduct = self.serviceScan['scan'][self.TargetIP]['tcp'][port]['product']
            serviceVersion = self.serviceScan['scan'][self.TargetIP]['tcp'][port]['version']

            scanSummary.extend([[str(port), str(service), serviceProduct + " " + serviceVersion],])
           
        MODULES.write2report.serviceScan2html(self, HTMLheader, scanSummary)

    applytoLabel()

    # Check box for enabling / disabling vulners scan
    if self.skipVulners == False:
        vulnersNmap(self)

    # if self.skipUDP == False:
    #     scanUDP(self)
  
    else:
        wrapUp(self)


# ##################### vulnersNmap #####################

def vulnersNmap(self):

    #time.sleep(1) # Used for testing

    # Updating status label.
    MODULES.functions.statusUpdate(self, statusText="Vulners scan in progress...")

    # Local list variable of open ports 
    fullOpenPortList = ','.join(map(str, self.fullOpenPortList))
   
    # Running the nmap vulners scan
    MODULES.functions.vulnersScan(self, fullOpenPortList)

    def applytoLabel():

        # This function is used to write results to html report
        for port in self.fullOpenPortList:
            HTMLheader = "Vulners scan results for port: " + str(port)
            vulnList = []

            try:
                vulnSummary = self.vulnersScan['scan'][self.TargetIP]["tcp"][port]["script"]["vulners"] + '\n'
                
                # Removing empty strings
                vulnSummary = "".join([s for s in vulnSummary.splitlines(True) if s.strip("\r\n")])

                ### PRINTING FIRST LINE:
                vulnSummaryHeader = vulnSummary.partition('\n')[0]
                
                ### PRINTING RESULT LINES:
                vulnSummary = vulnSummary.partition("\n")[-1]

                ### SPLITTING LINES TO INDIVIDUAL LINES
                vulnList = vulnSummary.split("\n")

                vulnList2 = []
                for line in vulnList:
                    if line != "":
                        vulnList2.append(line.split())

                HTMLheader = "Vulners scan results for port: " + str(port) + vulnSummaryHeader
                MODULES.write2report.vulnScan2html(self, HTMLheader, vulnList2)

            except KeyError:
                pass
            
    applytoLabel()
   
    MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap vulners scan done!\n")
    wrapUp(self)



def scanUDP(self):
    pass

    # time.sleep(1) # Used for testing

    # # Updating status label.
    # MODULES.functions.statusUpdate(self, statusText="UDP port scan in progress...")

    # # Running namp command
    # #self.fullPortScan = nm.scan(self.TargetIP, arguments='-Su -T4 -Pn -p')   
    # MODULES.functions.statusUpdate(self, statusText="UDP port scan completed...")

    # # Writing the full port scan done update at bottom window.
    # MODULES.functions.bottomWindowUpdate(window=self.scrollWindowScannerBottom, updateText="nmap UDP port scan done!\n")


def wrapUp(self):

    # Changing permission to regular user from sudo, making report and creds files easier to access
    os.chown("/home/" + self.userName + "/Documents/" + self.TargetName + "/creds.txt", self.uid, self.gid)
    os.chown("/home/" + self.userName + "/Documents/" + self.TargetName + "/report.html", self.uid, self.gid)
    
    MODULES.functions.statusUpdate(self, statusText="All scans complete!")

    # Stop the progress bar
    self.progressBar.stop()

    # Make the enumeration button
    self.enumButton = MODULES.functions.buttonMaker(frameName=self.frameScanner, text="Enumeration")
    self.enumButton.place(anchor="nw", x=525, y=550)
    self.enumButton.configure(command=lambda:MODULES.Enumeration.enumeration(self), width=10)