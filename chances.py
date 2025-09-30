import random as rd
import time as t
funnys = 0
superfunnys = 0
megafunnys = 0
a = 1
b = 0
blacklist = []
choicelist = [
    1,2,3,4,5,6,7,8,9,10,
    11,12,13,14,15,16,17,
    18,19,20,21,22,23,24,
    25,26,27,28,29,30,31,
    32,33,34,35,36,37,38,
    39,40,41,42,43,44,45,
    46,47,48,49,50,51,52,
    53,54,55,56,57,58,59,
    60,61,62,63,64,65,66,
    67,68,69,70,71,72,73,
    74,75,76,77,78,79,80,
    81,82,83,84,85,86,87,
    ]
filler = ""
filler2 = ""
wrong = True
wrong2 = True
wrong3 = True
easy = False
random = False
asdf = False

while wrong:
    choice = input(
    "choose your odds (1/__ chance)\n"
    "##############################\n"
    "(very easy)\n" \
    "        vvv         \n" \
    "1: 1\n"
    "2: 10\n"
    "3: 100\n"
    "4: 1 thousand\n"
    "5: 10 thousand\n"
    "6: 100 thousand\n"
    "7: 1 million\n" \
    "(reasonable)\n" \
    "      vvv      \n" \
    "8: 10 million\n" \
    "9: 100 million\n" \
    "10: 1 billion\n" \
    "11: 10 billion\n"
    "(these will never happen)\n" \
    "       vvv         \n" \
    "12: 100 billion\n" \
    "13: 1 trillion\n" \
    "14: 10 trillion\n"
    "15: 100 trillion\n"
    "16: 1 quadrillion\n"
    "17: 10 quadrillion\n" \
    "18: 100 quadrillion\n" \
    "19: 1 quintillion\n"
    "20: 10 quintillion\n"
    "21: 100 quintillion\n"
    "22: 1 sextillion\n"
    "23: 10 sextillion\n" \
    "24: 100 sextillion\n" \
    "25: 1 septillion\n"
    "26: 10 septillion\n"
    "27: 100 septillion\n"
    "28: 1 octillion\n" \
    "29: 10 octillion\n" \
    "30: 100 octillion\n"
    "31: 1 nonillion\n"
    "32: 10 nonillion\n"
    "33: 100 nonillion\n" \
    "34: 1 decillion\n" \
    "35: 10 decillion\n"
    "36: 100 decillion\n"
    "37: 1 undecillion\n"
    "38: 10 undecillion\n"
    "39: 100 undecillion\n" \
    "40: 1 duodecillion\n" \
    "41: 10 duodecillion\n"
    "42: 100 duodecillion\n"
    "43: 1 tredecillion\n" \
    "44: 10 tredecillion\n" \
    "45: 100 tredecillion\n"
    "46: 1 quattuordecillion\n"
    "47: 10 quattuordecillion\n"
    "48: 100 quattuordecillion\n" \
    "49: 1 quindecillion\n" \
    "50: 10 quindecillion\n"
    "51: 100 quindecillion\n"
    "52: 1 sexdecillion\n"
    "53: 10 sexdecillion\n"
    "54: 100 sexdecillion\n" \
    "55: 1 septendecillion\n" \
    "56: 10 septendecillion\n"
    "57: 100 septendecillion\n"
    "58: 1 octodecillion\n"
    "59: 10 octodecillion\n" \
    "60: 100 octodecillion\n" \
    "61: 1 novemdecillion\n"
    "62: 10 novemdecillion\n"
    "63: 100 novemdecillion\n"
    "64: 1 vigintillion\n" \
    "65: 10 vigintillion\n" \
    "66: 100 vigintillion\n"
    "67: 1 tretrigintillion\n"
    "68: 10 tretrigintillion\n"
    "69: 100 tretrigintillion\n"
    "70: 1 quattuorvigintillion\n" \
    "71: 10 quattuorvigintillion\n" \
    "72: 100 quattuorvigintillion\n"
    "73: 1 quinquaquattuorvigintillion\n"
    "74: 10 quinquaquattuorvigintillion\n" \
    "75: 100 quinquaquattuorvigintillion\n"
    "76: 1 sexquattuorvigintillion\n"
    "77: 10 sexquattuorvigintillion\n" \
    "78: 100 sexquattuorvigintillion\n" \
    "79: 1 septenquattuorvigintillion\n"
    "80: 10 septenquattuorvigintillion\n"
    "81: 100 septenquattuorvigintillion\n"
    "82: 1 octoquattuorvigintillion\n"
    "83: 10 octoquattuorvigintillion\n" \
    "84: 100 octoquattuorvigintillion\n" \
    "85: 1 novemquattuorvigintillion\n"
    "86: 10 novemquattuorvigintillion\n"
    "87: 100 novemquattuorvigintillion\n" \
    "> ")
    try:
        
            print("\nit doesnt go that low\n")
        choice = int(choice)
    except:
        print("not a number")
        wrong = True
    if type(choice) == int:
        if choice not in choicelist and choice > 87:
            print("\nit doesnt go that high\n")
        elif choice not in choicelist and choice < 1:
            print("\nit doesnt go that low\n")
        elif choice not in choicelist:
            print("\ninvalid\n")
        else:
            wrong = False
            while wrong2:
                fart = input("would you like to make the odds decrease with each generation (y/n)\n> ").lower()
                if fart == "y":
                    easy = True
                    wrong2 = False
                elif fart == "n":
                    easy = False
                    wrong2 = False
                    while wrong3:
                        fart = input("would you like to make the pickrange random for funny (y/n)\n> ").lower()
                        if fart == "y":
                            random = True
                            wrong3 = False
                        elif fart == "n":
                            random = False
                            wrong3 = False
                        else:
                            print("type y or n")
                else:
                    print("type y or n")

number = ""
for i in range(choice):
    number += "9"
numver = int(number)
waits = [choice / 21, choice / 14, choice / 7]
pickrange = numver
while True:
    if easy == True and random == False:
        pickrange = numver - len(blacklist)
    elif easy == False and random == False:
        pickrange = numver
    elif random == True:
        pickrange = rd.randint(0,numver)
    thing = rd.randint(0,pickrange)
    zeroes = len(str(numver)) - len(str(thing))
    blacklist.append(thing)
    for i in range(zeroes):
        filler += "0"
    zeroes2 = len(str(numver)) - len(str(pickrange))
    for i in range(zeroes2):
        filler2 += "0"
    message = f"|| {filler}{thing} || {funnys} | {superfunnys} | {megafunnys} | #{a} ||     !|#|!"
    funnymessage = f"|| {filler}{thing} || {funnys} | {superfunnys} | {megafunnys} | #{a} ||     !|+|!"
    superfunnymessage = f"|| {filler}{thing} || {funnys} | {superfunnys} | {megafunnys} | #{a} ||     ;;#;;"
    megafunnymessage = f"|| {filler}{thing} || {funnys} | {superfunnys} | {megafunnys} | #{a} ||      <~^ "
    winmessage = f"|| {filler}{thing} || {funnys} | {superfunnys} | {megafunnys} | #{a} ||       *  "
    message143 = f"|| {thing} || {thing} | {thing} | {thing} | #{thing} ||      {thing}"
    messages = [message,funnymessage,superfunnymessage,megafunnymessage,winmessage]
    if easy == True:
        for i in range(len(messages)):
            messages[i] += f"     {pickrange} left"
    elif random == True:
        for i in range(len(messages)):
            messages[i] += f"     1/{filler2}{pickrange + 1}"
    a += 1
    if thing > 1000 and thing != 1225:
        print(messages[0])
    if thing == 1225:
        print(message143)
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        break
    if thing < 100 and thing > 35:
        funnys += 1
        print(messages[1])
        t.sleep(waits[0])
    if thing <= 35 and thing >= 10:
        superfunnys += 1
        print(messages[2])
        t.sleep(waits[1])
    if thing < 10 and thing >= 1:
        megafunnys += 1
        print(messages[3])
        t.sleep(waits[2])
    if thing == 0:
        print(messages[4])
        if pickrange == 0:
            print("\n\nwow\n\n")
            break
        print("")
        pickrange = numver
        blacklist = []
        a = 1
    filler = ""
    filler2 = ""
