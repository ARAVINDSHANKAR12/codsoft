import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")

        self.label = tk.Label(master, text="Choose: Rock, Paper, or Scissors")
        self.label.pack()

        self.user_choice = tk.StringVar()
        self.computer_choice = tk.StringVar()
        self.result = tk.StringVar()
        
        self.user_score = 0
        self.computer_score = 0

        choices = ["Rock", "Paper", "Scissors"]

        self.user_choice.set("")

        self.user_label = tk.Label(master, text="Your Choice:")
        self.user_label.pack()

        self.user_menu = tk.OptionMenu(master, self.user_choice, *choices)
        self.user_menu.pack()

        self.result_label = tk.Label(master, textvariable=self.result)
        self.result_label.pack()

        self.computer_label = tk.Label(master, textvariable=self.computer_choice)
        self.computer_label.pack()

        self.score_label = tk.Label(master, text="Score: You - 0, Computer - 0")
        self.score_label.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.play_button.pack(pady=5)

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again, bg="#2196F3", fg="white", font=("Arial", 12, "bold"), state="disabled")
        self.play_again_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Score", command=self.reset_score, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
        self.reset_button.pack(pady=5)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="#555", fg="white", font=("Arial", 12, "bold"))
        self.quit_button.pack(pady=5)

    def play(self):
        choices = ["Rock", "Paper", "Scissors"]
        user_choice = self.user_choice.get()
        computer_choice = random.choice(choices)
        self.computer_choice.set("Computer's Choice: " + computer_choice)

        if user_choice == computer_choice:
            self.result.set("It's a tie!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            self.result.set("You win!")
            self.user_score += 1
        else:
            self.result.set("You lose!")
            self.computer_score += 1

        self.score_label.config(text="Score: You - {}, Computer - {}".format(self.user_score, self.computer_score))

        if self.user_score == 5 or self.computer_score == 5:
            self.result.set("Game Over! You Win!" if self.user_score == 5 else "Game Over! Computer Wins!")
            self.play_again_button.config(state="normal")
            self.play_button.config(state="disabled")

    def play_again(self):
        self.result.set("")
        self.computer_choice.set("")
        self.user_choice.set("")
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You - 0, Computer - 0")
        self.play_button.config(state="normal")
        self.play_again_button.config(state="disabled")

    def reset_score(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You - {}, Computer - {}".format(self.user_score, self.computer_score))
        

def main():
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
