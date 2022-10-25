import telebot
import random
from config import *

api = "5714684314:AAFLa85bhpPPR7d6CDQOZps3wPb0eg-RkB0"
admin = 5795091740
bot = telebot.TeleBot(api, parse_mode="markdown")
kirim = bot.send_message 
lanjut = bot.register_next_step_handler 
kopi = bot.copy_message 

kenapa = ["gatau", "ntahlah", "tanya orang lain aja", "yntkts", "karna because tidak pernah never", "bodoamat", "apasiii wibu gaboleh nanya", "karna lu wibu", "karna aku mencintaimu", "karna kamu jelek", "pikir sendiri", "tanya google aja"]

kapan = ["mungkin sekarang", "1 jam lagi", "2 jam lagi", "8 jam lagi", "hari ini", "mungkin besok", "besok lusa", "sebulan lagi", "setahun lagi", "sewindu lagi", "tahun lalu", "tahun 1945 17 agustus", "tahun 2070", "diem deh gausah nanya", "apasi wibu", "pikir sendiri", "seabad lagi", "5000 SM", "minggu ini", "tahun ini"]

apakah = ["betul", "tidak", "iya", "ga", "kepo deh", "diem deh gausah nanya mulu", "bisa jadi si", "kurang tau", "bodo ah", "hmm", "ga mungkin", "kayanya iya", "mungkin aja", "mustahil", "pikir sendiri", "sudah pasti", "yoiii"]



@bot.message_handler(commands=["help", "start", "bcast"])
def perintah(message):
	id = message.chat.id
	teks = message.text
	mid = message.message_id
	with open("group.txt", "a+") as file:
			file.seek(0)
			value = str(id)
			lines = file.read().splitlines()
			if value in lines:
				print("Y")
			else:
				value = str(value)
				file.write(value + "\n")
	if "/start" in teks:
		kirim(id, "*Saya adalah bot yang dapat menjawab pertanyaan dalam group maupun private chat.\n\nketik /help untuk panduan\n\nby @garzproject*", reply_to_message_id=mid)
	elif "/help" in teks:
		kirim(id, "*# cara menggunakan bot #*\n\n_silahkan beri pertanyaan apakah, kapan, kenapa beserta pertanyaannya.\n\ncontoh pertanyaan:\n\nkapan aku menjadi anime?\n\napakah aku bisa menjadi raja iblis?\n\nkenapa aku terlalu tampan?_", reply_to_message_id=mid)
	elif "/bcast" in teks:
		if id == int(admin):
			pesan = kirim(id, "_silahkan masukan pesan anda..._")
			lanjut(pesan, bcast)
		else:
			kirim(id, "*perintah ini hanya untuk admin!!*")



@bot.message_handler(content_types=["text"], chat_types=["private", "group", "supergroup"])
def tanyain(message):
	id = message.chat.id
	with open("group.txt", "a+") as file:
			file.seek(0)
			value = str(id)
			lines = file.read().splitlines()
			if value in lines:
				print("Y")
			else:
				value = str(value)
				file.write(value + "\n")
	mid = message.message_id
	
	
	
	try:
		teks = message.text.split(" ")
		tt = teks[0]
		tt2 = teks[1]
		data = tt.lower()
		if data == "apakah":
			apa = random.choices(apakah)
			kirim(id, apa, reply_to_message_id=mid)
		elif data == "kapan":
			kpn = random.choices(kapan)
			kirim(id, kpn, reply_to_message_id=mid)
		elif data == "kenapa":
			knp = random.choices(kenapa)
			kirim(id, knp, reply_to_message_id=mid)
	except:
		print("not valdi")
	
def bcast(message):
	id = message.chat.id 
	pesans = message.message_id
	with open("group.txt", "r") as file:
				lines = file.read().splitlines()
				for x in lines:
					try:
						yy = int(x)
						kopi(yy, id, pesans)
					except:
						print(f"{x} pengguna tidak terdaftar")
	kirim(id, "Pesan broadcast berhasil dikirim.")
		
		
bot.infinity_polling()
		
		
