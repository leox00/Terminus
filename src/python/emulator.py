import sys
import os
import platform

# Add the root directory to PYTHONPATH
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(root_dir)

from terminus import renderer, pty_handler

class Shell:
    def __init__(self):
        self.pty_process = None

    def start(self):
        self.pty_process = pty_handler.start_pty()

    def read(self):
        if self.pty_process:
            if platform.system() == 'Windows':
                import msvcrt
                if msvcrt.kbhit():
                    return os.read(self.pty_process, 1024).decode()
            else:
                import select
                rlist, _, _ = select.select([self.pty_process], [], [], 0.1)
                if rlist:
                    return os.read(self.pty_process, 1024).decode()
        return ""

    def write(self, command):
        if self.pty_process:
            os.write(self.pty_process, command.encode())

class TerminalEmulator:
    def __init__(self):
        self.shell = Shell()
        self.shell.start()

    def display_text(self, text):
        renderer.render(text)

    def run(self):
        while True:
            output = self.shell.read()
            if output:
                self.display_text(output)
            command = input("Enter command: ")
            self.shell.write(command + "\n")

if __name__ == "__main__":
    emulator = TerminalEmulator()
    emulator.run()