import customtkinter as ctk
import random

# WHAT THE NUMBERGUESSR NEEDS:
# 1. An input box with a way to store user's input in a variable
# 2. A function that generates a random number and checks whether the input matches the number.
#    a) Notify the player whether they guess correctly or not
#    b) Add a limit on guesses, leading to "Game over" if they exceed it.
# 3. Feedback mechanism - a function that tells the user either "Too high!" or "Too low!" depending on his guess
# 4. Difficulty levels - allow the user to choose his difficulty level. E.g. 1-10, 1-50, 1-100 etc.
# 5. Create and allow the user to change the game's themes
# 6. Error handling
# 7. The ability to save progress
# 8. A good-looking UI with effects/animations

def num_gen(event):
    print("hello")

# class NumberGuessr(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Guess the Number")
#         self.geometry("360x600")
#         ctk.set_appearance_mode("dark")
#         ctk.set_default_color_theme("dark-blue")
#
#         self.frame = ctk.CTkFrame(master=self)
#         self.frame.pack(side="bottom", pady=100)
#
#         self.entry = ctk.CTkEntry(master=self.frame, font=("Roboto", 13), width=225)
#         self.entry.pack(pady=20)
#         self.entry.bind("<Return>", num_gen)

class NumberGuessr(ctk.CTk):
    def __init__(self):
        super().__init__()

    def gen_random_number(self):
        pass

    def check_the_guess(self):
        pass

    def start_a_new_round(self):
        pass

class NumberGuessrUI(ctk.CTk, NumberGuessr):
    def __init__(self):
        super().__init__()


def main():
    pass

app = NumberGuessr()
app.mainloop()