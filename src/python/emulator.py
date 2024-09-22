import sys
import os

# Add the root directory to PYTHONPATH
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root_dir)

from terminus import renderer

class TerminalEmulator:
    def __init__(self):
        pass

    def display_text(self, text):
        renderer.render(text)

    def run(self):
        while True:
            command = input("Enter command: ")
            self.display_text(f"Executed: {command}")

if __name__ == "__main__":
    emulator = TerminalEmulator()
    emulator.run()