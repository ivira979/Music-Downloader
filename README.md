# 🎵 Freyr Music Downloader# 🎵 Freyr Music Downloader# Music Downloader



A Streamlit web interface for [freyr-js](https://github.com/miraclx/freyr-js), inspired by [freyr-gui](https://github.com/miraclx/freyr-gui).



Download high-quality music from Spotify, Apple Music, Deezer, Tidal, and other supported services.A Streamlit web interface for [freyr-js](https://github.com/miraclx/freyr-js), inspired by [freyr-gui](https://github.com/miraclx/freyr-gui).A Streamlit-based application that allows users to download music by entering a song name. The app searches YouTube for the song and downloads the audio as MP3.



## Features



- 🎯 **Multiple Service Support**: Spotify, Apple Music, Deezer, Tidal, YouTube Music, and moreDownload high-quality music from Spotify, Apple Music, Deezer, Tidal, and other supported services.## Requirements

- 🎵 **High-Quality Audio**: Choose bitrate from 96k to 320k

- ⚡ **Concurrent Downloads**: Control the number of simultaneous downloads

- 📊 **Real-time Progress**: Live progress updates and command output

- 💾 **Direct Download**: Download files directly from your browser## Features- Python 3.7+



## Installation- ffmpeg (for audio extraction)



1. Install Python dependencies:- 🎯 **Multiple Service Support**: Spotify, Apple Music, Deezer, Tidal, YouTube Music, and more- Node.js and npm (for freyr-js support)

   ```bash

   pip install -r requirements.txt- 🎵 **High-Quality Audio**: Choose bitrate from 96k to 320k

   ```

- ⚡ **Concurrent Downloads**: Control the number of simultaneous downloads## Installation

2. Install Node.js from [nodejs.org](https://nodejs.org/)

- 📊 **Real-time Progress**: Live progress updates and command output

3. Install freyr-js globally:

   ```bash- 💾 **Direct Download**: Download files directly from your browser1. Clone or download this repository.

   npm install -g freyr

   ```2. Install Python dependencies:



## Usage## Installation   ```



Run the Streamlit app:   pip install -r requirements.txt

```bash

streamlit run app.py1. Install Python dependencies:   ```

```

   ```bash3. Install system dependencies:

1. **Enter URLs**: Paste music URLs (one per line) from supported services

2. **Configure Options**:   pip install -r requirements.txt   - ffmpeg:

   - Choose audio quality (bitrate)

   - Set concurrent download limit   ```     - On macOS: `brew install ffmpeg`

3. **Start Download**: Click the download button

4. **Monitor Progress**: Watch real-time progress and output     - On Ubuntu/Debian: `sudo apt install ffmpeg`

5. **Download Files**: Click download buttons for each completed track

2. Install Node.js from [nodejs.org](https://nodejs.org/)     - On Windows: Download from https://ffmpeg.org/download.html

## Supported Services

   - Node.js: Download from https://nodejs.org/

- **Spotify**: No authentication required

- **Apple Music**: May require authentication (experimental support)3. Install freyr-js globally:4. Install freyr-js globally:

- **Deezer**: No authentication required

- **Tidal**: May require authentication   ```bash   ```

- **YouTube Music**: No authentication required

- **SoundCloud**: No authentication required   npm install -g freyr   npm install -g freyr

- And many more...

   ```   ```

## Authentication



Some services require authentication:

- **Apple Music**: Currently experimental in freyr-js## Usage## Usage

- **Tidal**: Requires account credentials



For services that require authentication, freyr-js may prompt for login credentials or use stored credentials.

Run the Streamlit app:Run the Streamlit app:

## Note

```bash```

Some services may have download restrictions. Make sure you have permission to download the content you're accessing.
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