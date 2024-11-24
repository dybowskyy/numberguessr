import customtkinter as ctk
import random
from PIL import Image
from select import error

# WHAT THE NUMBERGUESSR NEEDS:
# 1. An input box with a way to store user's input in a variable - DONE
# 2. A function that generates a random number and checks whether the input matches the number. - DONE
#    a) Notify the player whether they guess correctly or not
#    b) Add a limit on guesses, leading to "Game over" if they exceed it.
# 3. Feedback mechanism - a function that tells the user either "Too high!" or "Too low!" depending on his guess - DONE
# 4. Difficulty levels - allow the user to choose his difficulty level. E.g. 1-10, 1-50, 1-100 etc.
# 5. Create and allow the user to change the game's themes
# 6. Error handling
# 7. The ability to save progress
# 8. A good-looking UI with effects/animations

class NumberGuessr(ctk.CTk):
    def __init__(self):
        super().__init__()

    def new_round(self):
        self.randomNumber = random.randint(1, 10)
        self.jinn_dialog.configure(text="Take a guess")

    def user_guess(self, user_guess):
        print(user_guess)
        print(self.randomNumber)
        try:
            if int(user_guess) > self.randomNumber:
                self.jinn_dialog.configure(text="Too high!")
            elif int(user_guess) < self.randomNumber:
                self.jinn_dialog.configure(text="Too low!")
            elif int(user_guess) == self.randomNumber:
                self.jinn_dialog.configure(text="Correct!")
                self.after(3000, self.new_round)
        except Exception as e:
            self.jinn_dialog.configure(text="Please enter a valid number.")


class NumberGuessrUI(NumberGuessr):
    def __init__(self):
        super().__init__()
        # Configure the window
        self.title("NumberGuessr")
        self.geometry("360x600")
        self.resizable(False, False)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        # Configure the grid layout
        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.grid(sticky="nsew", row=0, column=0, padx=20, pady=20)
        self.main_frame.rowconfigure((0, 5), weight=0)
        self.main_frame.rowconfigure((1, 2, 3, 4), weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        # Game title
        self.game_title = ctk.CTkLabel(master=self.main_frame, font=("Roboto", 30), text="NumberGuessr", width=320)
        self.game_title.grid(row=1, pady=30, sticky="nswe")
        # Image + text
        self.jinn_text = "Take a guess"
        self.jinn_image = ctk.CTkImage(dark_image=Image.open("sprites/chilldawg.png"), size=(151, 214))
        self.jinn_dialog = ctk.CTkLabel(master=self.main_frame, image=self.jinn_image, text=self.jinn_text, compound="left", font=("Roboto", 25), anchor="nw")
        self.jinn_dialog.grid(row=2, pady=10, sticky="nswe")
        # Empty field
        self.empty_field = ctk.CTkLabel(master=self.main_frame, height=150, text="")
        self.empty_field.grid(row=3)
        # Input Field
        self.input_field = ctk.CTkEntry(master=self.main_frame,  font=("Roboto", 20), width=320)
        self.input_field.grid(row=4, pady=5, sticky="nswe")
        self.input_field.bind("<Return>", lambda event: self.user_guess(self.input_field.get()))
        # Guess button
        self.guess_button = ctk.CTkButton(master=self.main_frame, width=320, font=("Roboto", 20), text="GUESS", hover=True, command=lambda: self.user_guess(self.input_field.get()))
        self.guess_button.grid(row=5, pady=5, sticky="nswe")

        self.new_round()

if __name__ == "__main__":
    app = NumberGuessrUI()
    app.mainloop()

