from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score:0", fg="white", bg=THEME_COLOR, font=("Arial", 10, "italic"))
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="Hello", fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true = Button(image=true_img, highlightthickness=0)
        self.true.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false = Button(image=false_img, highlightthickness=0)
        self.false.grid(column=1, row=2)





        self.window.mainloop()


    def get_next_question(self):
       q_text = self.quiz.next_question()
       self.canvas.itemconfig(self_text)