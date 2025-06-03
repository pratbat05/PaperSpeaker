from paper_speaker import PaperSpeaker

def main():
    # Initialize the PaperSpeaker agent
    speaker = PaperSpeaker(language='en')
    
    # Example 1: Convert a PDF file to audio
    try:
        output_path = speaker.process_paper(
            input_path="example_paper.pdf",
            output_path="paper_audio.mp3"
        )
        print(f"Audio file generated successfully: {output_path}")
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
    
    # Example 2: Convert a research paper URL to audio
    try:
        output_path = speaker.process_url(
            url="https://example.com/research-paper",
            output_path="url_paper_audio.mp3"
        )
        print(f"Audio file generated successfully from URL: {output_path}")
    except Exception as e:
        print(f"Error processing URL: {str(e)}")

if __name__ == "__main__":
    main() 