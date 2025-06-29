import speech_recognition as sr
import pyttsx3 as pyt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time as t
import wikipedia as wiki
import pywhatkit as kit
import webbrowser
from ctypes import windll
from PIL import Image
from io import BytesIO
import pyautogui as gui
from imdb import IMDb
import screen_brightness_control as sbc
import psutil
import requests
import random
import datetime
import os
import geocoder
import pycountry
import pygame 
import re
import smtplib
from plyer import notification
from bs4 import BeautifulSoup
from datetime import datetime
import math
import os
pygame.init()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
recognation = sr.Recognizer()
mic = sr.Microphone()
engine = pyt.init()
battery = psutil.sensors_battery()
global response
command=["add","addition","subtract","difference","multiply","product","division","divide","sum","factorial","square root"]
thanks = [
    "No problem!",
    "You're welcome!",
    "Glad I could help!",
    "Happy to assist!",
    "Anytime!",
    "Of course!",
    "My pleasure!",
    "Don't mention it!",
    "No worries!",
    "Always here to help!"
]

news_channel = ["Geo news live", "Ary news live", "Express news live"]
sender_email = "jarvis111924@gmail.com"
receiver_email = "muhammadhamzao241@gmail.com"
app_password = "ckwi pxyy lrci ezbn" 
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)
breakfast_time="02:00 PM"
dinner_time="07:27 PM"
password="hamza123qwe"

engine.say("Hello i am jarvis")
engine.runAndWait()
t.sleep(2)
engine.say("Tell correct password to activate system")
engine.runAndWait()
user_=str(input(">>>>>>>: "))
if user_==password:
   engine.say("Welcome Sir")
   engine.runAndWait()
   t.sleep(2)
   def my_jarvis():
    now=datetime.now().time()
    formatted_time = now.strftime("%I:%M %p")
    
    if formatted_time==dinner_time:
         engine.say("Sir, its a dinner time")
         engine.runAndWait()
    elif formatted_time==breakfast_time:
         engine.say("Sir, its breakfast time")
         engine.runAndWait()
    with mic as listener:
        recognation.adjust_for_ambient_noise(listener)
        audio = recognation.listen(listener)
        input_name = recognation.recognize_google(audio).lower()
        print(input_name)
        if "weather" in input_name or "tell me weather" in input_name or "multan weather" in input_name:
             response=requests.get("https://muslimsalat.com/Multan.json")
             data2=response.json()
             temperature=data2['today_weather']['temperature']
             engine.say(f"The Weather is {temperature} Celsius")
             engine.runAndWait()
            

        elif "play song" in input_name or "i want to listen song" in input_name or "song" in input_name or "video" in input_name:
            engine.say("Sir, Should I play your playlist on YouTube, or would you suggest a new song?")
            engine.runAndWait()
            
            audio = recognation.listen(listener)
            input_name = recognation.recognize_google(audio).lower()

            if "new song" in input_name or "i will tell" in input_name or "let me tell" in input_name:
                engine.say("Sure sir, tell me the new song name")
                engine.runAndWait()
                 
                audio = recognation.listen(listener)
                song_name = recognation.recognize_google(audio)
                kit.playonyt(song_name)
                engine.say(f"Playing {song_name} for you")
                engine.runAndWait()
            elif "playlist" in input_name or "my favourite" in input_name:
                
                webbrowser.open("https://www.youtube.com/watch?v=RBumgq5yVrA&list=PL1kS2TXl-UMe1JBBdW3qB0XqzGLdJtBKh")
                t.sleep(2)
                engine.say("Playing your playlist, Sir")
                engine.runAndWait()
        elif "search" in input_name or "look for" in input_name or "wikipedia" in input_name:
            engine.say("For whom would you like to search?")
            engine.runAndWait()
            
            audio = recognation.listen(listener)
            search_term = recognation.recognize_google(audio)
            search_result = wiki.summary(search_term, sentences=5)
            engine.say(search_result)
            engine.runAndWait()

        elif "listen news" in input_name or "play news" in input_name:
            engine.say("Sure, sir, I am playing news!")
            engine.runAndWait()
            g = geocoder.ip('me')
            country_code = g.country
            country = pycountry.countries.get(alpha_2=country_code)
            if country.name == "Pakistan":
                choose_news_channel = random.randint(0, 2)
                engine.say(f"Playing {news_channel[choose_news_channel]} for you..")
                engine.runAndWait()
                kit.playonyt(news_channel[choose_news_channel])
            else:
                kit.playonyt("CNN news live")

        elif "close tab" in input_name:
            t.sleep(3)
            engine.say("Closing....")
            engine.runAndWait()
            gui.hotkey('ctrl', 'W')
            engine.say("Done sir")
            engine.runAndWait()

        elif "info about movie" in input_name or "movie information" in input_name or "movie" in input_name:
            ia = IMDb()
            engine.say("For which movie do you want to know?")
            engine.runAndWait()
            
            audio = recognation.listen(listener)
            search_term = recognation.recognize_google(audio)

            movies = ia.search_movie(search_term)
            movie = movies[0]
            movie_id = movie.movieID
            movie_detail = ia.get_movie(movie_id)
            engine.say(f"{movie_detail['plot'][0]}")
            engine.runAndWait()

        elif "increase brightness" in input_name or "brightness" in input_name:
            sbc.set_brightness('+10')
            engine.say("Increased brightness sir")
            engine.runAndWait()
            
            audio = recognation.listen(listener)
            input_name = recognation.recognize_google(audio)

            if "more" in input_name:
                sbc.set_brightness('+30')
                engine.say("Done sir")
                engine.runAndWait()
                
                audio = recognation.listen(listener)
                input_name = recognation.recognize_google(audio)

        elif "battery" in input_name or "tell me my battery" in input_name:
            engine.say(f"Your Current battery is: {battery.percent} percent")
            engine.runAndWait()

        elif "thank" in input_name:
            find_random = random.randint(0, 9)
            engine.say(f"{thanks[find_random]}")
            engine.runAndWait()
        elif "stop" in input_name or "pause" in input_name or "run" in input_name:
            gui.press('space')
            engine.say("Done Sir")
            engine.runAndWait()
        elif "full screen" in input_name or "big screen" in input_name:
            gui.hotkey('f')
            engine.say("Done Sir")
            engine.runAndWait()
        elif "going to sleep" in input_name or "sleep mood" in input_name or "sleep" in input_name:
            sleep_start_time = t.time()
            engine.say("Should I put laptop on sleep mode?")
            engine.runAndWait()
            
            audio = recognation.listen(listener)
            search = recognation.recognize_google(audio)

            if "yes please" in search or "ofcourse" in search:
                engine.say("Putting laptop on sleep mode, Sir")
                engine.runAndWait()
                t.sleep(3)
                os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")

            elif "i am awake" in search or "i am up" in search or "awake" in search:
                sleep_duration = t.time() - sleep_start_time
                hours = int(sleep_duration // 3600)
                minutes = int((sleep_duration % 3600) // 60)
                seconds = int(sleep_duration % 60)

                engine.say(f"You've been sleeping for {hours} hours, {minutes} minutes, and {seconds} seconds.")
                engine.runAndWait()
        elif "quote of the day" in input_name or "thought" in input_name or "lesson of the day" in input_name:
                response = requests.get('https://zenquotes.io/api/random')
                if response.status_code==200:
                    quote_data=response.json()[0]
                    quote=quote_data['q']
                    author=quote_data['a']
                    engine.say("Quote of the day is")
                    engine.runAndWait()
                    t.sleep(1)
                    engine.say(quote)
                    engine.runAndWait()
                    t.sleep(1)
                    engine.say(f"Its written by {author}")
                    engine.runAndWait()
                    engine.say("Would you like to see as a notification")
                    engine.runAndWait()
                    subject = "Quote of the day!! "
                    body = f"Here is Quote of the day: \n{quote}\nIts said by: {author}"
                    message = f"Subject: {subject}\n\n{body}"
                    server.sendmail(sender_email, receiver_email, message)
                    audio = recognation.listen(listener)
                    check_name = recognation.recognize_google(audio).lower()
                    print(check_name)
                    if "of course" in check_name or "yes please" in check_name:
                        t.sleep(2)
                        notification.notify(
                            title="Quote of the Day!",
                            message=f"Quote: {quote}\nAuthor: {author} Date: {datetime.datetime.now().date()}",
                            timeout=6)
                    else:
                        pass
        elif "newspaper" in input_name or "akhbar" in input_name:
            engine.say("Showing today newspaper")
            engine.runAndWait()
            t.sleep(1)
            time1=datetime.datetime.now().strftime('%Y%m%d')
            webbrowser.open(f"https://www.express.com.pk/epaper/Index.aspx?Issue=NP_MUX&Page=FRONT_PAGE&Date={time1}&Pageno=1")  
        elif "today image" in input_name or "today nasa" in input_name or "pic of today" in input_name:
            response=requests.get("https://api.nasa.gov/planetary/apod?api_key=sZlqe4rYZc3N1bmisveVva2L8tM5qLDnzkoS7G6U")
            _image=response.json()
            nasa=_image['hdurl']
            engine.say("Showing image of the day..")
            engine.runAndWait()
            t.sleep(2)
            show=webbrowser.open(nasa)
            t.sleep(5)
            engine.say("Would you like to save it?")
            engine.runAndWait()

            print(nasa)
          
            audio = recognation.listen(listener)
            input_name = recognation.recognize_google(audio).lower()           
            if "yes please" in input_name or "ofcourse" in input_name:
                             gen=random.randint(1,1000)
                             print(gen)
                             user1 = requests.get('https://api.nasa.gov/planetary/apod?api_key=sZlqe4rYZc3N1bmisveVva2L8tM5qLDnzkoS7G6U')
                             with open(f"image_of_day{gen}.jpg", 'wb') as file:
                                     file.write(user1.content)
                                     engine.say("Image saved")
                                     engine.runAndWait()
            else:
                             print("Image not saved.")
        

        elif "namaz" in input_name or "fajar"  in input_name or "johar" in input_name or "asar" in input_name or "maghrib" in input_name or "isha" in input_name:
             if "fajar" in input_name:
                  response=requests.get("https://muslimsalat.com/Multan.json")   
                  data3=response.json()
                  fajr=data3['items'][0]['fajr']  
                  engine.say(f"Today Fajr prayer time is: {fajr}")
                  engine.runAndWait()
             elif "johar" in input_name:
                  response=requests.get("https://muslimsalat.com/Multan.json")
                  data3=response.json()
                  zohar=data3['items'][0]['dhuhr']
                  engine.say(f"Today zohar prayer time is: {zohar}")
                  engine.runAndWait()
             elif "asar" in input_name:
                  response=requests.get("https://muslimsalat.com/Multan.json")
                  data3=response.json()
                  asar=data3['items'][0]['asr']
                  engine.say(f"Today Asr time is: {asar}")
                  engine.runAndWait()
             elif "maghrib" in input_name:
                  response=requests.get("https://muslimsalat.com/Multan.json")
                  data3=response.json()
                  maghrib=data3['items'][0]['maghrib']
                  engine.say(f"Today maghrib time is: {maghrib}")
                  engine.runAndWait()
             elif "isha" in input_name:
                  response=requests.get("https://muslimsalat.com/Multan.json")
                  data3=response.json()
                  isha=data3['items'][0]['isha']
                  engine.say(f"Today isha time is: {isha}")
                  engine.runAndWait()
        elif "air condition" in input_name or "air pollution" in input_name or "smog" in input_name:
             response=requests.get("https://api.weatherapi.com/v1/current.json?key=82f72bc1d36745099e9145348240911&q=Multan&aqi=yes")
             data4=response.json()
             air_condition=data4['current']['air_quality']['gb-defra-index']
             if air_condition>=10:
                  engine.say("Sir, The air Condition is very Bad. You should not go out without proper safety!")
                  engine.runAndWait()
             else:
                  engine.say("Sir, The air condition is ok!")
                  engine.runAndWait()
        elif "dollar rate" in input_name or "dollar currency" in input_name:
             response=requests.get("https://v6.exchangerate-api.com/v6/59b70fdeb74aa85bdc583b64/latest/USD")
             currency=response.json()
             dollar_rate=currency["conversion_rates"]["PKR"]
             engine.say(f"Sir today dollar rate is {int(dollar_rate)}")
             engine.runAndWait()
        elif "top headlines" in input_name or "technology news" in input_name:
             response=requests.get("https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=828bea64b29a489f876a6da02cd1be82")
             data7=response.json()
             gene=random.randint(0,5)
             print(gene)
             news=data7['articles'][gene]
             title=news['title']
             author=news['author']
             engine.say("Showing tech news!!")
             engine.runAndWait()
             t.sleep(2)
             notification.notify(
                  title="Tech News!!",
                  message=f"{title}]\n{author}\n{datetime.datetime.now().date()}",
                  timeout=10
                  
             )
             t.sleep(6)
             engine.say("Would you like to read about it?")
             engine.runAndWait()
             audio = recognation.listen(listener)
             input_name = recognation.recognize_google(audio).lower()
             if "yes please" in  input_name or "ofcourse" in input_name:
                  url=news['url']
                  engine.say("Opening....")
                  engine.runAndWait()
                  t.sleep(1)
                  opennn=webbrowser.open(url)
             else:
                  pass
        elif "next" in input_name or "skip" in input_name:
            gui.hotkey('shift','n')
            t.sleep(1)
            engine.say("Done")
            engine.runAndWait()
        elif "caption" in input_name:
             gui.hotkey('c')
             t.sleep(1)
             engine.say("Done")
             engine.runAndWait()
        elif "good bye" in input_name:
            engine.say("Good bye,Sir")
            engine.runAndWait()
        elif "cricket match" in input_name or "live score" in input_name or "live cricket score" in input_name:
             service1=Service(ChromeDriverManager().install())
             driver1=webdriver.Chrome(service=service1)
             
             driver1.get("https://www.cricbuzz.com/cricket-match/live-scores")
             driver1.refresh()
             score = WebDriverWait(driver1, 90).until(
                  EC.presence_of_all_elements_located((By.CLASS_NAME, "cb-ovr-flo"))
    )
             result = WebDriverWait(driver1, 90).until(
                  EC.presence_of_all_elements_located((By.CLASS_NAME, "cb-text-complete"))
    ) 
             title_element = WebDriverWait(driver1, 90).until(
                  EC.presence_of_element_located((By.CLASS_NAME, "text-hvr-underline"))
    )
             match_no = WebDriverWait(driver1, 90).until(
                  EC.presence_of_all_elements_located((By.CLASS_NAME, "text-gray"))
    )   
             result=WebDriverWait(driver1,90).until(
                  EC.presence_of_all_elements_located((By.CLASS_NAME,"cb-text-complete"))
        
    )
             title = title_element.get_attribute('title')
             match_list = match_no[0].text
             ground = match_no[2].text
             result=result[0].text
             team_1 = score[7].text
             team_1_score = score[8].text
             team_2 = score[9].text
             team_2_score = score[10].text
             notification.notify(
                    title=f"{title} {match_list}",
                    message=f"{team_1} {team_1_score}\n{team_2} {team_2_score}",
                    timeout=10,
                    app_name="CLS"
        )
             t.sleep(5)
             if team_1=="PAk" or team_2 =="PAK" or team_1=="PAKISTAN" or team_2=="PAKISTAN":
                  engine.say("Sir,Its pakistan match would you like to watch it live")
                  engine.runAndWait()
                  audio = recognation.listen(listener)
                  input_name = recognation.recognize_google(audio).lower()
                  if "yes please" in input_name or "ofcourse" in input_name:
                       driver1.get("https://tamashaweb.com/")
                       li_element = WebDriverWait(driver, 90).until(
                           EC.presence_of_all_elements_located((By.CLASS_NAME, "uk-active"))
    )

                       a_tag = li_element[2].find_element(By.TAG_NAME, "a")
                       href_value = a_tag.get_attribute("href")
                       webbrowser.open(href_value)
                  else:
                       pass 
                       
        elif any(cmd in input_name for cmd in command):
            numbers = re.findall(r'\d+', input_name)
            numbers = list(map(int, numbers))
            if "add" in input_name or "addition" in input_name or "sum" in input_name:
                add = numbers[0] + numbers[1]
                engine.say(f"Here is your answer {add}")
                engine.runAndWait()
            elif "subtract" in input_name or "difference" in input_name:
                subtract = numbers[0] - numbers[1]
                engine.say(f"Here is your answer {subtract}")
                engine.runAndWait()
            elif "multiply" in input_name or "product" in input_name or "zarb" in input_name:
                multiply = numbers[0] * numbers[1]
                engine.say(f"Here is your answer {multiply}")
                engine.runAndWait()
            elif "division" in input_name or "divide" in input_name:
                if numbers[1] == 0:
                    engine.say("Sorry division not possible")
                    engine.runAndWait()
                else:
                    division = numbers[0] / numbers[1]
                    engine.say(f"Here is your division {int(division)}")
                    engine.runAndWait()
            elif "square root" in input_name:
                sqrt=math.sqrt(numbers[0])
                engine.say(f"Here is your answer {int(sqrt)}")
                engine.runAndWait()
            elif "%" in input_name:
                percentage=(numbers[1]/100)*numbers[0]
                engine.say(f"Here is your percentage answer {percentage}")
                engine.runAndWait() 
            elif "factorial" in input_name:
                 factorial=math.factorial(numbers[0])
                 engine.say(f"The factorial of {numbers[0]} is {factorial}")
                 engine.runAndWait()
        elif "turn on" in input_name or "turn off" in input_name or "on" in input_name or "off" in input_name:
             if "on" in input_name: 
                  url="https://sgp1.blynk.cloud/external/api/update?token=rWrw3M-TKFWyLy_uEnFDV7IdxZ5LUFzc&v1=1"
                  response=requests.get(url)
                  t.sleep(1)
                  engine.say("Turn on the bulb")
                  engine.runAndWait()
                  subject = "Bulb State"
                  body = "Bulb has been turn on"
                  message = f"Subject: {subject}\n\n{body}"
                  server.sendmail(sender_email, receiver_email, message)
                  
             elif "off" in input_name:
                  url="https://sgp1.blynk.cloud/external/api/update?token=rWrw3M-TKFWyLy_uEnFDV7IdxZ5LUFzc&v1=0"
                  response=requests.get(url)
                  t.sleep(1)
                  engine.say("Turn off the bulb")
                  engine.runAndWait()
                  subject = "Bulb State"
                  body = "Bulb has been turn off"
                  message = f"Subject: {subject}\n\n{body}"
                  server.sendmail(sender_email, receiver_email, message)
                  
                  
        # elif "wake up" in input_name or "time to to" in input_name:
        #      engine.say("I am always here for you,Sir")
        #      engine.runAndWait()
        elif "open notepad" in input_name or "notepad" in input_name:
            open=os.system('notepad')
            t.sleep(2)
            engine.say("Done")
            engine.runAndWait()
        elif "wallpaper" in input_name or "change wallpaper" in input_name:
             api_url = 'https://api.unsplash.com/photos/random'
             params = {
                       'client_id': '4WzCmfzRL5O6C2_di6YMo49AibIGIr410PWjOpl2Axw',  
                       'query': 'nature',  
                       'w': 1920,  
                       'h': 1080   
}
             response = requests.get(api_url, params=params)
             if response.status_code==200:
              data = response.json()
              image_url = data['urls']['full']
              img_response = requests.get(image_url)
              img = Image.open(BytesIO(img_response.content))
              temp_file_path = os.path.join(os.environ["TEMP"], "temp_wallpaper.jpg")
              img.save(temp_file_path, format="JPEG")
              result = windll.user32.SystemParametersInfoW(20, 0, temp_file_path, 3)
              if result == 0:
                  engine.say("Sorry Sir")
                  engine.runAndWait()
              else:
                  engine.say("Done Sir")
                  engine.runAndWait()

             else:
                  engine.say("Sorry Sir")
                  engine.runAndWait()
        elif "your name" in input_name or "who are you" in input_name:
             engine.say("My name is Jarvis. Hamza is my Creater")
             engine.runAndWait()
        elif "calories" in input_name:
             url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
             headers = {
             "x-app-id": "a55d34c2", 
             "x-app-key": "2318f968ff21ab1db77ec9088cb85218",  
             "Content-Type": "application/json"
}
             t.sleep(2)
             engine.say("Sure, Sir would you like to share your meal")
             engine.runAndWait()
             audio = recognation.listen(listener)
             input_name = recognation.recognize_google(audio).lower()
             data = {
    "query": input_name
}
             response = requests.post(url, json=data, headers=headers)
             calories1=0
             if response.status_code == 200:
                response_data = response.json()
                for food_data in response_data['foods']:
                  food_name = food_data['food_name']
                  serving_qty = food_data['serving_qty']
                  serving_unit = food_data['serving_unit']
                  calories = food_data['nf_calories']
                  calories1+=calories
                  calories1=int(calories1)
                  if calories1>= 2600 and calories<=3000:
                    engine.say("You already complete your calories, Sir")
                    engine.runAndWait()
                engine.say(f"Here is your caloried for given meal {calories1}")
                engine.runAndWait()

        print(input_name) 

else:
     engine.say("Sorry")
     engine.runAndWait()
     t.sleep(2)
     engine.say("Shutting down the system for safety")
     engine.runAndWait()
     exit()
     
          
while True:
    try:       
             my_jarvis()
    except:
        continue
