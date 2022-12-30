from passlib.hash import bcrypt
from libsrary import pingo
import os
import sys

print ("\n")
print ("===============================   Welcome To Crazy-Root     ===============================")
print ("= ██████╗██████╗  █████╗ ███████╗██╗   ██╗     ██████╗  ██████╗██████╗ ██╗   ██╗██████╗ ████████╗=")
print ("=██╔════╝██╔══██╗██╔══██╗╚══███╔╝╚██╗ ██╔╝     ██╔══██╗██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝=")
print ("=██║     ██████╔╝███████║  ███╔╝  ╚████╔╝█████╗██████╔╝██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   =")
print ("=██║     ██╔══██╗██╔══██║ ███╔╝    ╚██╔╝ ╚════╝██╔══██╗██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   =")
print ("=╚██████╗██║  ██║██║  ██║███████╗   ██║        ██████╔╝╚██████╗██║  ██║   ██║   ██║        ██║   =")
print ("= ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝  ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   =")
print ("============================== https://github.com/Aminul0x01 ==============================")
print ("\n")

options = input('decode bcrypt get bro ? type (y) to continue decoding, key (ctrl+c) not continue decoding : ')

if (options != "y" and options != "n"):
    sys.exit('Invalid Option')

passwords = (options == "y")
text_file = open("wordlist.txt", "r")

words = text_file.read().splitlines()

hash = input('enter bcrypt hash : ')
length = len(words)

correct_word = ""
for (index, word) in enumerate(words):
    pingo(index, length, prefix='Wait for a while :', suffix='Complete')
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        print()
        break

print("Decode Bcrypt result :", correct_word)

