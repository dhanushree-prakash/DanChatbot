import tkinter as tk
from tkinter import scrolledtext
import random
import datetime
import re
from textblob import Word

# Predefined patterns and responses for the chatbot
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing great, thank you!", "I'm fine, how about you?"]),
    (r"what is your name?", ["My name is Dan!", "I'm Dan, your friendly chatbot!"]),
    (r"what is the time?", [lambda: datetime.datetime.now().strftime("%H:%M:%S")]),
    (r"what is today's date?", [lambda: datetime.datetime.now().strftime("%Y-%m-%d")]),
    (r"tell me a joke", ["Why don't skeletons fight each other? They don't have the guts!", 
                         "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats."]),
    (r"bye", ["Goodbye! Take care!", "See you later!"]),
]

# Spell correction function using TextBlob
def correct_spelling(input_text, pattern_responses):
    # Correct spelling for user input
    input_text = Word(input_text).correct()

    # Match input with predefined patterns
    for pattern, responses in pattern_responses:
        if re.search(pattern, input_text.lower()):
            response = random.choice(responses)
            if callable(response):
                return response()
            return response
    return ["Sorry, I didn't understand that. Can you ask something else?"]


# Create the main window
root = tk.Tk()
root.title("Dan Chatbot")
root.geometry("500x600")  # Set the window size to avoid elongating
root.config(bg="#f4f7f6")  # Light background color for a modern look

# Chat log window (with modern design)
chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, state=tk.DISABLED, font=("Arial", 12), bg="#1a1a1a", fg="white", bd=0, relief="flat")
chat_log.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Entry field for user input (with sleek design)
entry_field = tk.Entry(root, width=40, font=("Arial", 14), bg="#ffffff", fg="#333333", bd=0, relief="flat", insertbackground="#333333")
entry_field.grid(row=1, column=0, padx=10, pady=10)

# Send message function
def send_message():
    user_input = entry_field.get()  # Get input from the user
    if user_input != "":
        chat_log.config(state=tk.NORMAL)  # Enable editing of chat log
        
        # Display user message in a separate bubble
        chat_log.insert(tk.END, "You: " + user_input + "\n")  # Display user input in chat window
        entry_field.delete(0, tk.END)  # Clear the input field
        
        # Get chatbot response based on predefined patterns with spell correction
        answer = correct_spelling(user_input, pairs)
        
        # Extract the string from the list (just in case it's a list)
        if isinstance(answer, list):
            answer = answer[0]  # Take the first element if it's a list
        
        # Display chatbot response in a separate bubble
        chat_log.insert(tk.END, "Dan: " + answer + "\n\n")  # Display chatbot response
        chat_log.config(state=tk.DISABLED)  # Disable editing of chat log
        
        # Scroll to the bottom to show the latest message
        chat_log.yview(tk.END)

# Button to send message (with sleek, modern design)
send_button = tk.Button(root, text="Send", width=20, height=2, font=("Arial", 14), command=send_message, bg="#4CAF50", fg="white", relief="flat", bd=0)
send_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Adding a header label with modern font, color, and shadow effect
header_label = tk.Label(root, text="Dan Chatbot", font=("Arial", 18, "bold"), fg="#4CAF50", bg="#f4f7f6", pady=10)
header_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Adding a footer label with modern font, color, and shadow effect
footer_label = tk.Label(root, text="Powered by Dan AI", font=("Arial", 12), fg="#4CAF50", bg="#f4f7f6")
footer_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Adding rounded corners and shadow effect to the entry field and button
def add_rounded_corners(widget):
    widget.config(highlightthickness=2, highlightbackground="#4CAF50", relief="flat", bd=0)

# Apply rounded corners and shadow effect
add_rounded_corners(entry_field)
add_rounded_corners(send_button)

# Run the application
root.mainloop()
