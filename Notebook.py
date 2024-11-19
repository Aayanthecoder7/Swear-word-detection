from tkinter import *
from tkinter import messagebox
import re

root = Tk()
root.geometry("400x200")
root.config(background="Black")
root.title("Swear Word Detector")

# GUI Elements
drag_label = Label(root, text="Enter Text File Name (with extension):", bg="Black", fg="White", font=("Arial", 14))
drag_label.pack(pady=10)

get_text = Entry(root, width=40)
get_text.pack(pady=10)

swear_words = [
    "arse", "arsehead", "arsehole", "ass", "asshole", "bastard", "bitch",
    "bloody", "bollocks", "bugger", "bullshit", "cock", "cocksucker", "crap", 
    "cunt", "damn", "dick", "dumbass", "faggot", "fuck", "fucker", "hell", 
    "nigga", "piss", "prick", "pussy", "shit", "slut", "twat", "wanker"
]

# Function to process the file
def check_swear_words():
    file_name = get_text.get()
    if not file_name:
        messagebox.showerror("Error", "Please enter a file name!")
        return

    try:
        # Read the file
        with open(file_name, "r") as file:
            text = file.read()
        
        # Detect swear words
        flagged_words = set()
        for word in swear_words:
            # Case-insensitive full word match
            if re.search(rf"\b{word}\b", text, re.IGNORECASE):
                flagged_words.add(word)
        
        if flagged_words:
            print(f"Swear words detected: {', '.join(flagged_words)}")
            messagebox.showinfo("Result", f"Swear words detected: {', '.join(flagged_words)}")
        else:
            print("No swear words detected.")
            messagebox.showinfo("Result", "No swear words detected.")
    
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please check the file name.")

# Button to trigger the checking process
check_button = Button(root, text="Check File", command=check_swear_words, bg="White", fg="Black")
check_button.pack(pady=20)

root.mainloop()
