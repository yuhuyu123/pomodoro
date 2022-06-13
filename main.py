import time

# Get time and convert it to int value in seconds, with error checker

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
    return config
    
def menu():
    print("Pomodoro menu:")
    print("1. Start pomodoro")
    print("2. Check Pomodoro times")
    print("3. Configure all Pomodoro times")
    print("4. Check Statistics")
    print("5. About")
    selection = input("Select an option: ")
    if selection == 1:
        return#TODO implement function
    elif selection == 2:
        return#TODO check if there's config file and print current config, if not ask if want to configure
    elif selection == 3:
        return#TODO configure Pomodoro times
    elif selection == 4:
        return#TODO implement log saver and statistics report
    elif selection ==5:
        print("Pomodoro terminal, coded by Yuhuyu.")


# pomodoro temporal function
def start_pomodoro():
    time_tuple = configure()
    block = 1

    while True:

        print(f"{block} pomodoro")
        time.sleep(time_tuple[0])
        
        if block != 4:

            print(f"short break {time_tuple[1]} minutes")
            time.sleep(time_tuple[1])
            block += 1
        else:
                   
            print(f"Long break {time_tuple[2]} minutes")
            time.sleep(time_tuple[2])
            break