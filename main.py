import pywhatkit as whatsapp
import json
from datetime import datetime
import subprocess 
import time

def without_website(phone,index):
    without_website_msg = '''Hi there, 

I noticed you don’t have a website for your shop and I can build a modern beautiful website for your place. I’m a student and I’m building my portfolio I charge 50$ for the website and If you didn’t like the final result you don’t pay anything. A website can shift your online presence 180 degrees most sales now are online.

The website is of four sections. The first is an introduction about the place, name, and exact location. The second is products your sell, their pictures, titles, and price. The third is a contact us page with a button and animation that when clicked will open the phone app and insert your phone number and the final section is reviews that I will pull online with their pictures

Thank you in advance, message me back if you like the proposal and we can discuss how you want it to look'''
    whatsapp.sendwhatmsg(phone, without_website_msg, datetime.now().hour, datetime.now().minute + 2)
    print(f"sent a message @ {index}")
    time.sleep(25)
    subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
    
def with_website(phone,index):
    with_website_msg = '''Hi there,

 I found your Shop on google maps and I checked your website and I think I can rebuild your website to be so much better and modern and change your customers experience. I’m a student and I’m building my portfolio and I will make your website for 50$ and if you didn’t like what you see you pay nothing. 

Thanks in advance, message me and we can discuss if you want it to look a specific way or if you have something in mind already.'''
    whatsapp.sendwhatmsg(phone, with_website_msg, datetime.now().hour, datetime.now().minute + 2)
    print(f"sent a message @ {index}")
    time.sleep(25)
    subprocess.call("TASKKILL /f  /IM  CHROME.EXE")
    
def dumpDataJson(data,index):
    print(f"data before {len(json.load(open('data.json','r')))}")
    json.dump(data[index:],open("data.json","w"))
    print(f"data after {len(json.load(open('data.json','r')))}")

data = json.load(open('data.json', 'r'))



for i in range(len(data)):
    if data[i]["phone"] != "":
        try:
            if data[i]["website"] == "":
                without_website(data[i]["phone"],i)
            else:
                with_website(data[i]["phone"],i)
        except Exception as e:
            print(f"Exception occured @ {i}")
    dumpDataJson(data,i)
