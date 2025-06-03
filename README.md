# PaperSpeaker

PaperSpeaker is a Python-based agent that converts research papers (PDF files or URLs) into audiobooks. It provides an easy way to listen to academic papers and research content.

## Features

- Convert PDF research papers to audio files
- Process research papers from URLs
- Clean and process text for better audio output
- Support for multiple languages
- Customizable voice speed
- PDF validation and error handling

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/PaperSpeaker.git
cd PaperSpeaker
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from paper_speaker import PaperSpeaker

# Initialize the agent
speaker = PaperSpeaker(language='en')

# Convert a PDF file to audio
output_path = speaker.process_paper(
    input_path="path/to/your/paper.pdf",
    output_path="output_audio.mp3"
)

# Convert a paper from URL
output_path = speaker.process_url(
    url="https://example.com/research-paper",
    output_path="url_paper_audio.mp3"
)
```

### Example Script

Check out `example.py` for a complete usage example.

## Configuration

- `language`: Specify the language code (default: 'en')
- `voice_speed`: Adjust the speech rate (default: 1.0)

## Requirements

- Python 3.7+
- See `requirements.txt` for all dependencies

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 