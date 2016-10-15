# This program is my first Python program created not using tutorials...
# (jk, i had to lookup arrays because the way i was doing it before was retarded)
# let me know how I do, anything I can optimize.
# techiejohnathan@gmail.com

import random

# |Defining each character as number to make it easier(harder?). Most
# likely is a better way to do this?|
# ignore 2 lines up ^ found out about arrays.
# Main purpose of this program is to practice python, and make a semi
# working program.
# it works! I feel like I did it in a really retarded way though.

arraylowercase = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def mainui():
    try:
        print('Random Password Generator!')
        print('Please select the options you wish too generate the password under.')
        print('  1. lowercase')
        print('  2. lowercase/uppercase')
        print('  3. alphanumeric')
        print('  4. alphanumeric special characters')
        selection = input()
        varselection = int(selection)
        if varselection == 1:
            lowercase()
        elif varselection == 2:
            lowerupper()
        elif varselection == 3:
            alphanumeric()
        elif varselection == 4:
            alphanumericspecial()
        elif varselection > 4:
            print(' ')
            print('Please enter valid number...')
            print(' ')
            mainui()
    except ValueError:
        print(' ')
        print('Enter numbers, you know those numbered thingies.')
        print(' ')
        mainui()





def lowercase():

    print('Please enter how many characters you want the password to be')
    charlen = input()
    
    global intcharlen
    intcharlen = int(charlen)
    
    if intcharlen <= 20:
        print('Sending too super duper computer for computing...')
        print('Done!')
        
        def gen():
                char1 = random.randint(1, 26)
                char2 = random.randint(1, 26)
                char3 = random.randint(1, 26)
                char4 = random.randint(1, 26)
                char5 = random.randint(1, 26)
                char6 = random.randint(1, 26)
                char7 = random.randint(1, 26)
                char8 = random.randint(1, 26)
                char9 = random.randint(1, 26)
                char10 = random.randint(1, 26)
                char11 = random.randint(1, 26)
                char12 = random.randint(1, 26)
                char13 = random.randint(1, 26)
                char14 = random.randint(1, 26)
                char15 = random.randint(1, 26)
                char16 = random.randint(1, 26)
                char17 = random.randint(1, 26)
                char18 = random.randint(1, 26)
                char19 = random.randint(1, 26)
                char20 = random.randint(1, 26)
                if intcharlen == 1:
                    print(arraylowercase[char1],sep="")
                    
                elif intcharlen == 2:
                    print(arraylowercase[char1], arraylowercase[char2],sep="")
                    
                elif intcharlen == 3:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3],sep="")
                    
                elif intcharlen == 4:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4],sep="")
                    
                elif intcharlen == 5:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5],sep="")
                    
                elif intcharlen == 6:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],sep="")
                    
                elif intcharlen == 7:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7],sep="")
                    
                elif intcharlen == 8:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8],sep="")

                elif intcharlen == 9:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9],sep="")

                elif intcharlen == 10:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10],sep="")

                elif intcharlen == 11:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11],sep="")

                elif intcharlen == 12:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],sep="")

                elif intcharlen == 13:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13],sep="")

                elif intcharlen == 14:
                    rint(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14],sep="")

                elif intcharlen == 15:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15],sep="")

                elif intcharlen == 16:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15], arraylowercase[char16],sep="")

                elif intcharlen == 17:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15], arraylowercase[char16], arraylowercase[char17],sep="")

                elif intcharlen == 18:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15], arraylowercase[char16], arraylowercase[char17], arraylowercase[char18],sep="")

                elif intcharlen == 19:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15], arraylowercase[char16], arraylowercase[char17], arraylowercase[char18],
                      arraylowercase[char19],sep="")

                elif intcharlen == 20:
                    print(arraylowercase[char1], arraylowercase[char2], arraylowercase[char3], arraylowercase[char4], arraylowercase[char5], arraylowercase[char6],
                      arraylowercase[char7], arraylowercase[char8], arraylowercase[char9], arraylowercase[char10], arraylowercase[char11], arraylowercase[char12],
                      arraylowercase[char13], arraylowercase[char14], arraylowercase[char15], arraylowercase[char16], arraylowercase[char17], arraylowercase[char18],
                      arraylowercase[char19], arraylowercase[char20],sep="")
            
                
        gen()
            
        
    

    

def lowerupper():
    print('worked2')

def alphanumeric():
    print('worked3')

def alphanumericspecial():
    print('worked4')




mainui()
