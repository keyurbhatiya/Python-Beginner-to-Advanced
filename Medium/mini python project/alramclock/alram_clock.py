from playsound import playsound
import time

CLEAR_SCREEN = "\033[2J\033[H"
MOVE_CURSOR_HOME = "\r"

def alarm(seconds):
    print(CLEAR_SCREEN)
    print("Alarm will sound in:")

    while seconds > 0:
        minutes_left = seconds // 60
        seconds_left = seconds % 60

        print(f"{MOVE_CURSOR_HOME}{minutes_left:02d}:{seconds_left:02d}", end="")

        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

    try:
        playsound('mirzapur.mp3')  # Replace with your actual sound file path
    except Exception as e:
        print(f"Error playing sound: {e}")

if __name__ == "__main__":
    try:
        minutes = int(input("How many minutes to wait: "))
        seconds = int(input("How many seconds to wait: "))
        total_time = minutes * 60 + seconds

        alarm(total_time)
    except ValueError:
        print("Please enter valid numbers for minutes and seconds.")
