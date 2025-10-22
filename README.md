# 🎵 Freyr Music Downloader# Music Downloader



A Streamlit web interface for [freyr-js](https://github.com/miraclx/freyr-js), inspired by [freyr-gui](https://github.com/miraclx/freyr-gui).A Streamlit-based application that allows users to download music by entering a song name. The app searches YouTube for the song and downloads the audio as MP3.



Download high-quality music from Spotify, Apple Music, Deezer, Tidal, and other supported services.## Requirements



## Features- Python 3.7+

- ffmpeg (for audio extraction)

- 🎯 **Multiple Service Support**: Spotify, Apple Music, Deezer, Tidal, YouTube Music, and more- Node.js and npm (for freyr-js support)

- 🎵 **High-Quality Audio**: Choose bitrate from 96k to 320k

- ⚡ **Concurrent Downloads**: Control the number of simultaneous downloads## Installation

- 📊 **Real-time Progress**: Live progress updates and command output

- 💾 **Direct Download**: Download files directly from your browser1. Clone or download this repository.

2. Install Python dependencies:

## Installation   ```

   pip install -r requirements.txt

1. Install Python dependencies:   ```

   ```bash3. Install system dependencies:

   pip install -r requirements.txt   - ffmpeg:

   ```     - On macOS: `brew install ffmpeg`

     - On Ubuntu/Debian: `sudo apt install ffmpeg`

2. Install Node.js from [nodejs.org](https://nodejs.org/)     - On Windows: Download from https://ffmpeg.org/download.html

   - Node.js: Download from https://nodejs.org/

3. Install freyr-js globally:4. Install freyr-js globally:

   ```bash   ```

   npm install -g freyr   npm install -g freyr

   ```   ```



## Usage## Usage



Run the Streamlit app:Run the Streamlit app:

```bash```

streamlit run app.pystreamlit run app.py

``````



1. **Enter URLs**: Paste music URLs (one per line) from supported servicesOpen the provided URL in your browser. Select your preferred download method:

2. **Configure Options**:- **yt-dlp (YouTube)**: Enter a song name/artist for YouTube search and download

   - Choose audio quality (bitrate)- **freyr-js (Multiple sources)**: Enter a URL from supported music services (Spotify, Apple Music, Deezer, Tidal, etc.) for high-quality downloads

   - Set concurrent download limit

3. **Start Download**: Click the download buttonThen click "Download". Once the download is ready, click the "Download Song" button to save the MP3 file.

4. **Monitor Progress**: Watch real-time progress and output

5. **Download Files**: Click download buttons for each completed track## Deployment on Streamlit Community Cloud



## Supported Services1. Push this repository to GitHub.

2. Go to [share.streamlit.io](https://share.streamlit.io)

- Spotify (tracks, albums, playlists)3. Connect your GitHub account and select this repository.

- Apple Music4. Set the main file path to `app.py`

- Deezer5. Click Deploy.

- Tidal

- YouTube MusicThe app includes:

- SoundCloud- `requirements.txt`: Python dependencies

- And many more...- `packages.txt`: System dependencies (ffmpeg)

- `runtime.txt`: Python version specification

## Note

## Note

Some services may have download restrictions or require authentication. Make sure you have permission to download the content you're accessing.
- **yt-dlp**: Downloads the first YouTube search result for the song name/artist query.
- **freyr-js**: Requires URLs from supported music services. Plain text searches are not supported. Supported services include Spotify, Apple Music, Deezer, Tidal, and more. Note: freyr-js may also encounter YouTube download restrictions similar to yt-dlp.
- Downloads are temporary and cleaned up after providing the file.
- Ensure you have permission to download and use the content.