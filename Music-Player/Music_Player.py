import os,pygame
from dotenv import load_dotenv

def main():

    load_dotenv()
    folder_path = os.getenv("folder_path")
    folder_isdir = os.path.isdir(folder_path)
    if not folder_isdir:
        print("Invalid Path!")
    else:
        print("\n******** MP3 Player ********\nMP3 Files:\n")
        if os.listdir(folder_path):
            for index,file in enumerate(os.listdir(folder_path)):
                print(f"{index+1}. {file}") 

            isrunning = True
            while isrunning:
                choice = input("\nEnter the # of song to play (q to quit) > ").lower()
                if choice == "q":
                    print("Bye!\n")
                    isrunning = False
                elif not choice.isdigit():
                    print("Invalid Input!")
                    continue
                elif not (0 < int(choice) <= len(os.listdir(folder_path))):
                    print("Invalid Input!")
                    continue
                else:
                    filename = os.listdir(folder_path)[int(choice)-1]
                    sound_file = os.path.join(folder_path,filename)
                    pygame.mixer.init()
                    pygame.mixer.music.load(sound_file)
                    pygame.mixer.music.play()

                    isplaying = True
                    while isplaying:
                        choice2 = input("\n[P]ause/[R]esume/[S]top/[Q]uit > ").upper()

                        if choice2 == 'Q':
                            print("Bye!\n")
                            isplaying = False
                            isrunning = False
                        if choice2 == 'P':
                            print(f"{filename} Paused")
                            pygame.mixer.music.pause()
                        if choice2 == 'R':
                            print(f"{filename} Resumed")
                            pygame.mixer.music.unpause()
                        if choice2 == 'S':
                            print(f"{filename} Stoped\n")
                            pygame.mixer.music.stop()
                            isplaying = False
                            for index,file in enumerate(os.listdir(folder_path)):
                                print(f"{index+1}. {file}") 

if __name__ == "__main__":
    main()