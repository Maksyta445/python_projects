import pdfplumber
from gtts import gTTS


def get_text_computer():
    pages_pdf_text = []
    with pdfplumber.open("first_computer_history.pdf") as pdf:
        for page in pdf.pages:
            pages_text = page.extract_text()
            pages_pdf_text.append(pages_text)  
        pdf_text = "".join(pages_pdf_text) 
        text_replace = pdf_text.replace("\n", " ")
    return text_replace  


def get_audio_file(text):
    phrase = gTTS(text=text, lang="ru", slow=False) 
    phrase.save("audio_first_computer.mp3")


def main(): 
    get_audio_file(get_text_computer())  


if __name__ == "__main__":  
    main()