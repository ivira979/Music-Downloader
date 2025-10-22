# Music Downloader

A Streamlit-based application that allows users to download music by entering a song name. The app searches YouTube for the song and downloads the audio as MP3.

## Requirements

- Python 3.7+
- ffmpeg (for audio extraction)

## Installation

1. Clone or download this repository.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install ffmpeg:
   - On macOS: `brew install ffmpeg`
   - On Ubuntu/Debian: `sudo apt install ffmpeg`
   - On Windows: Download from https://ffmpeg.org/download.html

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

Open the provided URL in your browser, enter a song name, and click "Download". Once the download is ready, click the "Download Song" button to save the MP3 file.

## Note

- The app downloads the first YouTube search result for the song name.
- Downloads are temporary and cleaned up after providing the file.
- Ensure you have permission to download and use the content.