import  os
import sys
from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup

class Karen(): 

    def __init__(self, sr):
        self.sr = sr
        self.recognizer = self.sr.Recognizer()
        self.microphone = self.sr.Microphone()

    def respond(self, audio):
        "speaks audio passed as argument"
        print(audio)

        for line in audio.splitlines():
            os.system("say " + audio)

    def command(self):
        "listens for commands" 
        with self.sr.Microphone() as source:
            print('Say something...')
            self.recognizer.pause_threshold = 1
            # self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
        #loop back to continue to listen for commands if unrecognizable speech is received
        except self.sr.UnknownValueError:
            print('....')
            command = self.myCommand();
        return command

    def run(self, command):

        if 'news for today' in command:
            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:15]:
                    self.respond(news.title.text.encode('utf-8'))
            except Exception as e:
                    print(e)

        if 'shutdown' in command:
            self.respond('Bye bye! Have yourself a good one.')
            sys.exit(0)

        print(command + ". Unfortunately, I do not understand your command.")