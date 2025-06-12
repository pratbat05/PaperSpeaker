import os
from typing import Optional
from PyPDF2 import PdfReader
from gtts import gTTS
import nltk
from nltk.tokenize import sent_tokenize
from dotenv import load_dotenv
import magic
from bs4 import BeautifulSoup
import requests

class PaperSpeaker:
    def __init__(self, language: str = 'en', voice_speed: float = 1.0):
      
        self.language = language
        self.voice_speed = voice_speed
        
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

    def extract_text_from_pdf(self, file_path: str) -> str:
    
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Verify if file is PDF
        file_type = magic.from_file(file_path, mime=True)
        if file_type != 'application/pdf':
            raise ValueError(f"File is not a PDF: {file_path}")
        
        reader = PdfReader(file_path)
        text = ""
        
        for page in reader.pages:
            text += page.extract_text() + "\n"
            
        return text.strip()

    def process_text(self, text: str) -> str:
    
        sentences = sent_tokenize(text)
        
        cleaned_sentences = [' '.join(sentence.split()) for sentence in sentences]
        return ' '.join(cleaned_sentences)

    def convert_to_audio(self, text: str, output_path: str) -> None:

        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(output_path)

    def process_paper(self, input_path: str, output_path: Optional[str] = None) -> str:
    
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.mp3'

        
        text = self.extract_text_from_pdf(input_path)
   
        processed_text = self.process_text(text)
       
        self.convert_to_audio(processed_text, output_path)
        
        return output_path

    def process_url(self, url: str, output_path: Optional[str] = None) -> str:
      
        if output_path is None:
            output_path = "paper_audio.mp3"
     
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        

        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        processed_text = self.process_text(text)
        

        self.convert_to_audio(processed_text, output_path)
        
        return output_path 
