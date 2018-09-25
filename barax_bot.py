
import random,time,os,telepot,threading
from pathlib import Path
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space,per_callback_query_chat_id,include_callback_query_chat_id
import subprocess

TOKEN = "-----BOT TOKEN GOES HERE ----"
class Barax(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Barax, self).__init__(*args, **kwargs)
        self._count = 0
        self.result_counter = 0
        self.result_msg = None
        self.all = None
        self._id = 0
        self.mode = 'main'

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg,flavor='chat',long=True)

        if content_type == 'voice':
        	duration = msg['voice']['duration']
        	if(duration)>30:
        		print("ERR: Longer than 30 seconds.")
        		bot.sendMessage(chat_id,"Ok, I don't want to deal with messages longer than 30 seconds.")
        		return
        	file_name = msg['voice']['file_id']
        	bot.download_file(msg['voice']['file_id'],"./file.ogg")
        	my_file = Path("./file.ogg")

        	while not my_file.is_file():
        		time.sleep(2)

        	start_time = time.time()
        	shell_cmd = "yes y | ffmpeg -i file.ogg -vf reverse -af areverse -f mp3 "+ file_name+".mp3"
        	p = subprocess.Popen(shell_cmd, shell=True,stdout=subprocess.PIPE)

        	while(p.wait() != 0):
        		time.sleep(2)
                
        	elapsed_time = time.time() - start_time
        	print("Time Elapsed: ", elapsed_time)
        	bot.sendVoice(chat_id,open(file_name+'.mp3', 'rb'))
        	return None
   
bot = telepot.DelegatorBot(TOKEN, [
	include_callback_query_chat_id(
    pave_event_space())(
        per_chat_id(), create_open, Barax, timeout=90)
])
MessageLoop(bot).run_as_thread()
answerer = telepot.helper.Answerer(bot)
print('Listening ...')

while 1:
    time.sleep(10)