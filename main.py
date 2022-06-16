import pickle
from os.path import exists
import time
from playsound import playsound

# Get time and convert it to int value in seconds, with input error checker
def get_time(vara):
    alarm_input = input(f"Enter time for {vara} in minutes: ")
    while True:
        try:
            alarm_input = int(alarm_input) * 60
            print(f"{vara} set to : {alarm_input/60} minutes.")
            return alarm_input
        except ValueError:
            print("Oops! the input is not a number in minutes, try again...")


# config function that return pomodoro variable as dictionary
def configure_all():
    config = {}
    config["pomodoro time"] = get_time("Study Time")
    config["short break"] = get_time("Short_Break")
    config["long break"] = get_time("Long Break")
    
    with open('pomoconfig.pkl', 'wb+') as f:
        pickle.dump(config, f)

    print("\nPomodoro succesfully configured")
    time.sleep(2)

# Main menu
def menu():

    print("\nPomodoro menu:")
    print("\n1. Start pomodoro")
    print("2. Check Pomodoro times")
    print("3. Configure all Pomodoro times")
    print("4. Check Statistics")
    print("5. About")

    selection = input("\nSelect an option: ")

    while True:
        try:
            selection = int(selection)

            if selection >= 1 and selection <= 5:
                break
            else:
                selection = input(
                    "Not a valid option, please select a valid option between 1-5: ")
        except ValueError:
            selection = input(
                "Not a valid option, please select a valid option: ")

    if selection == 1:
        if exists("pomoconfig.pkl"):
            with open('pomoconfig.pkl', 'rb') as f:
                config = pickle.load(f)
            start_pomodoro(config)

        else:
            selection = input(
                "\nPomodoro not configured, do you want to configure pomodoro? y/n: ")
            if selection == "y":
                configure_all()
    elif selection == 2:
        if exists("pomoconfig.pkl"):
            with open('pomoconfig.pkl', 'rb') as f:
                config = pickle.load(f)
                print("\n")

                for key in config:
                     print(key.capitalize(), ": ",config[key]/60," minutes")
                time.sleep(2)
        else:
            selection = input(
                "\nPomodoro not configured, do you want to configure pomodoro? y/n: ")
            if selection == "y":
                configure_all()
            else:
                return

    elif selection == 3:
        configure_all()

    elif selection == 4:
        print("\nStill not implemented")
        time.sleep(2)
        return  # TODO implement log saver and statistics report

    elif selection == 5:
        print("\nPomodoro terminal, coded by Yuhuyu.")
        time.sleep(3)


# Pomodoro temporal function
# TODO Allow stop/resume/going back to menu
# TODO Implement log saving for statistics 
def start_pomodoro(config):
    while True:
        sound_pause = "sound.mp3"
        sound_pomo  = "pomo.mp3"
        block = 1
        pomo = config["pomodoro time"]
        short = config["short break"]
        long = config["long break"]

        while True:
            playsound(sound_pomo)
            print(f"{block} pomodoro {pomo/60} minutes")
            time.sleep(pomo)


            if block != 4:
                playsound(sound_pause)
                print(f"short break {short/60} minutes")
                time.sleep(short)
                block += 1
                
            else:
                playsound(sound_pause)
                print(f"Long break {long/60} minutes")
                time.sleep(long)
                break


while True:
    menu()

