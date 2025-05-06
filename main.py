import tkinter as tk
from gui import SleepTrackerUI
from data_handle import setup_events_and_run


class SleepTrackerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.ui = SleepTrackerUI(self.root)

        setup_events_and_run(self.root, self.ui)


if __name__ == "__main__":
    app = SleepTrackerApp()
