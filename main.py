import os #to make ping commands in the terminal
import time #to add a sleep time between pings
import jokes #the array of jokes to randomize from
import random #to randomize jokes and stuff
from notifypy import Notify #to notify the user when the internet connects or disconnects


hostname = "8.8.8.8" #the DNS to ping


#setting up the Notify library instance
notification = Notify()
notification.icon = "assets/images/WifiWho.png" #the icon for the notification
notification.audio = "assets/audio/confirmation-tone.wav" #the sound being played during the notification

def randomJoke(): return jokes.quotes_and_jokes[random.randint(0, len(jokes.quotes_and_jokes)-1)]
def sendNotification(title):
    notification.title = "Internet is " + title #depending on the state, the internet is...? hopefully connected.
    notification.message = randomJoke() #calls in the the randomJoke method to find a joke
    notification.send() #send the notification to the system 

isConnected = False #to alternate... [testing for bugs]
#response = 1 no internet
#response = 0 internet access
def pingServer():
    global isConnected #defining a global varaible called isConnected
    response = os.system("ping "+hostname+" -n 1 ")
    #and then check the response...
    if response == 0 and isConnected == False: #ping and send notification
        sendNotification("back! ✅")
        isConnected = True
        time.sleep(1.5)
        pingServer()
    elif response == 0 and isConnected == True: #don't send any notification, but keep pinging
        time.sleep(5)
        pingServer()
    if response == 1 and isConnected == True:
        sendNotification("is down! ❌")
        isConnected = False
        time.sleep(1.5)
        pingServer()
    elif response == 1 and isConnected == False:
        time.sleep(5)
        pingServer()
