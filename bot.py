from telebot import TeleBot
from requests import get,post
from random import choice
from threading import Thread
#token='6335490221:AAE1vzDGY5HpxYSAZj81EQzNWzBjj_NQ0f0'

token='7189166882:AAG6m9re3OIcyMgF8umA7Hf_XRlQATp0sWk'

from json import dump,load

def get_data(file):
	with open(file,'r') as d:
		s=load(d)
	return s

def plus(file,text):
	h=get_data(file)
	h.append(text)
	with open(file,'w') as d:
		dump(h,d)

def check_it(file,ids):
	f=get_data(file)
	if ids in f:
		return True
	else:
		return False

def check_write_it(file,chat_id):
	if check_it(file,chat_id):
		pass
	else:
		plus(file,chat_id)

def get_len(file):
	g=get_data(file)
	return len(g)


def sets(file):
	e=get_data(file)
	with open(file,'w') as d:
		dump(set(e),d)


def get_user(chat_id):
	g=get(f'https://api.telegram.org/bot{token}/getChat?chat_id={str(chat_id)}')
	try:
		t='@'+g.json()['result']['username']
	except:
		t='tg://openmessage?user_id='+str(chat_id)
	return t

def get_admin():
	h=get_data('adm.json')
	return h
def plus_amdin(chat_id):
	g=get_admin()
	plus('adm.json',str(chat_id))

def del_admin(chat_id):
	g=get_admin().remove(str(chat_id))
	with open('adm.json','w') as d:
		dump(g,d)



def get_adm():
	g=get_admin()
	text='''
	الادمنيه
:::::::::::::::::::: \n

	'''
	for i in g:
		r=get(f'https://api.telegram.org/bot{token}/getChat?chat_id={str(i)}').json()['result']
		for i,io in r.items():
			if i=='username':
				text+='username : @'+io+'\n'
				text+='id : '+str(r['id'])+'\n'+'*******************************'
			elif i=='id':
				text+=f'''
				id : {io}

				url : tg://openmessage?user_id={io}

				'''+'\n'


	return text






cards='''
2UE80T6HUF57R4RD
K44BZ3ZMPZSP65S3
BGMS37NMY87XMGMG
DMZ0F3539E7UY6MK
38WUNBRE087MNR02
2NZD4XVDD09ECSPF
3BRF35YM9V50VC4Z
HMKATSPEDF9AY7TG
GMCHZBN03H74M4YX
HM0FWMDT8KU7BFHF
2GF2KMFGDRFB7GHV
3NFHM1J88MUHNE96
HMKATSPEDF9AY7TG
BMYSH198YGEE0N6Y
2SCLU8MPSSGN3MH4
2NZD4XVDD09ECSPF
7BV3UAMVCFFYMXHH
HMKATSPEDF9AY7TG
50EX9VSGA0PR2YNH
1GPZ6P2W8C3S6JJD
2SCLU8MPSSGN3MH4
3VT94HP9H039M9P9
50EX9VSGA0PR2YNH
7BV3UAMVCFFYMXHH
'''.split()

card_random=lambda :choice(cards)



ad_text='''

انت الادمن

مرحبا انا بوت وضيفتي اعطاءك بطاقات مجانيه مضمونه 100%

مميزات

* اقوم بأعلان هديه بطاقه مجانيه كل يوم لشخص عشوائي

* اقوم بأرسال هديه بطاقه الى جميع المستخدمين و الذي يحصل عليها هو اول من يعبئها


الاستعمال

/start ارسل الامر للبدء

/help ارسل الامر للمساعده

/check ارسل الامر للتحقق من انك اشتركت بالقناه لكي تأخذ البطاقه

/card ارسل الامر لكي تأخذ البطاقه المجانيه

/admen ارسل لكي تعرف اوامر الادمن

**************************************

'''






start_text='''
مرحبا انا بوت وضيفتي اعطاءك بطاقات مجانيه مضمونه 100%

مميزات

* اقوم بأعلان هديه بطاقه مجانيه كل يوم لشخص عشوائي

* اقوم بأرسال هديه بطاقه الى جميع المستخدمين و الذي يحصل عليها هو اول من يعبئها


الاستعمال

/start ارسل الامر للبدء

/help ارسل الامر للمساعده

/check ارسل الامر للتحقق من انك اشتركت بالقناه لكي تأخذ البطاقه

/card ارسل الامر لكي تأخذ البطاقه المجانيه

**************************************

'''

channals=['p5_0k','DS_5K']


def rechan(chan_id,chat_id):
	#chan_id=chan_id[13:]
	try:
		rt=get(f'https://api.telegram.org/bot{token}/getChatMember?chat_id=@{chan_id}&user_id={chat_id}').json()
		#print(rt)
		if rt['ok']==False:
			return False
		else:
			return True
	except:
		bot.send_message(myid,f'حدث خطا عند فحص القناه للشخص {chat_id} للقناه {chan_id}')


uch=lambda x:'https://t.me/'+x

ad_ad='''

اوامر الادمن

المستخدمون : لعرض عدد المستخدمون

الادمنيه : لعرض عدد الادمنيه

ارسال الهديه : لارسال الهديه العشواءيه

اعلان : لعمل اعلان يتم ارساله لكل المستخدمون

تصفيه : لتصفيه المستخدمون الذي حضرو البوت

تفعيل البطاقه : ليأخذ كل شخص بطاقه

'''


def check_chan(chat_id):
	r=[]
	for i in channals:
		s=rechan(str(i),str(chat_id))
		if s==False:
			r.append(i)
		else:
			pass
			#r.append(i)
	if r:
		text='''لقد نسيت ان تشترك بهاذه القنوات
		اشترك ثم اكتب الامر التالي للتحقق

		 /check \n
		'''
		for i in r:
			text+=uch(i)+'\n'
		return text
	else:
		if check_it('users.json',str(chat_id)):
			text='''
			لقد ربحت بطاقتك مؤخرا انتضر الهدايه و الجوائز اليوميه

			'''
		else:
			plus('users.json',str(chat_id))
			text='''
		مبروك لقد ربحت بطاقه مجانيه

		لا تقم بأعطاء كود البطاقه لاي شخص مهما كان

		اذا لم تقم بتعبئه البطاقه سيتم اعطاءها لشخص اخر

		كود البطاقه اسفل


		{}

		________________________________


		'''.format(card_random())



		return text


def thsend(text,idn):
	g=get_data('ids.json')
	for i in g:
		try:
			if str(i)==str(idn):
				pass
			else:

				bot.send_message(int(i),text)
		except:
			pass



myid='6018588578'

#admenid=['6018588578']

bot=TeleBot(token)


@bot.message_handler(commands=['start','help'])
def start(message):
	ids=message.chat.id
	if str(ids) in get_admin() or str(ids) == myid:

		check_write_it('ids.json',str(ids))
		bot.send_message(ids,ad_text)
	else:
		check_write_it('ids.json',str(ids))
		bot.send_message(ids,start_text)

@bot.message_handler(commands=['card'])
def card(message):

	ids=message.chat.id
	check_write_it('ids.json',str(ids))
	t=''
	for i in channals:
		t+=uch(i)+'\n\n'


	text='''
	اشترك بهاذه القنوات ثم ارسل الامر التالي للتحقق

	/check

	لكي تحصل على البطاقات المجانيه


	{}


			اذا كنت تعتقد بأنك تملك قناه و تريد ان تضيفها
	فيجب عليك التواصل مع صاحب البوت

	*****************************
	'''.format(t)

	bot.send_message(ids,text)

def f_g1(text):
	g=get_data('ids.json')
	try:
		for i in g:
			post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={i}&text={text}')
	except:
		pass

def g1(text,chat_id):
	if chat_id in get_admin() or chat_id==myid:
		if text.startswith('اعلان'):
		#if chat_id in admenid or chat_id==myid:
			text=text[len('اعلان '):]
			Thread(target=f_g1,args=(text,)).start()


def g2(text,chat_id):
	if chat_id==myid:
		if text.startswith('اضف ادمن '):
			ti=text[len('اضف ادمن '):]
			plus_amdin(ti)
			bot.send_message(int(chat_id),'تم اضافه الادمن')

def g3(text,chat_id):
	if chat_id==myid:
		if text.startswith('حذف ادمن '):
			ti=text[len('حذف ادمن '):]
			del_admin(ti)
			bot.send_message(int(chat_id),'تم حذف الادمن')

def g4(text,chat_id):
	if chat_id in get_admin() or chat_id==myid:
		if text.startswith('الادمنيه'):
			bot.send_message(int(chat_id),get_adm())

def g5(text,chat_id):
	if chat_id==myid or chat_id in get_admin():
		if text.startswith('المستخدمون'):
			tiop='عدد المستخدمون ({})'.format(get_len('ids.json'))
			bot.send_message(int(chat_id),tiop)

def g6(text,chat_id):
	if chat_id==myid or chat_id in get_admin():
		if text.startswith('ارسال الهديه'):
			t=get_data('ids.json')
			g=choice(t)
			text='''
			مبروك لقد ربحت الهديه العشوائيه

			لا تشارك البطاقه مع اي احد مهما كان
			اذا لم تقم بتعبئه البطاقه سيتم اعطاءها لشخص اخر

			كود البطاقه اسفل


			{}


		______________________

			'''.format(card_random())
			tp='''
			خطاء ناتج عن محاوله ارسال البطاقه الى الشخص التالي

			ربما يكون قد حضر البوت


			{}


			'''.format('tg://openmessage?user_id='+g)
			tc='''
			لقد فاز هاذا المستخدم بالبطاقه العشوائيه لليوم

			{}
			'''.format(get_user(g))
			try:
				bot.send_message(int(g),text)
				Thread(target=thsend,args=(tc,g)).start()
			except:

				bot.send_message(myid,tp)

def f_g7(text,chat_id):
	h=get_data('ids.json')
	for i in h:
		k=get_user(i)
		if k:
			pass
		else:
			h.remove(i)

	with open('ids.json','w') as d:
		dump(h,d)
	bot.send_message(int(chat_id),'تمت التصفيه بنجاح')
def g7(text,chat_id):
	if chat_id in get_admin() or chat_id==str(myid):
		if text.startswith('تصفيه'):
			Thread(target=f_g7,args=(text,chat_id)).start()


def f_g8(text,chat_id):
	with open('users.json','w') as d:
		d.write('[]')

	text='''
	تم التفعيل
	البطاقه متاحه يمكنك ان تأخذها ارسل الامر التالي لأخذ بطاقه

	/check

	'''

	Thread(target=thsend,args=(text,'66')).start()

def g8(text,chat_id):
	if chat_id in get_admin() or chat_id==str(myid):
		if text.startswith('تفعيل البطاقه'):
			f_g8(text,chat_id)


@bot.message_handler(commands=['check'])
def check(message):
	ids=message.chat.id
	check_write_it('ids.json',str(ids))
	text=check_chan(str(ids))
	bot.send_message(ids,text)


@bot.message_handler(commands=['admen'])

def h(message):
	ids=message.chat.id
	if str(ids)==myid or str(ids) in get_admin():
		bot.send_message(ids,ad_ad)

@bot.message_handler(func=lambda message: True)
def ptr(message):
	ids=message.chat.id
	text=message.text
	g1(text,str(ids))
	g2(text,str(ids))
	g3(text,str(ids))
	g4(text,str(ids))
	g5(text,str(ids))
	g6(text,str(ids))
	g7(text,str(ids))
	g8(text,str(ids))




bot.infinity_polling()


