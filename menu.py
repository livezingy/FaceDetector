# -*- coding:utf-8 -*-
mainList = ['choose detect source', 'choose face detector', 'choose age and gender detector','RUN', 'exit']
sourceList = ['images', 'videos', 'camera', 'back to main menu']
faceList = ['HAAR', 'Tensornet', 'back to main menu']
ageList = ['ssrnet', 'Caffenet', 'back to main menu']

def print_mainmenu():
    print ("="*20 + "Main menu" + "="*20)
    for i in mainList:
        print (mainList.index(i) + 1, i)
    print(" ")
    
def print_sourcemenu():
    print ("="*20 + "Source menu" + "="*20)
    
    for i in sourceList:
        print (sourceList.index(i) + 1, i)
    print(" ")
    
def print_facedetectoremenu():
    print ("="*20 + "face detector menu" + "="*20)
    for i in faceList:
        print (faceList.index(i) + 1, i)
    print(" ")
    
def print_agegendermenu():
    print ("="*20 + "age gender detector menu" + "="*20)
    for i in ageList:
        print (ageList.index(i) + 1, i)
    print(" ")
    
def menu():
    #set default value for source/faceDetector/agDetector
    source = sourceList[1]
    faceDetector = faceList[1]
    agDetector = ageList[0]
    bRuning = False
    
    print_mainmenu()
    
    while True:
        #get user input
        try:
            num = int(input("Please choose the step："))
        except IndexError:
            print("Please input a valid value：（1.2.3.4.5）")
            continue
        #process the function according the user input
        if num == 1:
            print_sourcemenu()
            
            while True:
                #get user input
                try:
                    srcnum = int(input("Please choose the source："))
                except IndexError:
                    print("Please input a valid value：（1.2.3.4）")
                    continue
                    
                if srcnum == 1 or srcnum == 2 or srcnum == 3:
                    source = sourceList[srcnum - 1]
                    print("The detect source come from " + source)
                    print(" ")
                    print_mainmenu()
                    break
                elif srcnum == 4:
                    print_mainmenu()
                    break
                else:
                    print("input invalid！")
                    
        elif num == 2:
            print_facedetectoremenu()
            
            while True:
                #get user input
                try:
                    facenum = int(input("Please choose the face detector："))
                except IndexError:
                    print("Please input a valid value：（1.2.3）")
                    continue
                
                if facenum == 1 or facenum == 2:
                    faceDetector = faceList[facenum - 1]
                    print("The face detector is " + faceDetector)
                    print(" ")
                    print_mainmenu()
                    break
                elif facenum == 3:
                    print_mainmenu()
                    break
                else:
                    print("input invalid！")
                    
        elif num == 3:
            print_agegendermenu()
            while True:
                #get user input
                try:
                    agenum = int(input("Please choose age gender detector："))
                except IndexError:
                    print("Please input a valid value：（1.2.3）")
                    continue
                    
                if agenum == 1 or agenum == 2:
                    agDetector = ageList[agenum - 1]
                    print("The age gender detector is " + agDetector)
                    print(" ")
                    print_mainmenu()
                    break
                elif agenum == 3:
                    print_mainmenu()
                    break
                else:
                    print("input invalid！")
                    
        elif num == 4:
            print("The detect source come from " + source)
            print("The face detector is " + faceDetector)
            print("The age gender detector is " + agDetector)
            bRuning = True
            break
            
            
        elif num == 5:
            break
        else:
            print("input invalid！")
            
    return(source, faceDetector,agDetector,bRuning)