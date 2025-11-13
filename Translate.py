from tkinter import *
from googletrans import Translator

def translate_text():
    text = input_text.get("1.0", END).strip()
    if text:
        translator = Translator()
        translated = translator.translate(text, src='en', dest='es')
        output_text.delete("1.0", END)
        output_text.insert(END, translated.text)

# Main window
root = Tk()
root.title("English to Spanish Translator")
root.geometry("400x300")
root.resizable(False, False)
root.config(bg="#f0f0f0")

# Labels
Label(root, text="Enter English text:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
input_text = Text(root, height=4, width=45)
input_text.pack(pady=5)

Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 10)).pack(pady=5)

Label(root, text="Spanish translation:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
output_text = Text(root, height=4, width=45)
output_text.pack(pady=5)

root.mainloop()
