from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz = quiz
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(150, 125,
                                                width=280,
                                                fill=THEME_COLOR,
                                                font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=30, pady=30)

        self.button_true = Button(image=true_img, borderwidth=0, padx=20, pady=20,
                                  command=self.check_true)
        self.button_true.grid(row=2, column=0)

        self.button_false = Button(image=false_img, borderwidth=0, padx=20, pady=20,
                                   command=self.check_false)
        self.button_false.grid(row=2, column=1)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.configure(bg="white")
        self.button_true.config(state="normal")
        self.button_false.config(state="normal")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've' reached the end of quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.button_true.config(state="disabled")
        self.button_false.config(state="disabled")
        self.label.config(text=f"Score:{self.quiz.score}")
        self.window.after(1000, self.next_question)
