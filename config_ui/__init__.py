import tkinter as tk
import json

class Config_window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Config Window")

        self.window_width = 250
        self.window_height = 250
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
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.rowconfigure(6, weight=1)
        self.root.rowconfigure(7, weight=1)
        self.root.rowconfigure(8, weight=1)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        # # #

        # study boxes
        # hour
        study_label = tk.Label(self.root, text="Study time")
        study_label.grid(column=0, row=0, padx=5, pady=5, columnspan=2)

        hour_label = tk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

        hour_current_value = tk.StringVar(value=0)
        self.hour_spin_box_study = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        self.hour_spin_box_study.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

        # minutes
        minute_label = tk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=2, sticky=tk.EW, padx=5, pady=5)

        minute_current_value = tk.StringVar(value=0)
        self.minute_spin_box_study = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        self.minute_spin_box_study.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

        # seconds
        seconds_label = tk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5)

        second_current_value = tk.StringVar(value=0)
        self.second_spin_box_study = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        self.second_spin_box_study.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)
        # # #

        # rest boxes
        rest_label = tk.Label(self.root, text="Rest time")
        rest_label.grid(column=0, row=4, padx=5, pady=5, columnspan=2)

        hour_label = tk.Label(self.root, text="Hours:")
        hour_label.grid(column=0, row=5, sticky=tk.EW, padx=5, pady=5)

        hour_current_value = tk.StringVar(value=0)
        self.hour_spin_box_rest = tk.Spinbox(self.root, from_=0, to=24, textvariable=hour_current_value)
        self.hour_spin_box_rest.grid(column=1, row=5, sticky=tk.EW, padx=5, pady=5)

        # minutes
        minute_label = tk.Label(self.root, text="Minutes:")
        minute_label.grid(column=0, row=6, sticky=tk.EW, padx=5, pady=5)

        minute_current_value = tk.StringVar(value=0)
        self.minute_spin_box_rest = tk.Spinbox(self.root, from_=0, to=60, textvariable=minute_current_value)
        self.minute_spin_box_rest.grid(column=1, row=6, sticky=tk.EW, padx=5, pady=5)

        # seconds
        seconds_label = tk.Label(self.root, text="Seconds:")
        seconds_label.grid(column=0, row=7, sticky=tk.EW, padx=5, pady=5)

        second_current_value = tk.StringVar(value=0)
        self.second_spin_box_rest = tk.Spinbox(self.root, from_=0, to=60, textvariable=second_current_value)
        self.second_spin_box_rest.grid(column=1, row=7, sticky=tk.EW, padx=5, pady=5)
        # # #

        self.config_button = tk.Button(self.root, text="Change config time", command=self.change_config_button_clicked)
        self.config_button.grid(column=0, row=8, padx=5, pady=5, columnspan=2)


    def change_config_button_clicked(self):
        try:
            study_hours = int(self.hour_spin_box_study.get())
            study_minutes = int(self.minute_spin_box_study.get())
            study_seconds = int(self.second_spin_box_study.get())

            study_time = study_hours * 3600 + study_minutes * 60 + study_seconds

            if study_time > 24 * 3600:
                study_time = 24 * 3600
        except (KeyError, TypeError, ValueError):
            study_time = 0
        
        try:
            rest_hours = int(self.hour_spin_box_rest.get())
            rest_minutes = int(self.minute_spin_box_rest.get())
            rest_seconds = int(self.second_spin_box_rest.get())

            rest_time = rest_hours * 3600 + rest_minutes * 60 + rest_seconds

            if rest_time > 24 * 3600:
                rest_time =  24 * 3600
        except (KeyError, TypeError, ValueError):
            rest_time = 0      

        dict_time = {
            "study_time" : study_time,
            "rest_time" : rest_time,
            "alarm" : "./assets/alarms/alarm.wav" 
        }

        with open("config.json", "w") as outfile:
            json.dump(dict_time, outfile)

    def show(self):
        self.root.mainloop()