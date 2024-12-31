from tkinter import *
from random import randint, choice

def checkAnswer():
    try:
        user_input = float(youranswer.get())  # Convert user input to a number
        if user_input == answer:
            resultLabel.config(text='CORRECT!', fg="#4CAF50")  # Green for correct
        else:
            resultLabel.config(text='INCORRECT!', fg="#F44336")  # Red for incorrect
    except ValueError:
        resultLabel.config(text="Invalid input! Enter a number.", fg="#FF9800")  # Orange for invalid input

# Initialize the GUI
root = Tk()
root.geometry("400x300")
root.title("Modern Maths Quiz")
root.configure(bg="#2C3E50")  # Background color

# Heading
headingLabel = Label(root, text="MATHS QUIZ", font=('Helvetica', 24, 'bold'), bg="#2C3E50", fg="#ECF0F1")
headingLabel.pack(pady=20)

# Generate question
num1 = randint(1, 100)
num2 = randint(1, 100)
operator = choice(['+', '-', '*', '/'])
if operator == '/':
    num1 *= num2  # Ensure integer division
question = f"{num1} {operator} {num2}"
answer = eval(question)

# Display question
questionLabel = Label(root, text=question, font=('Helvetica', 20), bg="#2C3E50", fg="#ECF0F1")
questionLabel.pack(pady=20)

# Input field
youranswer = StringVar()
answerEntry = Entry(root, textvariable=youranswer, font=('Helvetica', 18), justify='center', bg="#ECF0F1", fg="#2C3E50", relief=FLAT)
answerEntry.pack(pady=10, ipady=5, ipadx=10)

# Submit button
def on_enter(e):
    submit.config(bg="#1ABC9C")  # Hover color

def on_leave(e):
    submit.config(bg="#16A085")  # Default color

submit = Button(root, text="Submit", font=('Helvetica', 18, 'bold'), bg="#16A085", fg="#ECF0F1", relief=FLAT, command=checkAnswer)
submit.pack(pady=20)
submit.bind("<Enter>", on_enter)
submit.bind("<Leave>", on_leave)

# Result label
resultLabel = Label(root, text='', font=('Helvetica', 18), bg="#2C3E50", fg="#ECF0F1")
resultLabel.pack(pady=20)

# Run the GUI
root.mainloop()
