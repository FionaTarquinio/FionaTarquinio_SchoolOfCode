import tkinter as tk

from palindrome_detector import check_palindrome

class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label_0 = tk.Label(self, text = "Welcome to the Palindrome Detector!\n", fg = "#1D24CA", bg = "#98ABEE", font = "bold")
        self.label_0.pack()
        self.label_1 = tk.Label(self, text = "Enter word or phrase (no numbers or punctuation characters):", fg = "#201658", bg = "#98ABEE")
        self.label_1.pack()
        self.entry_0 = tk.Entry(self, bg = "#F9E8C9")
        self.entry_0.pack()
        self.space_0 = tk.Label(self, text = "", bg = "#98ABEE") # Added this so that button is not touching entry box
        self.space_0.pack()
        self.btn = tk.Button(self, text = "Submit", command = self.submit)
        self.btn.pack()
        self.label_2 = tk.Label(self, fg = "#1D24CA", bg = "#98ABEE")
        self.label_2.pack()

    def submit(self):
        self.user_input = self.entry_0.get()
        self.label_2["text"] = check_palindrome(self.user_input)

if __name__ == "__main__":
    root = Root()
    root.geometry("400x200")
    root["bg"] = "#98ABEE"
    root.mainloop()
        