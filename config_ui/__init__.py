import tkinter as tk
import json

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
        hour_label = tk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

        hour_current_value = tk.StringVar(value=0)
        self.hour_spin_box = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        self.hour_spin_box.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

        # minutes
        minute_label = tk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        minute_current_value = tk.StringVar(value=0)
        self.minute_spin_box = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        self.minute_spin_box.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # seconds
        seconds_label = tk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

        second_current_value = tk.StringVar(value=0)
        self.second_spin_box = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        self.second_spin_box.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        self.config_button = tk.Button(self.root, text="Change config time", command=self.change_config_button_clicked)
        self.config_button.grid(column=0, row=3, padx=5, pady=5, columnspan=2)

    def change_config_button_clicked(self):
        hours = int(self.hour_spin_box.get())
        minutes = int(self.minute_spin_box.get())
        seconds = int(self.second_spin_box.get())
        #print(hours, minutes, seconds)

        dict_time = {
            "hours" : hours,
            "minutes" : minutes,
            "seconds" : seconds 
        }

        with open("config.json", "w") as outfile:
            json.dump(dict_time, outfile)

    def show(self):
        self.root.mainloop()