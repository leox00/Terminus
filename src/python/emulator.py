from terminus import renderer
class TerminalEmulator:
    def __init__(self):
        pass

    def display_text(self, text):
        renderer.render(text)

if __name__ == "__main__":
    emulator = TerminalEmulator()
    emulator.display_text("Hello, Terminus!")