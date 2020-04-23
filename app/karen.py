import  os
import re
import sys 
import wikipedia
import auto.start
from urllib.request import urlopen 
from bs4 import BeautifulSoup as soup

class Karen(): 

    def __init__(self, sr):
        self.sr = sr
        self.recognizer = self.sr.Recognizer()
        self.microphone = self.sr.Microphone()
        self.is_connected = auto.start.is_connected()

        
        self.intro = 1

    def respond(self, audio):
        "speaks audio passed as argument" 
        print(audio)   
        os.system(f"espeak '{audio}'")

        # for line in audio.splitlines(): 
        #     # print(line)

    def command(self):
        "listens for commands" 
        with self.sr.Microphone() as source:

            if self.intro:
                self.respond("Hey, I am karen, your personal assitant how may I be of help")
                self.intro = 0

            print('Say something...')
            self.recognizer.pause_threshold = 1.5
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = self.recognizer.listen(source)
        
        if self.is_connected:
            try: 
                command = self.recognizer.recognize_google(audio).lower()
                print('You said: ' + command + '\n') 
            #loop back to continue to listen for commands if unrecognizable speech is received
            except self.sr.UnknownValueError:
                print('....')
                command = self.command();
            return command
        self.respond('Please check your internet connection') 

    def run(self, command):  

        # playground
        if 'hi karen' in command:
            self.respond('Hi to you')
        
        elif 'danny devito' in command:
            self.respond('Omg! I. Am. His. Biggest. Fan! Pass my regards')
        
        elif 'feeling today' in command:
            self.respond('I do not have feelings, yet. Maybe soon I will.')

        elif 'you are a robot' in command:
            self.respond('How do you know you are human') 

        elif 'tell me about' in command:

            reg_ex = re.search('tell me about (.*)', command)

            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    self.respond(ny.content[:10].encode('utf-8'))
            except Exception as e:
                    print(e)
                    self.respond(e)

        elif 'news for today' in command:

            try:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()
                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:5]:
                    print(news)
                    self.respond(news.title.text.encode('utf-8')) 
            except Exception as e:
                    print(e) 

        elif 'shutdown' in command:
            self.respond('Bye bye! Have yourself a good one.')
            sys.exit()

        else:
            self.respond('Unfortunately, I do not understand. ' + command)