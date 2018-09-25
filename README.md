
# Barax bot 
<img src="https://github.com/pharzan/barax_bot/blob/master/docs/logo.png" alt="Smiley face" width="180">

## A Telegram Voice/Sound Reverse Bot

<p>A simple telegram bot written in python to reverse voice messages it recieves.</p>

### Test:
<p>You can use this <a href="http://t.me/barax_bot">link</a> to test the bot.</p>

### Installation and Usage:
Before anything you can clone the repository using:
```
git clone https://github.com/pharzan/barax_bot.git
```
#### Get a Token:
1. Using the bot father create a Telegram bot to obtain a _Token_ explained [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
The bot father will chat with you through the process of obtaining a token.
Then replace the obtained token in the source code.
The token should look something like this:
```
123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
```
#### Install required packages


2. Install [Telepot](https://telepot.readthedocs.io/en/latest/reference.html) for Python to use the Telegram API in python.
```
pip install telepot
pip install telepot --upgrade  # UPGRADE
```
Or using Easy install:
```
easy_install telepot
easy_install --upgrade telepot  # UPGRADE
```
3. Use python to run the script.
```
python barax_bot.py
```
### How it works:
The bot uses [subprocesses](https://docs.python.org/3/library/subprocess.html) in python to execute a 
[ffmpeg](https://www.ffmpeg.org/), handy Linux utility for audio and video.

The bot listens to any messages that are recieved.
```python
    def on_chat_message(self, msg):
        content_type, chat_type, chat_id, msg_date, msg_id = telepot.glance(msg,flavor='chat',long=True)
```
If the recieved message is a voice message and the duration is less than 30 seconds it downloads the file.
```python
file_name = msg['voice']['file_id']
bot.download_file(msg['voice']['file_id'],"{0}.ogg".format(file_name))
```
Finally it executes ffmpeg in the shell to simply reverses the ogg file and creates an MP3 to send to the user.
```python
shell_cmd = "yes y | ffmpeg -i {0} -vf reverse -af areverse -f mp3 {1}.mp3".format(my_file,file_name)
p = subprocess.Popen(shell_cmd, shell=True,stdout=subprocess.PIPE)
....
bot.sendVoice(chat_id,open(file_name+'.mp3', 'rb'))

```
Notice: The chat ID is a unique ID created by Telegram which is an identifier between the bot and user chat.

