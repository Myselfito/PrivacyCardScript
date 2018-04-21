import requests
import json
import time
from newtext import *
from config import *

def pauseCard():
    cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
    r = requests.session()
    card_id = raw_input("Card ID: ")
    r = requests.post("https://privacy.com/api/v1/card/"+card_id+"/pause", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
    rs = r.status_code
    print rs
    if rs == 200:
        print "Card was paused successfully!"
def pauseAll():
    for cardid in card_ids:
        cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
        r = requests.session()
        r = requests.post("https://privacy.com/api/v1/card/"+cardid+"/pause", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
        rs = r.status_code
        if rs == 200:
            print "Card " + cardid + " was paused successfully!"
        time.sleep(3)
    print "All cards paused successfully!"
def resumeAll():
    for cardid in card_ids:
        cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
        r = requests.session()
        r = requests.post("https://privacy.com/api/v1/card/"+cardid+"/resume", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
        rs = r.status_code
        if rs == 200:
            print "Card " + cardid + " was resumed successfully!"
        time.sleep(2)
    print "All cards resumed successfully!"
def resumeCard():
    cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
    r = requests.session()
    card_id = raw_input("Card ID: ")
    r = requests.post("https://privacy.com/api/v1/card/"+card_id+"/resume", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
    rs = r.status_code
    if rs == 200:
        print "Card resumed successfully!"
def closeCards():
    rl = da["cardList"]
    toclose = raw_input("Enter card nicknames to close(use \',\' to separate, matching nickname case and no spaces): ")
    toclose = toclose.split(",")
    for card in rl:
        for c in toclose:
            if c in card["memo"]:
                cid = card["cardID"]
                print "Found card " + cid + ", closing card now."
                cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
                r = requests.session()
                r = requests.post("https://privacy.com/api/v1/card/"+cid+"/close", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
                rs = r.status_code
                if rs == 200:
                    print "Card ",card," closed successfully!"
                time.sleep(3)
            else:
                pass
    print "Selected cards closed successfully!"
def closeUsed():
    rl = da["cardList"]
    count = 0
    for card in rl:
        if "false" in card["unused"] and "OPEN" in card["state"]:
            cid = card["cardID"]
            print "Found card " + cid + ", closing card now."
            cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
            r = requests.session()
            r = requests.post("https://privacy.com/api/v1/card/"+cid+"/close", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess)
            rs = r.status_code
            if rs == 200:
                print "Card ",card["PAN"][-4:]," closed successfully!"
            else:
                print "Error deleting card."
            count = count + 1
            time.sleep(3)
    print "Total of",count,"open and used cards were closed successfully on your Privacy account."
def createCard():
    ca = raw_input("Spend limit period (MONTHLY,ETC..): ")
    str(ca)
    cb = raw_input("Card nickname: ")
    str(cb)
    cc = raw_input("Spend limit amount: ")
    str(cc)
    payload={"reloadable":True,"spendLimitDuration":ca,"memo":cb,"meta":{"hostname":""},"style":"","spendLimit":cc}
    cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
    r = requests.session()
    r = requests.post("https://privacy.com/api/v1/card/", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess, json=payload)
    e = requests.get("https://privacy.com/api/v1/card/", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess, json=payload)
    rs = r.status_code
    es = e.status_code
    print "r status: ", rs
    print "e status: ", es
    if rs == 200:
        print "Card created successfully!"
    else:
        print "Error creating card! :("
def createCards():
        for i in range(0,MAXCARDS):
            payload={"reloadable":True,"spendLimitDuration":limit_duration,"memo":card_names[i],"meta":{"hostname":""},"style":"","spendLimit":spend_limit}
            cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
            r = requests.session()
            r = requests.post("https://privacy.com/api/v1/card/", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess, json=payload)
            e = requests.get("https://privacy.com/api/v1/card/", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess, json=payload)
            rs = r.status_code
            es = e.status_code
            print "r status: ", rs
            print "e status: ", es
            if rs == 200:
                print "Card ",card_names[i]," created successfully!"
            else:
                print "Error creating card! :("
                print "Status: ", r.text
            time.sleep(3)
        print "Done creating cards!"

def getCards():
    payload={"reloadable":True,"spendLimitDuration":"MONTHLY","memo":"123","meta":{"hostname":""},"style":"","spendLimit":"1"}
    cookiess = {"ETag":etag,"sessionID":sessionid, "token":ctoken}
    e = requests.get("https://privacy.com/api/v1/card/", headers={"Accept": "application/json, text/plain, */*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.9,es;q=0.8", "Authorization": "Bearer " + ctoken, "Connection": "keep-alive", "Content-Length": "0", "Cookie": "ETag=" + etag + "; sessionID="+ sessionid +"; " + ctoken, "Host": "privacy.com", "Origin": "https://privacy.com", "Referer": "https://privacy.com/cards", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}, cookies=cookiess, json=payload)
    e0 = e.status_code
    print "status: ", e0
    cardlisttxt = e.text
    c1 = open("scrap.txt","w")
    c1.write(cardlisttxt)
    c1.close()
    f1 = open("scrap.txt","r")
    a=f1.read()
    str1 = a.replace("true", "\"true\"")
    str1 = str1.replace("false", "\"false\"")
    f1.close()
    f2 = open("newtext.py","w")
    f2.write("da = "+str1)
    f2.close()

    cl = da["cardList"]
    f1 = open("privacy cards.txt","w")
    f2 = open("profile format.txt","w")

    q1 = raw_input("Excel copy paste output?(y/n): ")
    str(q1)

    if q1 is "n":
        for card in cl:
            if "OPEN" in card["state"]:
                print "Card name: ", card["memo"] , "Card number: ", card["PAN"], "CVV :",card["CVV"], "expMonth: ",card["expMonth"], "expYear: ",card["expYear"]
                f1.write("Card name: "+card["memo"]+ " Card number: "+ card["PAN"]+ " CVV :"+card["CVV"]+ " expMonth: "+card["expMonth"]+ " expYear: "+card["expYear"]+"\n")
        print
        print "All done, check your \"privacy cards txt\" file to view the output!"

    elif q1 is "y":
        for card in cl:
            if "OPEN" in card["state"]:
                print "Card name: ", card["memo"] , "Card number: ", card["PAN"], "CVV :",card["CVV"], "expMonth: ",card["expMonth"], "expYear: ",card["expYear"]
                f2.write(card["memo"]+"\t"+card["PAN"]+"\t"+card["expMonth"]+"\t"+card["expYear"]+"\t"+card["CVV"]+"\n")
        print
        print "All done, check your \"profile format txt\" file to view the output!"
    else:
        print "Invalid entry! Try again :)"


    global card_ids
    card_ids=[]
    for card in cl:
        if "OPEN" in card["state"]:
            card_ids.append(card["cardID"])
            print "Added card " + card["cardID"] + " to card list..."
        elif "PAUSED" in card["state"]:
            card_ids.append(card["cardID"])
            print "Added card " + card["cardID"] + " to card list..."
    print "Adding card ids done..."
    print "Card ID list: ", card_ids

    f1.close()
    f2.close()

def getAction():
    if action == "pause":
        pauseCard()
    elif action == "resume":
        resumeCard()
    elif action == "create":
        createCard()
    elif action == "create cards":
        createCards()
    elif action == "get cards":
        getCards()
    elif action == "pause all":
        pauseAll()
    elif action == "resume all":
        resumeAll()
    elif action == "close cards":
        closeCards()
    elif action == "close used":
        closeUsed()
    else:
        "Invalid entry"
        pass
def intro():
    print "Below are the commands that you may use within the script. Please type them with matching case."
    print "-----------------------------------------------------------------------------------------------"
    print "> pause (Pauses a specific card)"
    print "> resume (Resumes a specific card)"
    print "> create (Creates a new card)"
    print "> create cards (Creates multiple cards at once. Adjust configuration in config.py)"
    print "> get cards (ALWAYS RUN THIS FIRST! Gets all open state cards and puts them in a text file)"
    print "> pause all (pauses all open cards)"
    print "> resume all (resumes all open cards)"
    print "> close cards (Closes SELECT cards)"
    print "> close used (Closes ALL OPEN AND USED CARDS ONLY)"

print
print "IMPORTANT! TO HAVE SCRIPT WORK PROPERLY FIRST RUN THE \"get cards\" FUNCTION. YOU MAY RUN ANY FUNCTION AFTERWARDS!"
print
print "Get cards will first get all your card data and make text files required to call other functions like Create Card(s), Close Card(s), Pause Card, etc."
print

intro()

print

open("newtext.py","w")
open("newtext.py","w").close()

action = raw_input("What do you want to do?: ")
getAction()
new_action = raw_input("Would you like to do something else?(Y/N): ")
if new_action == "y":
    action = raw_input("What do you want to do?: ")
    getAction()
else:
    print "Ok!"
