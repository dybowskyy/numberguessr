import customtkinter as ctk
import random

# WHAT THE NUMBER GUESSING APP NEEDS:
# 1. Input box
# 2. Function to check if the number input matches the random number, if so outputs the result in console

def num_gen(event):
    print("hello")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Guess the Number")
        self.geometry("360x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(side="bottom", pady=100)
        self.frame1 = ctk.CTkFrame(master=self)
        self.frame1.pack(side="top", pady=40)

        self.label = ctk.CTkLabel(master=self.frame1, text="NUMBERGUESSR", font=("Roboto-Bold", 35))
        self.label.pack()

        self.entry = ctk.CTkEntry(master=self.frame, font=("Roboto", 13), width=225)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", num_gen)


app = App()
app.mainloop()