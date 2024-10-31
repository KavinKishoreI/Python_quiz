THEME_COLOR = "#375362"

from tkinter import *
from tkinter import messagebox

change=None

class UserInterface:
    def __init__(self, quiz_brain):
        self.new_quiz = quiz_brain

        self.window = Tk()
        self.window.config(pady=20, padx=20, background=THEME_COLOR)
        self.window.minsize(width=320, height=500)
        self.Score_label = Label(text=f"score:{self.new_quiz.score}", background=THEME_COLOR, font=['Arial', 24, 'italic'])
        self.Score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question = self.canvas.create_text(150, 130,width=280, text="", font=['Arial',13, 'bold'])
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')

        self.true_button = Button(image=true_image, pady=50,command=self.next_1)
        self.true_button.grid(row=2, column=1, padx=10)

        self.false_button = Button(image=false_image, pady=50,command=self.next_0)
        self.false_button.grid(row=2, column=0)

        self.start_quiz()
        self.window.mainloop()
    def start_quiz(self):
        try:
            a = self.new_quiz.next_question()
            self.canvas.itemconfig(self.question, text=a)
        except IndexError:
            self.Score_label.config(text=f'Thank You', font=['Bookman Old Style', 32, 'bold'])
            self.Score_label.grid(row=0, column=0, columnspan=2)
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question,
                                   text=f"Quiz Over.\n Final Score:{self.new_quiz.score}/{len(self.new_quiz.question_list)}",
                                   font=["Times New Roman", 30, 'normal'])

    def next_1(self):
        answer='True'
        result=self.new_quiz.check_answer(answer)
        if result==True:
            self.change_to_green()
            change=self.window.after(2000,func=self.change_normal)

        else:
            self.change_to_Red()
            change=self.window.after(2000,func=self.change_normal)

        self.Score_label.config(text=f"Score:{self.new_quiz.score}")
        self.window.after(2000, func=self.start_quiz)
    def next_0(self):
        answer='False'
        result = self.new_quiz.check_answer(answer)
        self.Score_label.config(text=f'Score:{self.new_quiz.score}')
        if result == True:
            self.change_to_green()
            self.window.after(2000, func=self.change_normal)
        else:
            self.change_to_Red()
            self.window.after(2000, func=self.change_normal)
        self.Score_label.config(text=f"Score:{self.new_quiz.score}")
        self.window.after(100,func=self.start_quiz)
    def change_to_green(self):
        self.canvas.config(bg='green')
    def change_to_Red(self):
        self.canvas.config(bg='red')
    def change_normal(self):
        self.canvas.config(bg='white')