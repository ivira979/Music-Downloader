# Music Downloader

A Streamlit-based application that allows users to download music by entering a song name. The app searches YouTube for the song and downloads the audio as MP3.

## Requirements

- Python 3.7+
- ffmpeg (for audio extraction)
- Node.js and npm (for freyr-js support)

## Installation

1. Clone or download this repository.
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install system dependencies:
   - ffmpeg:
     - On macOS: `brew install ffmpeg`
     - On Ubuntu/Debian: `sudo apt install ffmpeg`
     - On Windows: Download from https://ffmpeg.org/download.html
   - Node.js: Download from https://nodejs.org/
4. Install freyr-js globally:
   ```
   npm install -g freyr
   ```

## Usage

Run the Streamlit app:
```
streamlit run app.py
```

Open the provided URL in your browser. Select your preferred download method:
- **yt-dlp (YouTube)**: Downloads from YouTube search results
- **freyr-js (Multiple sources)**: Downloads from various music services (Spotify, Apple Music, etc.)

Enter a song name and artist, then click "Download". Once the download is ready, click the "Download Song" button to save the MP3 file.

## Deployment on Streamlit Community Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account and select this repository.
4. Set the main file path to `app.py`
5. Click Deploy.

The app includes:
- `requirements.txt`: Python dependencies
- `packages.txt`: System dependencies (ffmpeg)
- `runtime.txt`: Python version specification

## Note

- **yt-dlp**: Downloads the first YouTube search result for the song name.
- **freyr-js**: Supports multiple music services. For best results, you may need to provide URLs from supported services, though queries should work for basic searches.
- Downloads are temporary and cleaned up after providing the file.
- Ensure you have permission to download and use the content.