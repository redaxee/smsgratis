#RedAxee
import time;
from requests import Session
import re, sys
s = Session()
localtime = time.asctime( time.localtime(time.time())  )
try:
        print("=====================================")
        print("Minimal 7 huruf \nAwalan Menggunkan 08 ex : 08xxxxxxxxx ")
        print("Date Time :",localtime)
        print("=====================================")
        no = int(input("Nomer Tujuan  : "))
        msg = input("Pesan : ")
except:
        print("\n\t* Cek Nomer Tujuan Atau Pesan Anda Mungk>
        sys.exit()

headers = { 'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36',
            'Referer': 'http://sms.payuterus.biz/alpha/'} 
          
bypass = s.get("http://sms.payuterus.biz/alpha/?a=keluar",
	 headers=headers).
	 textkey = re.findall(r'value="(\d+)"',
	 	 bypass)[0]jml = re.
	 	 findall(r'<span>(.*?) = </span>',
	 bypass)[0]captcha = eval(jml.replace("x", "*").
	 replace(":", "/")) 
	 data = {	
	     'nohp':no,
	 	'pesan':msg,	
	 	'captcha':captcha,	
	 	'key':key} 
send = s.post("http://sms.payuterus.biz/alpha/send.php",
	 headers=headers, data=data).
	 text if 'SMS Gratis Telah Dikirim' in send:	
	 	print(f"\nSukses dikirim! \n[{no}] => {msg}")
	 	elif 'MAAF....!' in send:	
	 		print("\n\t* Mohon Tunggu 5 menit Untuk Sms ke nomer yang Sama *")
	 		else:	
	 			print("\n\t* Gagal dikirim! *")
