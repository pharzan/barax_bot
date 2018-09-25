import random,time,os,telepot,threading
from pathlib import Path
from telepot.loop import MessageLoop
from telepot.delegate import per_chat_id, create_open, pave_event_space,per_callback_query_chat_id,include_callback_query_chat_id
import subprocess

TOKEN = " --- Bot Token Goes Here ---"

class Barax(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Barax, self).__init__(*args, **kwargs)
        self._id = 0

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg,flavor='chat',long=True)

        if content_type == 'voice':
            duration = msg['voice']['duration']
            if(duration)>30:
                print("ERR: Longer than 30 seconds.")
                bot.sendMessage(chat_id,"Ok, I don't want to deal with messages longer than 30 seconds.")
                return
            file_name = msg['voice']['file_id']
            bot.download_file(msg['voice']['file_id'],
                              "{0}.ogg".format(file_name))
            my_file = Path("./{0}.ogg".format(msg['voice']['file_id']))

            while not my_file.is_file():
                time.sleep(2)

            start_time = time.time()
            shell_cmd = "yes y | ffmpeg -i {0} -vf reverse -af areverse -f mp3 {1}.mp3".format(my_file,file_name)
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