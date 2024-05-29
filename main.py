from pystyle import Colors , Colorate , Write
from itertools import product
import string
from os import system , name 

system('cls' if name == 'nt' else 'clear')
system('title [+] * pass list Created By Darka * [+] || echo -e "\e]0;[+] * Web_Shock Created By Darka * [+]\a"')

banner = '''

                                            (    (              (         (                       Pytho Learn
                                            )\ : )\  (  (       )\   ( (  )\               
                                            ((_) (_() )\ )\     ((_)  )\)\((_)                    Iran On Top
                                            | _ \(_)()(_)(_)    | |  (_)(_) |_                
                                            |  _/ _` |_-/_-/    | |__| |_-/  _|
                                            |_| \__/_|__/__/    |____|_|__/\__|
                                            
                                     

            
                                      
                                      
'''
print(Colorate.Horizontal(Colors.red_to_blue , banner ))
min_len = int(Write.Input("[+] Enter minimum length of password [>>>] " , Colors.red_to_blue , interval = 0.05))
max_len = int(Write.Input("[+] Enter maximum length of password [>>>] " , Colors.red_to_blue , interval = 0.05))
counter = 0
character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
Write.Print('[+] generating passwords pls wait . . . ' , Colors.red_to_blue , interval = 0.05)
file_open = open("worldlist.txt",'w')

for i in range(min_len,max_len+1):
    for j in product(character,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter+=1
print(f"worldlist of {counter} passwords created")
