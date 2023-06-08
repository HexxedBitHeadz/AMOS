import os, re

def header2html(self):

    HeBiLogo=self.amosDir + "/IMAGES/HeBi_Logo.png"

    html = '''
    <?xml version="1.0" encoding="iso-8859-1" standalone="no"?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=iso-8859-1" />
        <title> ''' + self.entryTargetName.get() + ''' Target scan report</title>
    
        <link rel="stylesheet" type="text/css" href="''' + str(self.amosDir) + '''/MODULES/stylesheets/lfs.css" />
    </head>

        <body class="blfs" id="blfs-11.3">
            <div class="report">
                <div class="titlepage">
                    <div>
                        <div>
                            <h1 class="title">
                            Hexxed BitHeadz
                            </h1>
                            <h2 class="subtitle">
                                <img src="''' + HeBiLogo + '''" width="100" height="150"></img><br>
                                <p style="color:white;">''' + self.entryTargetName.get() + ''' Target scan report</p>
                            </h2>
                        </div>
                        <div class="toc">
                            <h3>
                                Table of Contents
                            </h3>
                            <ul>
                                <li class="preface">
                                    <h4>
                                        <a href="#Full">1. Full service scan results</a>
                                    </h4>
                                </li>

                                <li class="preface">
                                    <h4>
                                        <a href="#Vulners">2. Vulners scan results</a>
                                    </h4>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </body>

    '''
    filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/report.html"
    with open(filename, "w") as file:
        file.write(html)
    file.close


def serviceScan2html(self, HTMLheader, element, show=1):

    html = '''
    <body>
        <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
        <div id=''' + HTMLheader + '''></div>
    </body>

    <div class="table-contents">
        <table class="table" summary="Service scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
        <colgroup>
            <col width=".4in" />
            <col width=".4in" />
            <col width=".8in" />
        </colgroup>
        <thead>
            <tr>
                <th>
                    PORT
                </th>
                <th>
                    SERVICE
                </th>
                <th>
                    DETAILS
                </th>
            </tr>
        </thead>
        <tbody>
'''

    portList = [x[0] for x in element]
    serviceList = [x[1] for x in element]
    detailsList = [x[2] for x in element]

    for i in range(len(portList)):
        html += '''<tr><td>''' + str(portList[i]) + '''</td><td>''' + str(serviceList[i]) + '''</td><td>''' + str(detailsList[i]) + '''</td></tr>'''

    html += f'''</tbody></table>'''

    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/report.html"
        with open(filename, "a") as file:
            file.write(html)
        file.close


def vulnScan2html(self, HTMLheader, element, show=1):

    html = '''
    <body>
        <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
        <div id=''' + HTMLheader + '''></div>
    </body>

    <div class="table-contents">
        <table class="table" summary="Vuln scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
        <colgroup>
            <col width=".4in" />
            <col width=".4in" />
            <col width=".8in" />
        </colgroup>
        <thead>
            <tr>
                <th>
                    CVE
                </th>
                <th>
                    SCORE
                </th>
                <th>
                    LINK
                </th>
            </tr>
        </thead>
        <tbody>
'''

    CVEList = [x[0] for x in element]
    scoreList = [x[1] for x in element]
    linkList = [x[2] for x in element]

    for i in range(len(CVEList)):
        html += '''<tr><td>''' + str(CVEList[i]) + '''</td><td>''' + str(scoreList[i]) + '''</td><td>''' + str(linkList[i]) + '''</td></tr>'''

    html += f'''</tbody></table></html>'''

    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/report.html"
        with open(filename, "a") as file:
            file.write(html)
        file.close

def enum2html(self, HTMLheader, element, show=1):

    html = '''
    <body>
        <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
        <div id=''' + HTMLheader + '''></div>
    </body>

    <div class="table-contents">
        <table class="table" summary="Enumeration scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
        <colgroup>
            <col width=".10in" />
        </colgroup>
        <thead>
            <tr>
                <th>
                    DETAILS
                </th>
            </tr>
        </thead>
        <tbody>
'''
    
    productList = [x[0] for x in element]

    for i in range(len(productList)):
         html += '''<tr><td>''' + str(productList[i]) + '''</td></tr>'''

    html += f'''</tbody></table>'''

    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/report.html"
        with open(filename, "a") as file:
            file.write(html)
        file.close


def auth2html(self, HTMLheader, element, show=1):


    html = '''
        <body>
            <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
            <div id=''' + HTMLheader + '''></div>
        </body>

        <div class="table-contents">
            <table class="table" summary="Enumeration scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
            <colgroup>
                <col width=".10in" />
            </colgroup>
            <thead>
                <tr>
                    <th>
                        DETAILS
                    </th>
                </tr>
            </thead>
            <tbody>
    '''
        
    new_list = [item for item in element if item != '']

    for item in new_list:
        html += '''<tr><td>''' + str(item) + '''</td></tr>'''

    html += f'''</tbody></table>'''

    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/report.html"
        with open(filename, "a") as file:
            file.write(html)
        file.close

def webExtract2html(self, HTMLheader, element, show=1):

    header2html(self)

    HeBiLogo=self.amosDir + "/IMAGES/HeBi_Logo.png"

    html = '''
    <?xml version="1.0" encoding="iso-8859-1" standalone="no"?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=iso-8859-1" />
        <title> ''' + self.entryTargetName.get() + ''' extract report</title>
    
        <link rel="stylesheet" type="text/css" href="''' + str(self.amosDir) + '''/MODULES/stylesheets/lfs.css" />
    </head>

        <body class="blfs" id="blfs-11.3">
            <div class="report">
                <div class="titlepage">
                    <div>
                        <div>
                            <h1 class="title">
                            Hexxed BitHeadz
                            </h1>
                            <h2 class="subtitle">
                                <img src="''' + HeBiLogo + '''" width="100" height="150"></img><br>
                                <p style="color:white;">''' + self.entryTargetName.get() + ":" + self.entryWebPort.get() + ''' extraction report</p>
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
        </body>


        <body>
                <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
                <div id=''' + HTMLheader + '''></div>
            </body>

            <div class="table-contents">
                <table class="table" summary="Web scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
                <colgroup>
                    <col width=".4in" />
                </colgroup>
                <thead>

                    <tr>
                        <th>
                            URL
                        </th>
                    </tr>
                </thead>
                <tbody>
        '''


    urlList = [x[0] for x in element]
    linkList = [x[1] for x in element]

    emails_pattern = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
    phone1_pattern = re.compile(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$")
    phone2_pattern = re.compile(r"tel:\+\d{11}")
    urls_pattern = re.compile(r"(?P<url>https?://[^\s]+)")


    emails = re.findall(emails_pattern, str(linkList))
    phone1 = re.findall(phone1_pattern, str(linkList))
    phone2 = re.findall(phone2_pattern, str(linkList))
    urls = re.findall(urls_pattern, str(linkList))

    # Removing emails and telephone numbers from results
    filtered = [i for i in linkList if not emails_pattern.search(i)]
    filtered = [i for i in filtered if not phone1_pattern.search(i)]

    # search for the phone number using regex
    filtered = [i for i in filtered if not phone2_pattern.search(i)]
    filtered = [i for i in filtered if not urls_pattern.search(i)]

    for i in range(len(filtered)):

        html += '''<tr><td><a href=''' + str(urlList[i]) + "/" + str(filtered[i]) + '''> ''' + str(urlList[i]) + "/" + str(filtered[i]) + '''</a></td></tr>'''

    html += f'''</tbody></table><br><br>'''

    html += '''<table class="table" summary="Web scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
                    <colgroup>
                        <col width=".4in" />
                    </colgroup>
                    <thead>
                        <tr>
                            <th>
                                emails
                            </th>
                        </tr>
                    </thead>
                    <tbody>
            '''


    for i in range(len(emails)):

        html += '''<tr><td>''' + str(emails[i]) + '''</td></tr>'''

    html += f'''</tbody></table><br><br>'''

    html += '''<table class="table" summary="Web scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
                    <colgroup>
                        <col width=".4in" />
                    </colgroup>
                    <thead>
                        <tr>
                            <th>
                                phone numbers
                            </th>
                        </tr>
                    </thead>
                    <tbody>
            '''

    for i in range(len(phone1)):

        html += '''<tr><td>''' + str(phone1[i]) + '''</td></tr>'''

    for i in range(len(phone2)):

        html += '''<tr><td>''' + str(phone2[i]) + '''</td></tr>'''

    html += f'''</tbody></table><br><br>'''

    html += '''<table class="table" summary="Web scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
                    <colgroup>
                        <col width="5in" />
                    </colgroup>
                    <thead>
                        <tr>
                            <th>
                                URLs
                            </th>
                        </tr>
                    </thead>
                    <tbody>
            '''

    for link in linkList:
        match = urls_pattern.search(link)
        if match:

            html += '''<tr><td>''' + str(match.group()) + '''</td></tr>'''
    html += f'''</tbody></table><br><br>'''

    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/HTML_report-Extraction-" + self.entryWebPort.get() + ".html"
        with open(filename, "w") as file:
            file.write(html)
        file.close


def dirBust2html(self, HTMLheader, element, show=1):


    header2html(self)


    HeBiLogo=self.amosDir + "/IMAGES/HeBi_Logo.png"

    html = '''
    <?xml version="1.0" encoding="iso-8859-1" standalone="no"?>
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta http-equiv="Content-Type" content="application/xhtml+xml; charset=iso-8859-1" />
        <title> ''' + self.entryTargetName.get() + ''' extract report</title>
    
        <link rel="stylesheet" type="text/css" href="''' + str(self.amosDir) + '''/MODULES/stylesheets/lfs.css" />
    </head>

        <body class="blfs" id="blfs-11.3">
            <div class="report">
                <div class="titlepage">
                    <div>
                        <div>
                            <h1 class="title">
                            Hexxed BitHeadz
                            </h1>
                            <h2 class="subtitle">
                                <img src="''' + HeBiLogo + '''" width="100" height="150"></img><br>
                                <p style="color:white;">''' + self.entryTargetName.get() + ":" + self.entryWebPort.get() + ''' extraction report</p>
                            </h2>
                        </div>
                    </div>
                </div>
            </div>
        </body>

        <body>
            <h1 style="width:650px;background-color: red;">''' + HTMLheader + '''</h1>
            <div id=''' + HTMLheader + '''></div>
        </body>

        <div class="table-contents">
            <table class="table" summary="Web scan results" border="5" width="650px" cellspacing="5" cellpadding="0">
            <colgroup>
                <col width=".4in" />
            </colgroup>
            <thead>

                <tr>
                    <th>
                        URL
                    </th>
                </tr>
            </thead>
            <tbody>
        '''
        
    dirList = [x[0] for x in element]
    
    for i in range(len(element)):
        html += '''<tr><td>''' + str(element[i]) + '''</td></tr>'''
        
    if show == 1:

        filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/HTML_report-DirBust-" + self.entryWebPort.get() + ".html"
        with open(filename, "w") as file:
            file.write(html)
        file.close

def write2Creds(self):
    credsTxtFile = '''admin/admin
    administrator/administrator
    root/root'''

    filename = "/home/" + os.getlogin() + "/Documents/" + self.entryTargetName.get() + "/creds.txt"
    with open(filename, "w") as file:
        file.write(credsTxtFile)
    file.close 
