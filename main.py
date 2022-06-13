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


# Calls the function get_time 3 times and return a tuple with the values for different times
def pomodoro():
    study_time = get_time("Study Time")
    short_break = get_time("Short_Break")
    long_break = get_time("Long Break")
    return study_time, short_break, long_break

# start the pomodoro input argument is a tupple containing the 3 values for study time, short and long break


def start_pomodoro():
    time_tuple = pomodoro()
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


start_pomodoro()
