import random 
import os
prefix = "0x00"
for x in range (9):                                 #--> range above 2900 is deadly 
    
    try:
        os.mkdir("folderbomb")
        os.chdir("folderbomb")
    except:
        try:
            os.chdir("folderbomb")                  #--> tries to bomb existing folder by name folderbomb
            foldername = random.randrange(0,99999)  #--> set range high to avoid conflicting folder names
            foldername = prefix+str(foldername)
        except:
            foldername = random.randrange(0,99999)  #--> set range high to avoid conflicting folder names
            foldername = prefix+str(foldername)
        try:
            os.mkdir(foldername)                    #--> folder will not be created if it already exists 
        except:
            print(foldername)                       #--> prints name of the created folder

print("\n\nBOOM\n")