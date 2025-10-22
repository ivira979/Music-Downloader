# 🎵 Music Downloader# 🎵 Freyr Music Downloader# 🎵 Freyr Music Downloader# Music Downloader



A Streamlit web interface for downloading music from YouTube and other sources using yt-dlp.



Download high-quality music with an intuitive interface inspired by freyr-gui.A Streamlit web interface for [freyr-js](https://github.com/miraclx/freyr-js), inspired by [freyr-gui](https://github.com/miraclx/freyr-gui).



## Features



- 🎯 **Multiple Input Methods**: YouTube URLs, search terms, music service URLsDownload high-quality music from Spotify, Apple Music, Deezer, Tidal, and other supported services.A Streamlit web interface for [freyr-js](https://github.com/miraclx/freyr-js), inspired by [freyr-gui](https://github.com/miraclx/freyr-gui).A Streamlit-based application that allows users to download music by entering a song name. The app searches YouTube for the song and downloads the audio as MP3.

- 🎵 **High-Quality Audio**: Choose from MP3, M4A, FLAC, WAV formats

- ⚡ **Quality Selection**: 128k to 320k bitrate options

- 📊 **Real-time Progress**: Live progress updates and command output

- 💾 **Direct Download**: Download files directly from your browser## Features



## Installation



1. Install Python dependencies:- 🎯 **Multiple Service Support**: Spotify, Apple Music, Deezer, Tidal, YouTube Music, and moreDownload high-quality music from Spotify, Apple Music, Deezer, Tidal, and other supported services.## Requirements

   ```bash

   pip install -r requirements.txt- 🎵 **High-Quality Audio**: Choose bitrate from 96k to 320k

   ```

- ⚡ **Concurrent Downloads**: Control the number of simultaneous downloads

2. Install FFmpeg (required for audio extraction):

   ```bash- 📊 **Real-time Progress**: Live progress updates and command output

   # macOS

   brew install ffmpeg- 💾 **Direct Download**: Download files directly from your browser## Features- Python 3.7+



   # Ubuntu/Debian

   sudo apt install ffmpeg

## Installation- ffmpeg (for audio extraction)

   # Windows: Download from https://ffmpeg.org/

   ```



## Usage1. Install Python dependencies:- 🎯 **Multiple Service Support**: Spotify, Apple Music, Deezer, Tidal, YouTube Music, and more- Node.js and npm (for freyr-js support)



Run the Streamlit app:   ```bash

```bash

streamlit run app.py   pip install -r requirements.txt- 🎵 **High-Quality Audio**: Choose bitrate from 96k to 320k

```

   ```

### Input Methods

- ⚡ **Concurrent Downloads**: Control the number of simultaneous downloads## Installation

1. **YouTube URL**: Paste direct YouTube video URLs

   - Most reliable method2. Install Node.js from [nodejs.org](https://nodejs.org/)

   - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

- 📊 **Real-time Progress**: Live progress updates and command output

2. **Search Term**: Enter song/artist names

   - Searches YouTube automatically3. Install freyr-js globally:

   - Example: `Never Gonna Give You Up`

   ```bash- 💾 **Direct Download**: Download files directly from your browser1. Clone or download this repository.

3. **Music Service URL**: URLs from Spotify, Apple Music, etc.

   - May have limitations due to service restrictions   npm install -g freyr

   - Example: `https://open.spotify.com/track/...`

   ```2. Install Python dependencies:

### Audio Options



- **Format**: MP3 (compatible), M4A (efficient), FLAC (lossless), WAV (uncompressed)

- **Quality**: 128k, 192k, 256k, 320k bitrate## Usage## Installation   ```



## How It Works



1. **Input Processing**: Accepts YouTube URLs, search terms, or music service URLsRun the Streamlit app:   pip install -r requirements.txt

2. **YouTube Search**: Converts search terms to YouTube queries

3. **Download**: Uses yt-dlp with optimized settings for reliable downloads```bash

4. **Audio Extraction**: Converts video to selected audio format

5. **File Serving**: Provides direct download links in your browserstreamlit run app.py1. Install Python dependencies:   ```



## Troubleshooting```



### Common Issues   ```bash3. Install system dependencies:



- **403 Forbidden**: YouTube blocking - the app includes bypass measures1. **Enter URLs**: Paste music URLs (one per line) from supported services

- **No audio file**: Check URL validity or try a different input method

- **Slow downloads**: Reduce concurrent downloads or try different quality2. **Configure Options**:   pip install -r requirements.txt   - ffmpeg:



### For Music Service URLs   - Choose audio quality (bitrate)



Some music service URLs (Spotify, Apple Music) may not work due to:   - Set concurrent download limit   ```     - On macOS: `brew install ffmpeg`

- Service authentication requirements

- Content licensing restrictions3. **Start Download**: Click the download button

- Platform-specific limitations

4. **Monitor Progress**: Watch real-time progress and output     - On Ubuntu/Debian: `sudo apt install ffmpeg`

For best results, use direct YouTube URLs or search terms.

5. **Download Files**: Click download buttons for each completed track

## Technical Details

2. Install Node.js from [nodejs.org](https://nodejs.org/)     - On Windows: Download from https://ffmpeg.org/download.html

- Built with Streamlit for the web interface

- Uses yt-dlp for robust YouTube downloading## Supported Services

- FFmpeg for high-quality audio extraction

- Real-time progress monitoring   - Node.js: Download from https://nodejs.org/

- Automatic cleanup of temporary files

- **Spotify**: No authentication required

## Note

- **Apple Music**: May require authentication (experimental support)3. Install freyr-js globally:4. Install freyr-js globally:

Make sure you have permission to download and use the content. This tool is for personal use with content you have rights to access.
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