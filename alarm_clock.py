import datetime
import webbrowser


def ring_alarm():
    webbrowser .open_new_tab("https://www.youtube.com/watch?v=iNpXCzaWW1s")

print("What time would you like to wake up?")
alarm_hour = int(input("Hour (0-24): "))
alarm_minute = int(input("Minute (00-60) "))


print("Alarm set successfully!\n")


time_hour = int(datetime.datetime.now().hour)  # type: int
time_minute = int(datetime.datetime.now().minute)

while (1 == 1):
    if alarm_hour == datetime.datetime.now() .hour and alarm_minute == datetime.datetime.now() .minute:
        ring_alarm()
        break




