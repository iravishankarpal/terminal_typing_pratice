

# practice typing with news headlines 
# aim typing pratice development 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time
import html5lib
import requests
import urllib.request

def delay(n):
            time.sleep(n)
            os.system("clear")

def game(a):
    
    string = a.casefold()
    word_count = len(string.split())
    print(string)
    t0 = time.time() #start time
    inputText = input()
    t1 = time.time() #stop time  
    acc = len(set(inputText.split()) & set(string.split()))
    acc = acc/word_count*100
    accuracy = round(acc,0)
    timeTaken = t1 - t0
    speed= (word_count/timeTaken)*100
    wordPM = round(speed,1)
    os.system("clear")
    print ("-"*50 + f"{wordPM}wpm | {accuracy}%"+ 50*"-") 


def online():
     # for typing online
        url = "https://inshorts.com/en/read/"
        r = requests.get(url)
        # url_code =   r.text
        # print(url_code)
        # delay(2)
        soup = BeautifulSoup(r.text,"html.parser")
        # print(soup.prettify())
        # delay(2)
               
              
        # for single lline headlines for 1 min
        def one_minutes():
            headline = soup.findAll("span")
            for span in headline:
                 if(span.get('itemprop')=="headline"):
                    #  print(span.text + "\n")
                        game(span.text)
                    

        
        # for its 60 word bordy   for 3 miinutes 
        # def three_minutes():
        #     articleBody = soup.findAll('div')
        #     for div in articleBody:
        #             if(div.get("itemprop")=="articleBody"):
        #                 #  print(div.text + "\n")
        #                  game(div.text)
        
        one_minutes()
        # three_minutes()
def offline():

        state=('''Andhra Pradesh, Assam, Arunachal Pradesh, Bihar, Goa, Gujarat,
        Jammu Kashmir, Jharkhand, West Bengal, Karnataka, Kerala, Madhya Pradesh,
        Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Orissa, Punjab,
        Rajasthan, Sikkim, Tamil Nadu, Tripura, Uttaranchal, Uttar Pradesh,
        Haryana, Himachal Pradesh, Chhattisgarh''').casefold()


        states = state.split(',')
           
        for i in states :
            x = i.strip()
            game(x)



def connect(host='http://google.com'):
  
    try:
        urllib.request.urlopen(host) 
        os.system("clear")
        print( "connected device is online")
        delay(1)
        online()
    except:
            os.system("clear")
            print( "no internet connection or some error")
            delay(2)
            offline()
       

connect()




    
            