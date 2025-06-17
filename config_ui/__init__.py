import tkinter as tk

class Config_window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Config Window")

        self.window_width = 250
        self.window_height = 120
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - self.window_width / 2)
        center_y = int(screen_height/2 - self.window_height / 2)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)

        #self.root.attributes('-alpha', 0.95)
        self.root.attributes('-topmost', 1)

        self.root.iconbitmap('./icon.ico')

        # rows and columns
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        # # #

        # hour
        hour_label = tk.Label(self.root, text="Hour:")
        hour_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

        hour_current_value = tk.StringVar(value=0)
        hour_spin_box = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        hour_spin_box.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        # minutes
        minute_label = tk.Label(self.root, text="Minute:")
        minute_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        minute_current_value = tk.StringVar(value=0)
        minute_spin_box = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        minute_spin_box.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # seconds
        minute_label = tk.Label(self.root, text="Seconds:")
        minute_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

        second_current_value = tk.StringVar(value=0)
        second_spin_box = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        second_spin_box.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        update_button = tk.Button(self.root, text="Update time")
        update_button.grid(column=0, row=3, padx=5, pady=5, columnspan=2)

    def show(self):
        self.root.mainloop()