from PIL import Image
from colorama import init, Fore, Back, Style
init()
spaces = """

















































"""
input("Enter...")
print(""""                        

                                           *##X        
                                           *###*       
                                           ####X       
             *#                           ####X#       
             X#X                          #X##X#       
 X           *##                          ###X#X       
X#     *XX*  *##X                         X####        
##*  *######XX# #                         *##X         
### *#X     #X* #              **          ##          
#X###X      X  ##          ***####         ##*         
#X  XX      *###X        #####X  X#       *#X*         
 ##X#*       *  ##*     *#   X    X#      XXX*         
X#XX#* X*X  *##XX#X     X#         X#     #*#          
#####* #*#*  #X*X*      #X          #X   X# #          
 * *#*       ##*      *##       X#* *##*## XX          
   X#XXX***  #*########*      X####  ##** X#           
 *##*     ***#X X*   *X*      *##### *#XX##*           
 XX           #*       *X      #####**#XX*    ##       
 #X **        *#    *X          X### ##   *X*####      
 #X*##* X#X    #X X####          X#  *#X  ###X  ###    
 #X*### ###X   XX X####X  *XXXX       *#XX#      *#X   
 X# ##X X##X   XX  X####X #####         ##X *##X  #X   
 X#  *   X#    #X X#####X #####             #XX#* *#   
  ##*         *#  ######X #####*           *#  X####*  
   ###XX***XX##X  ######X *####*           *#    ***   
    *X######X**    #####*  ####            ##          
         #*         ####   *X*            ##           
         #*         *XX*         X*     *#X            
         #*                     X*X#XXXX#X             
         X#                    #*  **###               
         X#* *               *#     * X#               
         #X#XX*            *##     X##X#               
         #  X##       X   ####X*  ##**X                
        *#   X#*     X# X###X*##X ##                   
        #X  X##X    X####X #XX##X#**                   
       #X  X# *#   *#X     *##* ##                     
       #  *#* *#   #X                                  
      *#   #  #X  ##                                   
      X# X##  #*  X#                                   
     *# *#*   #*  X#                                   
   X##X #*    #X X#*                                   
   #X   #     #XX#*                                    
  X# *  XX   ## #*                                     
  ##X   #*  #X  #*                                     
  *##*X##  X#*  #X                     
   X###X   #X*  #*                                     
           #X  X#                                      
           X###X*                                      
             **
Ruminant Digestive system""")


def menu():
    image = Image.open('cow2.jpeg')
    image.show()
    choice()
    
def choice():
    v1 = input("Where do you want to go? (1 Mouth, 2 Oesophagus, 3 Rumen, 4 Roticulum, 5 Omasum, 6 Abomasum, 7 Small Intestine, 8 Caecum, 9 Large Intestine, 0 Rectum) ")

    if v1 == "1":
        Mouth()
    elif v1 == "2":
        Oesophagus()
    elif v1 == "3":
        Rumen()
    elif v1 == "4":
        Roticulum()
    elif v1 == "5":
        Omasum()
    elif v1 == "6":
        Abomasum()
    elif v1 == "7":
        Small_Intestine()
    elif v1 == "8":
        Cecum()
    elif v1 == "9":
        Large_Intestine()
    elif v1 == "0":
        Rectum()
    else:
      print("Please try again")
      choice()


def Mouth():
    print(spaces)
    print(Fore.RED + """
    
    ███╗░░░███╗░█████╗░██╗░░░██╗████████╗██╗░░██╗
    ████╗░████║██╔══██╗██║░░░██║╚══██╔══╝██║░░██║
    ██╔████╔██║██║░░██║██║░░░██║░░░██║░░░███████║
    ██║╚██╔╝██║██║░░██║██║░░░██║░░░██║░░░██╔══██║
    ██║░╚═╝░██║╚█████╔╝╚██████╔╝░░░██║░░░██║░░██║
    ╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝""" + Style.RESET_ALL)


    print("""
    - The mouth chews food
    - Enzymes and saliva dissolve and breakdown fats
    - Ruminants don't have have upper teeth, instead they have a hard palate""")
    imagemouth = Image.open('tounging-cow.jpg')
    imagemouth.show()
    go_back()


def Oesophagus():
  print(spaces)
  print(Fore.RED + """

    ███████╗░██████╗░█████╗░██████╗░██╗░░██╗░█████╗░░██████╗░██╗░░░██╗░██████╗
    ██╔════╝██╔════╝██╔══██╗██╔══██╗██║░░██║██╔══██╗██╔════╝░██║░░░██║██╔════╝
    █████╗░░╚█████╗░██║░░██║██████╔╝███████║███████║██║░░██╗░██║░░░██║╚█████╗░
    ██╔══╝░░░╚═══██╗██║░░██║██╔═══╝░██╔══██║██╔══██║██║░░╚██╗██║░░░██║░╚═══██╗
    ███████╗██████╔╝╚█████╔╝██║░░░░░██║░░██║██║░░██║╚██████╔╝╚██████╔╝██████╔╝
    ╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚═════╝░""" + Style.RESET_ALL)

  print("""
    - Unlike humans, ruminant esophagi are bidirectional, meaning they allow food to travel both ways
    - Ruminants, such as cows, often regurgitate their food to further chew it and break it down
    - In calves, the esophagus directs milk to skip the rumen and travel straight to the abomasum""")
  imageesophagus = Image.open('esophagus.jpg')
  imageesophagus.show()
  go_back()

def Rumen():
  styling("""
██████╗░██╗░░░██╗███╗░░░███╗███████╗███╗░░██╗
██╔══██╗██║░░░██║████╗░████║██╔════╝████╗░██║
██████╔╝██║░░░██║██╔████╔██║█████╗░░██╔██╗██║
██╔══██╗██║░░░██║██║╚██╔╝██║██╔══╝░░██║╚████║
██║░░██║╚██████╔╝██║░╚═╝░██║███████╗██║░╚███║
╚═╝░░╚═╝░╚═════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝""", """
- The largest stomach compartment
- Used as a storage for food
- Contains microbes that ferment and digest food
- Lined with papillae to increase nutrient absorption
- Located on the left side of the animal""")
  imagerumen = Image.open('rumen.jpg')
  imagerumen.show()
  go_back()


def Roticulum():
  styling("""
██████╗░███████╗████████╗██╗░█████╗░██╗░░░██╗██╗░░░░░██╗░░░██╗███╗░░░███╗
██╔══██╗██╔════╝╚══██╔══╝██║██╔══██╗██║░░░██║██║░░░░░██║░░░██║████╗░████║
██████╔╝█████╗░░░░░██║░░░██║██║░░╚═╝██║░░░██║██║░░░░░██║░░░██║██╔████╔██║
██╔══██╗██╔══╝░░░░░██║░░░██║██║░░██╗██║░░░██║██║░░░░░██║░░░██║██║╚██╔╝██║
██║░░██║███████╗░░░██║░░░██║╚█████╔╝╚██████╔╝███████╗╚██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░╚════╝░░╚═════╝░╚══════╝░╚═════╝░╚═╝░░░░░╚═╝""","""
- Located near the heart
- Seperated from the rumen by a thin tissue
- Contains heavy or dense objects eaten by the animal""")
  imagereticulum = Image.open('reticulum.jpg')
  imagereticulum.show()
  go_back()


def Omasum():
  styling("""
░█████╗░███╗░░░███╗░█████╗░░██████╗██╗░░░██╗███╗░░░███╗
██╔══██╗████╗░████║██╔══██╗██╔════╝██║░░░██║████╗░████║
██║░░██║██╔████╔██║███████║╚█████╗░██║░░░██║██╔████╔██║
██║░░██║██║╚██╔╝██║██╔══██║░╚═══██╗██║░░░██║██║╚██╔╝██║
╚█████╔╝██║░╚═╝░██║██║░░██║██████╔╝╚██████╔╝██║░╚═╝░██║
░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝""","""
- R o u n d
- Contains layers of thin tissue
- Absorbs moisture""")
  imageomasum = Image.open('omasum.jpg')
  imageomasum.show()
  go_back()

def Abomasum():
  styling("""
░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░░██████╗██╗░░░██╗███╗░░░███╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██║░░░██║████╗░████║
███████║██████╦╝██║░░██║██╔████╔██║███████║╚█████╗░██║░░░██║██╔████╔██║
██╔══██║██╔══██╗██║░░██║██║╚██╔╝██║██╔══██║░╚═══██╗██║░░░██║██║╚██╔╝██║
██║░░██║██████╦╝╚█████╔╝██║░╚═╝░██║██║░░██║██████╔╝╚██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝""","""
- Lined with glands that secreate hydrochloric acid ad digestive enzymes
- the most similar to a non ruminant's stomach""")
  go_back()


def Small_Intestine():
  styling("""
░██████╗███╗░░░███╗░█████╗░██╗░░░░░██╗░░░░░  ██╗███╗░░██╗████████╗███████╗░██████╗████████╗██╗███╗░░██╗███████╗
██╔════╝████╗░████║██╔══██╗██║░░░░░██║░░░░░  ██║████╗░██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║████╗░██║██╔════╝
╚█████╗░██╔████╔██║███████║██║░░░░░██║░░░░░  ██║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░██║██╔██╗██║█████╗░░
░╚═══██╗██║╚██╔╝██║██╔══██║██║░░░░░██║░░░░░  ██║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██║██║╚████║██╔══╝░░
██████╔╝██║░╚═╝░██║██║░░██║███████╗███████╗  ██║██║░╚███║░░░██║░░░███████╗██████╔╝░░░██║░░░██║██║░╚███║███████╗
╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝  ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚══════╝""","""
- 3 sections: the duodenum, jejunum and ileum
- More than 20x the length of the animal
- Digestion is aided through secretions from the pancrease and gallbladder
- Nutrients enter the bloodstream through the small intestine through villi""")
  imagesmall_intestine = Image.open('small_intestine.jpg')
  imagesmall_intestine.show()
  go_back()

def Cecum():
  styling("""
░█████╗░███████╗░█████╗░██╗░░░██╗███╗░░░███╗
██╔══██╗██╔════╝██╔══██╗██║░░░██║████╗░████║
██║░░╚═╝█████╗░░██║░░╚═╝██║░░░██║██╔████╔██║
██║░░██╗██╔══╝░░██║░░██╗██║░░░██║██║╚██╔╝██║
╚█████╔╝███████╗╚█████╔╝╚██████╔╝██║░╚═╝░██║
░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝""","""
- Where the small and large intestine meet
- Breaks down some undigested fivers
- Its function is unknown""")
  imagececum = Image.open('cecum.jpg')
  imagececum.show()
  go_back()

def Large_Intestine():
  styling("""
██╗░░░░░░█████╗░██████╗░░██████╗░███████╗  ██╗███╗░░██╗████████╗███████╗░██████╗████████╗██╗███╗░░██╗███████╗
██║░░░░░██╔══██╗██╔══██╗██╔════╝░██╔════╝  ██║████╗░██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██║████╗░██║██╔════╝
██║░░░░░███████║██████╔╝██║░░██╗░█████╗░░  ██║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░██║██╔██╗██║█████╗░░
██║░░░░░██╔══██║██╔══██╗██║░░╚██╗██╔══╝░░  ██║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░██║██║╚████║██╔══╝░░
███████╗██║░░██║██║░░██║╚██████╔╝███████╗  ██║██║░╚███║░░░██║░░░███████╗██████╔╝░░░██║░░░██║██║░╚███║███████╗
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝  ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝╚══════╝""","""
- Microbes digest some remaining fibers
- Absorbs water""")
  go_back()

def Rectum():
  styling("""
██████╗░███████╗░█████╗░████████╗██╗░░░██╗███╗░░░███╗
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║░░░██║████╗░████║
██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░░██║██╔████╔██║
██╔══██╗██╔══╝░░██║░░██╗░░░██║░░░██║░░░██║██║╚██╔╝██║
██║░░██║███████╗╚█████╔╝░░░██║░░░╚██████╔╝██║░╚═╝░██║
╚═╝░░╚═╝╚══════╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░░░░╚═╝""","""
- Also known as the anus
- Excretes faeces and waste outside the body""")
  imagerectum = Image.open('rectum.png')
  imagerectum.show()
  go_back()







def styling(ASCII,TEXT):
  print(spaces)
  print(Fore.RED + ASCII + Style.RESET_ALL + TEXT)


def go_back():
  input(Back.YELLOW + "Hit Enter to go back. " + Style.RESET_ALL)
  choice()
menu()