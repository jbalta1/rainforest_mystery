def main():
    print("You find yourself in the middle of a rainforest")
    print()
    rainforest_art = r"""
      ___
    _/   \_
   /       \
  (         )
   \       /
    \_____/ 
      |||
      |||
      |||
      |||

    """
    print(rainforest_art)

    # First it needs to be a ancient bridge to pass with a boolean action 

    # Infinite loop to make loops when is answer else.
    # Making use of continue for else and break to end the infinite loop
    
    while True:
        print("There is a bridge")
        
        
        if bridge_decision():
            print("You went over the bridge")
            bridge_art = r"""

            —————————————————————-—-—O =========== O——————————————————————
                                    /|=============|\
                    '--'-           () '=============' ()
                                    /| =============== |\        '--'-
                        '--'-      / |=================| \  
                                ()  =================  ()  '--'-    '--'-
                '--'-     '--'-  /| ------------------- |\
                                / |---------------------| \      '--'-    '--'-
            -'--'--'           ()  '---------------------'  ()
                            /| ------------------------- |\    --'--'--'
                --'--'     / |---------------------------| \    '--'
                            ()  |___________________________|  ()           '--'-
            --'-          /| _______________________________  |\
            --' gpyy      / |__________________________________| \
                    

            """
            print(bridge_art)
            # Discovering the ruins        

            if discover_ruins():
                print("Suddenly, you stumble upon clearing ancient revealing ruins and find a sign in one of the columns")
                ancient_ruins_art = r"""     
                        .----------.
                        :`.---------`.          .-----------.
                        '.|_.------..'          :`.----------`.  .-----.._
                        | ||    | ||           `.|__.------..' |`--..__.'|
                        | ||__..| ||-._ ___    | | |.... | ||-.|`--.._ |.'----.
                    _ .:::/ / |    | ||   ___  `--| | |  _  | ||  | | | | |\      `.
                .` `.  -'.|_|    `.||  /`.  `.  '.|_\     `.|/  | | | | ||`.      `.
                / `. _`.  `-   _     _  |  `.__`   _           _ `.|.' | || |\       \
                \   /   \ _            _ `. |   |     `--   _          '.|| | `.______.
                /`. |   |  .'`---...____   `'---' _       _          _    | | |'------'
                | /`.-_.' |`---...___ . |  `--      ______________________`.|_| |  ` |
                | | | '|  `---...____|.'    _     |`._-_______-______-_____`. | |    |
                .| | |  | _ |  .---. | '| `-       '.|  ' ' '  '  '  '  ' ' ' || |    |  
                ' `| |  |   /  ||  |'|  |      _    |'.__.-------.__.-----.__.'| | .- | \
                |  | |' |   |  ||  | |  |   `--     | |..|    |  |''|   | |::| `.|____| |
                \   `|__| _ |  || _| '. | .`-._     | |  |    |  |  |   | |  | `--     .'
                '.         |  ||  |  | | |`.  `. _ | |  |    |  |  |   | |  |   _    `.
                '-. _    \__|   |  | | |  `.__`. | |  | __ |  |  |___| |  |  `-- _  |
                    `''''.    _  `-.|.' '.  |   |  `|__| ___ `.|__| _ `.|__|        /
                    LGB :    _    _      `.|_.-'   `-             _          _   .'
                            `-._______.::.__     `-     _      _       ___.:::.__.-'
                                            `----.....__..------------`
                                            """
                print(ancient_ruins_art)
            
            else:
                print("Sorry, try again")
                #continue to go back to start the loop
                continue

            # A strange sign
            # read the sign
            
            
            if read_strange_sign():
                print("It says:'Here is a portal, push the rock in the center'") 

            else:
                print("Sorry, try again")
                continue

            # pushing the item in the panel

            if push_rock():
                print("The door opens and you find the treasure of the mistery of the rainforest")
                print(r'''
                *******************************************************************************
                        |                   |                  |                     |
                _________|________________.=""_;=.______________|_____________________|_______
                |                   |  ,-"_,=""     `"=.|                  |
                |___________________|__"=._o`"-._        `"=.______________|___________________
                        |                `"=._o`"=._      _`"=._                     |
                _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
                |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
                |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
                _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
                |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
                |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
                ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
                /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
                ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
                /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
                ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                /______/______/______/______/______/______/______/______/______/______/[TomekK]
                *******************************************************************************
                ''')            
                
                print("Congratulations you have found the treasure of the rainforest!")
                
            else: 
                print("Sorry, try again")
                continue

            
        else:
            print("You stay there")

            
        break

def bridge_decision ():
    answer = input("Would you like to pass the bridge? 'yes' or 'not'")
    print("You entered 'answer'", answer)
    return answer == "yes"
def discover_ruins ():
    answer = input("Would you take a look in front of you? 'yes' or 'not'")
    print("You entered 'answer'", answer)
    return answer == "yes"
def read_strange_sign ():
    answer = input("Would you like to read the sign? 'yes' or 'not'")
    print("You entered 'answer'", answer)
    return answer == "yes"
def push_rock ():
    answer = input("Would you like to push the rock? 'yes' or 'not'")
    print("You entered 'answer'", answer)
    return answer == "yes"

if __name__ == "__main__":
    main()


