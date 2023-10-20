from PyPDF2 import PdfReader
from gtts import gTTS
from langdetect import detect
import tkinter as tk
from tkinter import filedialog

text = ""
text_language = ""
file_path = ""

root = tk.Tk()
root.geometry("700x800")
root.title("Extract Speech")
file_frame = tk.Frame(root)
file_frame.pack()

def browse_files():
    global file_path
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
    print(file_path)
    if file_path:
        extract_text()
        lang_detect()
        extract_speech()
        show_text()

def extract_text():
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    global text
    text = ""
    for page_num in range(total_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    print(text)

def lang_detect():
    global text_language
    text_language = detect(text)
    print(text_language)

def extract_speech():
    tts = gTTS(text, lang=text_language)
    tts.save("audio.mp3")

def show_text():
    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.insert("1.0", text)
    text_widget.pack(fill=tk.BOTH, expand=True)

    scroll_y = tk.Scrollbar(root, command=text_widget.yview)
    text_widget.config(yscrollcommand=scroll_y.set)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

file_button = tk.Button(file_frame, text="Choose the PDF", borderwidth=0, command=browse_files)
file_button.pack(pady=50)

root.mainloop()
