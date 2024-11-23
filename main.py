import customtkinter as ctk
import random

from select import error


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
    @staticmethod
    def gen_random_number(event) -> int:
        random_number = random.randint(1, 10)
        return random_number

    def guess(self, user_guess):
        random_number = self.gen_random_number(event=None)
        try:
            if random_number != int(user_guess):
                print(f'You guessed wrong. The number was {random_number}. Try again!')
            else:
                print(f'Correct!')
        except Exception as e: print(e)

    def start_a_new_round(self):
        pass

class NumberGuessrUI(NumberGuessr):
    def __init__(self):
        super().__init__()
        # Configure the window
        self.title("NumberGuessr")
        self.geometry(f'{360}x{600}')
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        # Configure the grid layout (3x3)
        # self.main_frame = ctk.CTkFrame(master=self, width=360, height=600)
        # self.main_frame.grid(sticky="nsew")
        # self.main_frame.rowconfigure((1, 2, 3, 4), weight=1)
        self.main_frame = ctk.CTkFrame(master=self, width=360, height=600)
        self.main_frame.grid(sticky="nsew")
        self.main_frame.rowconfigure((1, 2, 3, 4), weight=1)
        # Game title
        self.game_title = ctk.CTkLabel(master=self.main_frame, font=("Roboto", 25), width=200, text="NumberGuessr")
        self.game_title.grid(row=1)
        # Image + text
        # Feedback box
        # Input Field
        self.input_field = ctk.CTkEntry(master=self.main_frame, font=("Roboto", 20), width=200)
        self.input_field.grid(row=3)
        self.input_field.bind("<Return>", lambda event: self.guess(self.input_field.get()))
        # Guess button
        self.guess_button = ctk.CTkButton(master=self.main_frame, font=("Roboto", 20), width=200, text="GUESS", hover=True, command=lambda: self.guess(self.input_field.get()), anchor="center")
        self.guess_button.grid(row=4)

if __name__ == "__main__":
    app = NumberGuessrUI()
    app.mainloop()

