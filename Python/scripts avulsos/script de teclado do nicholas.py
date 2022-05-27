import datetime
#from pynput.keyboard import Key, Controller
import keyboard
import mouse
import time

# CONFIG
#keyb = keyboard.add_hotkey('e')
keyboard.press('e')
keyboard.release('e')

seconds_delay = 30

is_active = True

def get_current_time():
    now = datetime.datetime.now()
    return f"{str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}:{str(now.second).zfill(2)}"
    

def change_active_state(key):
    global is_active
    is_active = not is_active
    print(f"{get_current_time()} - Active state changed to {is_active}")


def main():
    if seconds_delay < 5:
        print("Mano o delay entre cliques tá menor que 5 segundos, isso é insanidade, diminui isso O_O")
        return

    print(f"Script running with key '{key}' and {seconds_delay} seconds delay between each click")
    keyboard.on_press_key(key, change_active_state)

    while True:
        if is_active:
            mouse.click()
            print(f"{get_current_time()} - Triggered mouse click")
        time.sleep(seconds_delay)


if __name__ == "__main__":
    main()
