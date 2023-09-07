import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("General Knowledge Quiz")
        
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Paris", "Madrid"],
                "correct_option": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_option": "Mars"
            },
            {
                "question": "Who wrote the play 'Romeo and Juliet'?",
                "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
                "correct_option": "William Shakespeare"
            },
            {
                "question": "Which gas do plants absorb from the atmosphere?",
                "options": ["Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen"],
                "correct_option": "Carbon Dioxide"
            },
            {
                "question": "Which is the fastest language in programming",
                "options": ["C++", "Ruby", "Java", "C"],
                "correct_option": "C"
            },
            {
                "question": "Whats my BTech Brranch",
                "options": ["ME", "ECE", "IT", "CS"],
                "correct_option": "CS"
            },
            {
                "question": "Whats my College name",
                "options": ["IIT", "PSIT", "KIT", "NIET"],
                "correct_option": "NIET"
            },
            {
                "question": "My name is ______",
                "options": ["Ankur", "Anuj", "Jai", "Raj"],
                "correct_option": "Anuj"
            },
            {
                "question": "I live in _____",
                "options": ["Rajesthan", "UP", "Delhi", "Chennai"],
                "correct_option": "UP"
            }
        ]
        
        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack(pady=5, padx=20, fill=tk.X)

        self.next_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), command=self.next_question)
        self.next_button.pack(pady=20)
        
        self.update_question()

    def update_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
        else:
            self.show_result()

    def check_answer(self, selected_option):
        question_data = self.questions[self.current_question]
        correct_option = question_data["correct_option"]
        if question_data["options"][selected_option] == correct_option:
            self.score += 1
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.update_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    app = QuizApp(root)
    root.mainloop()
