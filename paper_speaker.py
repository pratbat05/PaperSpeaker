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
        """
        Initialize the PaperSpeaker agent.
        
        Args:
            language (str): Language code for text-to-speech (default: 'en')
            voice_speed (float): Speed of the voice output (default: 1.0)
        """
        self.language = language
        self.voice_speed = voice_speed
        
        # Download required NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

    def extract_text_from_pdf(self, file_path: str) -> str:
        """
        Extract text content from a PDF file.
        
        Args:
            file_path (str): Path to the PDF file
            
        Returns:
            str: Extracted text content
        """
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
        """
        Process and clean the extracted text.
        
        Args:
            text (str): Raw text content
            
        Returns:
            str: Processed text
        """
        # Split text into sentences
        sentences = sent_tokenize(text)
        
        # Remove extra whitespace and join sentences
        cleaned_sentences = [' '.join(sentence.split()) for sentence in sentences]
        return ' '.join(cleaned_sentences)

    def convert_to_audio(self, text: str, output_path: str) -> None:
        """
        Convert text to audio using gTTS.
        
        Args:
            text (str): Text to convert to speech
            output_path (str): Path to save the audio file
        """
        tts = gTTS(text=text, lang=self.language, slow=False)
        tts.save(output_path)

    def process_paper(self, input_path: str, output_path: Optional[str] = None) -> str:
        """
        Process a research paper and convert it to audio.
        
        Args:
            input_path (str): Path to the input PDF file
            output_path (str, optional): Path to save the audio file
            
        Returns:
            str: Path to the generated audio file
        """
        if output_path is None:
            output_path = os.path.splitext(input_path)[0] + '.mp3'

        # Extract text from PDF
        text = self.extract_text_from_pdf(input_path)
        
        # Process and clean the text
        processed_text = self.process_text(text)
        
        # Convert to audio
        self.convert_to_audio(processed_text, output_path)
        
        return output_path

    def process_url(self, url: str, output_path: Optional[str] = None) -> str:
        """
        Process a research paper from a URL and convert it to audio.
        
        Args:
            url (str): URL of the research paper
            output_path (str, optional): Path to save the audio file
            
        Returns:
            str: Path to the generated audio file
        """
        if output_path is None:
            output_path = "paper_audio.mp3"

        # Fetch content from URL
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract main text content (this might need customization based on the website structure)
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        # Process and clean the text
        processed_text = self.process_text(text)
        
        # Convert to audio
        self.convert_to_audio(processed_text, output_path)
        
        return output_path 