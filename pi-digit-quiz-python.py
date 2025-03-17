import tkinter as tk
from tkinter import messagebox
import random

class PiDigitQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Pi Digit Quiz")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Pi to 100 digits (first 100 decimal places)
        self.pi_digits = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        
        # Initialize variables
        self.position = 0
        self.score = 0
        self.attempts = 0
        
        # Create GUI elements
        self.create_widgets()
        
        # Generate first question
        self.generate_question()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Pi Digit Quiz", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        
        # Instructions
        instructions = "What is the digit at position {} of Pi?"
        self.question_label = tk.Label(self.root, text=instructions.format(""), font=("Arial", 12))
        self.question_label.pack(pady=10)
        
        # Entry for user answer
        self.answer_var = tk.StringVar()
        self.answer_entry = tk.Entry(self.root, textvariable=self.answer_var, font=("Arial", 14), width=5, justify="center")
        self.answer_entry.pack(pady=10)
        
        # Check button
        check_button = tk.Button(self.root, text="Check Answer", command=self.check_answer, font=("Arial", 12), bg="#4287f5", fg="white")
        check_button.pack(pady=10)
        
        # Score label
        self.score_label = tk.Label(self.root, text="Score: 0/0", font=("Arial", 12))
        self.score_label.pack(pady=10)
        
        # Bind Enter key to check answer
        self.root.bind('<Return>', lambda event: self.check_answer())
    
    def generate_question(self):
        # Generate a random position between 1 and 100
        self.position = random.randint(1, 100)
        self.question_label.config(text=f"What is the digit at position {self.position} of Pi?")
        self.answer_var.set("")  # Clear previous answer
        self.answer_entry.focus()  # Set focus to entry field
    
    def check_answer(self):
        user_answer = self.answer_var.get().strip()
        
        # Validate input
        if not user_answer.isdigit() or len(user_answer) != 1:
            messagebox.showerror("Invalid Input", "Please enter a single digit (0-9).")
            self.answer_var.set("")
            return
        
        # Get correct digit
        correct_digit = self.pi_digits[self.position - 1]
        
        # Update score and show feedback
        self.attempts += 1
        if user_answer == correct_digit:
            self.score += 1
            messagebox.showinfo("Correct!", f"The digit at position {self.position} is indeed {correct_digit}.")
        else:
            messagebox.showerror("Incorrect", f"The digit at position {self.position} is {correct_digit}.")
        
        # Update score label
        self.score_label.config(text=f"Score: {self.score}/{self.attempts}")
        
        # Generate new question
        self.generate_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = PiDigitQuiz(root)
    root.mainloop()
