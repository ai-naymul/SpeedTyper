import tkinter as tk
import time
import random
import string

## Constant 
TIME_REMAINING = 0



window = tk.Tk()
window.geometry("900x900")
window.title("SpeedTyper Pro - Test Your Typing Speed")


#3 Generate random paragraph
def generate_random_paragraph(length):
    letters = string.ascii_lowercase + string.ascii_uppercase
    punctuation = '., '
    all_character = letters + punctuation
    random_paragraph = ''.join(random.choice(all_character) for _ in range(length))
    return random_paragraph

## SHow the paragraph when the start button is pressed
def start_game():
    global TIME_REMAINING
    ## Canvas for the praragraph
    para_canvas = tk.Canvas(window, width=400, height=200)
    # Generate the paragraph of 200 words
    random_paragraph = generate_random_paragraph(200)
    # showing the paragraph to the canvas
    para_text = tk.Text(para_canvas, wrap=tk.WORD, width=40, height=10)
    para_text.insert(tk.END, random_paragraph)
    para_canvas.grid(row=1, column=1)
    para_text.grid(row=1,column=1)
    para_canvas.create_window(200, 100, window=para_text)

    ## Start timer
    TIME_REMAINING = 60
    update_timer()
    

def update_timer():
    global TIME_REMAINING
    if TIME_REMAINING > 0:
        TIME_REMAINING -=1
        time_label.config(text=f"Time remaining: {TIME_REMAINING} seconds")
        window.after(1000, update_timer)


        







# Welcome Message
welcome_message = tk.Label(text="Welcome to the SpeedTyper Pro", font=(24,15,'bold'))






## Start Button
start_button = tk.Button(text="Start the Typing test", command=start_game)

## text input
type_text = tk.Text()
type_text_label = tk.Label(text="Enter your text here")


# Time label 
time_label = tk.Label(text="Time remaining: 60 seconds")







## Location of the widgets
welcome_message.grid(row=0, column=1)
type_text.grid(row=3,column=1)
type_text_label.grid(row=3,column=0)
start_button.grid(row=4, column=1, pady=25)
time_label.grid(row=2, column=1)


window.mainloop()