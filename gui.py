import tkinter as tk
from PIL import Image, ImageTk


class SleepTrackerUI:
    def __init__(self, root):
        # Initialize the UI with the main root window
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        # Set up the main window and initialize all frames
        self.root.title("NightNest")
        self.root.geometry("400x420")
        self.root.resizable(False, False)

        self.home_frame = tk.Frame(self.root, bg="#121212")
        self.loading_frame = tk.Frame(self.root, bg="#121212")
        self.data_frame = tk.Frame(self.root)
        self.error_frame = tk.Frame(self.root, bg="#121212")

        self.setup_home_frame()
        self.setup_loading_frame()
        self.setup_error_frame()

        self.show_frame("home")

    def setup_home_frame(self):
        # Configure the home screen layout and visuals
        self.home_bg_image = Image.open("bg/bg.jpg").resize(
            (400, 420), Image.Resampling.LANCZOS
        )
        self.home_bg_photo = ImageTk.PhotoImage(self.home_bg_image)

        self.home_canvas = tk.Canvas(
            self.home_frame, width=400, height=420, highlightthickness=0
        )
        self.home_canvas.pack(fill="both", expand=True)
        self.home_canvas.create_image(
            0, 0, image=self.home_bg_photo, anchor="nw"
        )

        # Add title and subtitle text
        self.home_canvas.create_text(
            200, 140, text="NightNest",
            font=("Helvetica Neue", 30, "bold"), fill="white"
        )
        self.home_canvas.create_text(
            200, 190, text="Hi professional sleeper,",
            font=("Inter", 14), fill="white"
        )
        self.home_canvas.create_text(
            200, 220,
            text="Your sleep data is ready to be viewed!",
            font=("Inter", 14), fill="white"
        )

        # Add button to load data
        self.button_img = Image.open("bg/btn.jpg").resize((135, 35))
        self.button_photo = ImageTk.PhotoImage(self.button_img)

        self.home_button = tk.Label(
            self.home_canvas,
            image=self.button_photo,
            text="Log my score",
            compound="center",
            font=("Inter", 12),
            fg="white",
            bd=0,
            bg="#161817",
            cursor="hand2",
        )
        self.home_canvas.create_window(
            200, 260, window=self.home_button, anchor="center"
        )

    def setup_loading_frame(self):
        # Configure the loading screen with background and text
        self.loading_bg_image = Image.open("bg/bg_fetch_data.jpg").resize(
            (400, 420), Image.Resampling.LANCZOS
        )
        self.loading_bg_photo = ImageTk.PhotoImage(self.loading_bg_image)

        self.loading_canvas = tk.Canvas(
            self.loading_frame, width=400, height=420, highlightthickness=0
        )
        self.loading_canvas.pack(fill="both", expand=True)
        self.loading_canvas.create_image(
            0, 0, image=self.loading_bg_photo, anchor="nw"
        )

        self.loading_canvas.create_text(
            200, 140, text="Fetching data...",
            font=("Helvetica Neue", 30, "bold"), fill="white"
        )

        # Placeholder for motivational quote
        self.quote_text = self.loading_canvas.create_text(
            200, 210, text="", font=("Inter", 14),
            fill="white", width=350, justify="center"
        )

    def setup_error_frame(self):
        # Configure the error screen with message and close button
        self.error_label = tk.Label(
            self.error_frame,
            text="",
            font=("Helvetic Neue", 16, "bold"),
            fg="red",
            bg="#121212",
        )
        self.error_label.pack(pady=20)

        self.error_button = tk.Button(
            self.error_frame,
            text="Close",
            font=("Helvetica Neue", 14),
            command=lambda: self.show_frame("home"),
        )
        self.error_button.pack(pady=10)

    def setup_data_frame(self, sleep_index):
        # Set background image based on sleep index and prepare canvas
        if sleep_index > 81:
            bg_image = Image.open("bg/green.jpg")
        elif sleep_index > 62:
            bg_image = Image.open("bg/yellow.jpg")
        else:
            bg_image = Image.open("bg/red.jpg")

        self.data_bg_image = bg_image.resize(
            (400, 420), Image.Resampling.LANCZOS
        )
        self.data_bg_photo = ImageTk.PhotoImage(self.data_bg_image)

        # Clear any previous widgets before drawing new data
        for widget in self.data_frame.winfo_children():
            widget.destroy()

        self.data_canvas = tk.Canvas(
            self.data_frame, width=400, height=420, highlightthickness=0
        )
        self.data_canvas.pack(fill="both", expand=True)
        self.data_canvas.create_image(
            0, 0, image=self.data_bg_photo, anchor="nw"
        )

    def show_frame(self, frame_name):
        # Show the selected frame and hide all others
        frames = {
            "home": self.home_frame,
            "loading": self.loading_frame,
            "data": self.data_frame,
            "error": self.error_frame,
        }

        for frame in frames.values():
            frame.pack_forget()

        frames[frame_name].pack(fill=tk.BOTH, expand=True)

    def update_loading_quote(self, quote):
        # Update the motivational quote on the loading screen
        self.loading_canvas.itemconfig(self.quote_text, text=quote)

    def update_error_message(self, message):
        # Display an error message on the error screen
        self.error_label.config(text=f"Error: {message}")

    def update_data_screen(self, data):
        # Render sleep-related data on the data screen
        self.data_canvas.create_text(
            200, 90, text=data["sleep_index"],
            font=("Helvetica Neue", 45), fill="white"
        )
        self.data_canvas.create_text(
            200, 170, text=data["sleep_quality"],
            font=("Inter", 12, "bold"), fill="white"
        )
        self.data_canvas.create_text(
            200, 210, text=data["sleep_advice"],
            font=("Inter", 11), fill="white",
            justify="center", width=300
        )
        self.data_canvas.create_text(
            65, 282, text=data["bedtime_start"],
            font=("Inter", 9), fill="#626262"
        )
        self.data_canvas.create_text(
            355, 281.5, text=data["bedtime_end"],
            font=("Inter", 9), fill="#626262"
        )
        self.data_canvas.create_text(
            100, 320, text=f"{data['sleep_duration']}h",
            font=("Helvetica Neue", 16), fill="white"
        )
        self.data_canvas.create_text(
            300, 320, text=f"{data['sleep_cycles']} full",
            font=("Helvetica Neue", 16), fill="white"
        )
        self.data_canvas.create_text(
            100, 372, text=f"{data['resting_hr']} BPM",
            font=("Helvetica Neue", 16), fill="white"
        )
        self.data_canvas.create_text(
            300, 372, text=f"{data['avg_hrv']} ms",
            font=("Helvetica Neue", 16), fill="white"
        )
