from PyPDF2 import PdfReader
from gtts import gTTS
from langdetect import detect
text=""
text_language=""
def extract_text():
    reader=PdfReader("pdf-to-speech/siir.pdf")
    total_pages=len(reader.pages)
    global text
    for page_num in range(total_pages):
        page=reader.pages[page_num]
        text+=page.extract_text()
    print(text)

def lang_detect():
    global text_language
    text_language=detect(text)
    print(text_language)

def extract_speech():
    tts=gTTS(text, lang=text_language)
    tts.save("audio.mp3")

extract_text()
lang_detect()
extract_speech()
