import os
import subprocess

#
# This is DE KOMMER! HÆLP OS! Esoteric Language or (G&BLang, GNBLang)
#
# This esolang is inspired by Guts & Blackpowder Callout and it was made for a joke
# This is probably be the first Guts & Blackpowder Esoteric Language or not
# 07/17/26 or 17/07/26 depends on region as important history
# How to program, you have to use DE KOMMER! HÆLP OS! by counting on how many word up 1 to 9
# e.g. "DE" is 1, "DE KOMMER! HÆLP OS!" is 4, "DE KOMMER! HÆLP OS! DE KOMMER! HÆLP" is 7.
# Line represent the digit so 3 line is 3 digit
# DE KOMMER! HÆLP OS! DE KOMMER! HÆLP OS! DE KOMMER! is Zero not to be confuse
# DE KOMMER! HÆLP OS! DE KOMMER! HÆLP OS! DE KOMMER! HÆLP OS! can inserted as ASCII decimal
# The interpreter converts "DE KOMMER! HÆLP OS!" into a string from ASCII then converts to python source code
# To program, you mush write lines of code for digits and create new ASCII Character inorder to make program
#
# Note: If somebody make a better version of DE KOMMER! HÆLP OS! for making more
# interesting concept than that I would like to credit the people who did a good job of making
# interesting instruction rather than just basic language.
#

# Also Note: Sorry for my grammar and comprehention of my comments.

# Ignore These
# BEREITEN DIE VERTEIDIGUNG VOR!
# KÜRASSIER!
# KANNIBALE!
# DE KOMMER! HÆLP OS!
# Scum!, scum of the earth, really here after all the true gentlemen deserted their post?
# Hello!
# I think I’ve got the attention of that ship over there.
# I can lower this platform and get us down there.
# Get on the platform!
# The King's Colours. Save them, would you?
# Carry on and save yourselves.
# Goodnight, sir.
# Shambler
# Runner
# Bomber
# Igniter
# Sapper
# Cuirassier
# WE NEED A BARRICADE!
# TAKE COVER!
# ADVANCE!
# FORWARD MARCH!
# DON'T GIVE UP THE SHIP!

# This is a basic esoteric language were 4 instruction "DE KOMMER! HÆLP OS!".

order2 = "" # String of characters
intorder = 0 # Backup Ascii
intorder2 = 0 # Ascii
wait = 0 # How many
warn = 0 # More than 3 would result in error
exponential = 100 # Start with hundred then reduce to 90 percent due to digit

# Making Error Cause Unexpected or Incorrect Syntax once the program was converted

# Error management
def convert(x):
    if not isinstance(x, int):
        raise TypeError("!SO PLÆH !REMMOK ED")
    if not 0 <= x <= 127:
        raise TypeError("!!SO PLÆH !REMMOK ED")
    return chr(x)


def order(out):
    global order2
    global intorder
    global intorder2
    global wait
    global warn
    global exponential
    line = out.strip().split()
    part = 0 # 4 Per DE KOMMER! HÆLP OS!
    wait = 0
    

    if not line:
        return
    
    if warn <= 3:
        warn += 1
    else:
        warn = 0
        print("DE KOMMER! HÆLP OS!")
        return
    
    for i in range(len(line)):
        if wait <= 9:
            if line[i] == "DE" and part == 0:
                intorder += 1
                wait += 1
                part += 1
            elif line[i] == "KOMMER!" and part == 1:
                intorder += 1
                wait += 1
                part += 1
                if intorder >= 10:
                    intorder = 0
            elif line[i] == "HÃ†LP" and part == 2:
                intorder += 1
                wait += 1
                part += 1
            elif line[i] == "OS!" and part == 3:
                intorder += 1
                wait += 1
                part = 0
            else:
                break
        elif wait == 10:
            if line[i] == "HÃ†LP":
                wait += 1
        elif wait == 11:
            if line[i] == "OS!":
                order2 += convert(intorder2)
                wait = 0
                warn = 0
                intorder2 = 0
                exponential = 100
                return
        else:
            print("DE KOMMER! HÆLP OS!")
            break
    wait = 0
    intorder2 += exponential * intorder
    intorder = 0
    exponential //= 10
    return


def main():
    folder1 = os.getcwd()
    folder2 = os.path.join(folder1)
    input1 = "Input.txt"
    input2 = os.path.join(folder2, input1)
    output1 = "Outputbackup.py"
    output2 = os.path.join(folder2, output1)
    with open(input2, "r") as x:
        for i in x:
            order(i)
    
    
    try:
        # It Convert many "DE KOMMER! HÆLP OS!" into python code
        fix_it = order2.replace("\\n", "\n") # It gives you more new lines of code
        with open(output2, "w", encoding="utf-8") as x:
            x.write(fix_it)
        runner = subprocess.run(["python3", output2], check=True, text=True, capture_output=True)
        print(runner.stdout)
    except OSError:
        print("DE KOMMER! HÆLP OS!!")
    except subprocess.CalledProcessError:
        print("DE KOMMER! HÆLP OS!!")
    except Exception:
        print("DE KOMMER! HÆLP OS!!!")

main()