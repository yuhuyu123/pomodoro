import time

# Get time and convert it to int value, with error checker


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


x = configure_all()
print(x)
