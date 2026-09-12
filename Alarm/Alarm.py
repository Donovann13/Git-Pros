import time
import datetime
import pygame

def set_alarm(alarm_time):

    import os
    from dotenv import load_dotenv
    load_dotenv()
    MP3_File = os.getenv("MP3_File")

    sound_file = f"{MP3_File}"
    isrunning = True

    while isrunning:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == alarm_time:
            isrunning = False
            print("---WAKE UP!---")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)



if __name__ == "__main__":

    alarm_time = input("Enter the Hour of alarm time (00-23): ") + ":" + input("Enter the Minute of alarm time (00-59): ") + ":" + input("Enter the Second of alarm time (00-59): ")
    set_alarm(alarm_time)