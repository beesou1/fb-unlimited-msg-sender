import time 
import fbchat
from getpass import getpass
import pyautogui
from fbchat import Client

username = input("email or phone number: ")
client = fbchat.Client(username,getpass())

no_of_friend = int(input("Number of friend: "))
for word in range(no_of_friend):
    name = str(input("Name: "))
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg = input("Write your message: ")
    while True:
        time.sleep(1)
        sent = client.send(fbchat.models.Message(msg),friend.uid)
        time.sleep(0.4)
        pyautogui.press("enter")


        