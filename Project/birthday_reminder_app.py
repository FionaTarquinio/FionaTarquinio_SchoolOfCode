import tkinter as tk
import birthday_reminder

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Family Birthdays")
        self.label_0 = tk.Label(self, text = birthday_reminder.print_today(), fg = "#1D24CA", bg = "#EFF396", font = "bold")
        self.label_0.pack()
        self.space_0 = tk.Label(self, text = "", bg = "#EFF396") # Fix this if better method
        self.space_0.pack()
        self.btn_1 = tk.Button(self, text = "Find next birthday", command = self.submit_1)
        self.btn_1.pack()
        self.label_1 = tk.Label(self, fg = "#211C6A", bg = "#EFF396")
        self.label_1.pack()
        self.space_1 = tk.Label(self, text = "", bg = "#EFF396") # Fix this if beter method
        self.space_1.pack()
        self.btn_2 = tk.Button(self, text = "Find last birthday", command = self.submit_2)
        self.btn_2.pack()
        self.label_2 = tk.Label(self, fg = "#211C6A", bg = "#EFF396")
        self.label_2.pack()

    def submit_1(self):
  #      self.user_input = self.entry_0.get()
        self.label_1["text"] = birthday_reminder.find_next_birthday()

    def submit_2(self):
        self.label_2["text"] = birthday_reminder.find_last_birthday()

if __name__ == "__main__":
    root = Root()
    root.geometry("800x300")
    root["bg"] = "#EFF396"
    root.mainloop()