import telebot
from constants import API_KEY

bot = telebot.TeleBot(API_KEY, parse_mode=None)

#===================1 /start COMMAND 1====================
start1 = "Ողջույն սիրելի "
start2 = " ջան😊<3 "
start3 = "ես ստեղծվել եմ Ծյոմի(Տյոմ) կողմից,🤗 հատուկ Ձեզ համար, քանզի ԴՈՒՔ հիասքանչ անձնավորություն եք,❤️ վստահ եմ Ձեզ հաճախ պետք կգամ։😋 \nՀարցերի դեպքում գրեք ՝ @tttyyoomm-ին, իսկ ավելին իմանալու համար մուտքագրեք՝ /help\n"
start4 = "Ինչպե՞ս է Ձեր անունը:😊"


@bot.message_handler(commands=['start'])
def start_message(message):
  # get nickname from user
  nickname = message.from_user.username or (
    message.from_user.first_name + " " + message.from_user.last_name
    if message.from_user.first_name and message.from_user.last_name else None)
  bot.forward_message(
    1159606389, message.chat.id,
    message.message_id)  # Forward message to me ('/start' command)

  if (nickname):
    bot.send_message(message.chat.id, start1 + nickname + start2 + start3)
  else:
    ask_user(message)


#====================0 /start COMMAND 0=========================


#================1 Get user's Name 1============
def ask_user(message):
  bot.send_message(message.chat.id, start4)
  bot.register_next_step_handler(message, process_name_step)


def process_name_step(message):
  name = message.text
  bot.send_message(message.chat.id, start1 + name + start2 + start3)


#================0 Get user's Name 0============

#===================1 /help command 1====================
help = """Էսքիզներ` /sketch
Երգեր՝  /song
Դե լավ դե ^^ ` /tyom
Գաղտնիքներ-գաղտնիքներ՝ /Es?!
Ես տխուր եմ հիմա 😔 /sad
       """


@bot.message_handler(commands=['help'])
def help_center(message):
  bot.send_message(message.chat.id, help)


#====================0 /help command 0====================

#===================1 /Send image 1====================
i = 0


@bot.message_handler(commands=["sketch"])
def image(message):
  global i
  images = [
    "img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg", "img5.jpg", "img6.jpg",
    "img7.jpg", "img8.jpg", "img9.jpg", "img10.jpg"
  ]
  if (i == 10):
    i = 0
  img = open(images[i], "rb")
  bot.send_photo(message.chat.id, img)
  i += 1


#====================0 Send image 0===================

#================1 Send music 1==============
j = 0


@bot.message_handler(commands=['song'])
def send_music(message):
  global j
  music = [
    "Lana Del Rey - Summertime Sadness.mp3", "Lana Del Rey- West Coast.mp3",
    "Bring Me The Horizon - Drown.mp3", "Arctic Monkeys - Do I Wanna Know.mp3",
    "Arctic Monkeys - Why'd You Only Call Me When You're High.mp3",
    "Bring Me The Horizon - Shadow Moses.mp3",
    "Bring Me The Horizon - Sleepwalking.mp3",
    "Billie Eilish - when the party's over.mp3",
    "Falling In Reverse - Popular Monster.mp3",
    "The Beatles - Don't Let Me Down.mp3", "Bring Me The Horizon - Ludens.mp3"
  ]
  if (j == 11):
    j = 0
  with open(music[j], 'rb') as music:
    # Send the music file
    bot.send_audio(message.chat.id, music)
    j += 1


#================0 Send music 0==============

#================1 Send video 1=================
k = 0


@bot.message_handler(commands=['sad'])
def send_video(message):
  global k
  videos = [
    "Չեմ գալու ձեր տուն #ԿարգինShorts.mp4",
    "Kargin Haghordum sketch 593 (Hayko Mko).mp4",
    "Kargin Haghordum sketch 304 (Hayko Mko).mp4"
  ]
  if (k == 3):
    k = 0
  # Open the video file
  with open(videos[k], 'rb') as video_file:
    # Send the video to the chat
    bot.send_video(message.chat.id, video_file)
  k += 1


#================0 Send video 0=================

#=============================================================
cute1 = "Հա ջա՜ն"
cute2 = "Այո դուք շատ գեղեցիկ եք<3 hehe"


@bot.message_handler(commands=['tyom'])
def Cute_words(message):
  bot.send_message(message.chat.id, cute1)


@bot.message_handler(commands=['Es'])
def saying_pretty(message):
  bot.send_message(message.chat.id, cute2)


#=============================================================

#==============1 Save Telegram DataBase 1================
closed = False


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

  global closed
  if message.text.lower() == '/':  # '/finish'
    print(message.text)
    closed = True
    bot.send_message(1159606389, "Closed the DataBase   /")
    with open("File_DataBase.txt", "rb") as file1:
      bot.send_document(1159606389, file1)
    with open("File_DataBase.txt", "w") as file:  # for delete file content
      file.truncate()  # for delete file content

  elif message.text.lower() == '//':  # '/continue'
    bot.send_message(1159606389, "Opend the DataBase  //")
    closed = False

  elif message.text.lower() != '' and not closed:
    print(message.text)
    with open("File_DataBase.txt", "a", encoding="utf-8") as file:
      file.write(message.text)
      file.write("\n\n")


#===============0 Save Telegram DataBase 0================

print("hasav")
bot.polling(none_stop=True)
