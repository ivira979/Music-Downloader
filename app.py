import streamlit as st
import subprocess
import os
import tempfile

st.title("Music Downloader")

download_method = st.selectbox("Choose download method:", ["yt-dlp (YouTube)", "freyr-js (Multiple sources)"])

if download_method == "freyr-js (Multiple sources)":
    st.info("💡 For freyr-js, please provide a URL from supported music services (Spotify, Apple Music, Deezer, etc.)")
    
song_name = st.text_input("Enter song name/artist (yt-dlp) or URL (freyr-js):")

if st.button("Download"):
    if song_name:
        method_name = "YouTube" if "yt-dlp" in download_method else "multiple sources"
        with st.spinner(f"Searching and downloading from {method_name}..."):
            try:
                # Create temp directory
                temp_dir = tempfile.mkdtemp()
                
                if download_method == "yt-dlp (YouTube)":
                    # yt-dlp command to search and download audio
                    cmd = [
                        "yt-dlp",
                        "-x",  # Extract audio
                        "--audio-format", "mp3",
                        "--audio-quality", "192K",
                        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                        "--referer", "https://www.youtube.com/",
                        "--no-check-certificates",
                        "--extractor-args", "youtube:player_client=android",
                        "-o", f"{temp_dir}/%(title)s.%(ext)s",
                        f"ytsearch1:{song_name}"  # Search for first result
                    ]
                else:  # freyr-js
                    # freyr command to download from multiple sources
                    cmd = [
                        "freyr",
                        "get",
                        song_name,
                        "--no-auth",
                        "--directory", temp_dir
                    ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=temp_dir)
                
                if result.returncode == 0:
                    # Find the downloaded file(s)
                    mp3_files = []
                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            if file.endswith('.mp3'):
                                mp3_files.append(os.path.join(root, file))
                    
                    if mp3_files:
                        # Use the first MP3 file found
                        file_path = mp3_files[0]
                        file_name = os.path.basename(file_path)
                        with open(file_path, "rb") as f:
                            audio_data = f.read()
                        
                        # Provide download button
                        st.success("Download ready!")
                        st.download_button(
                            label="Download Song",
                            data=audio_data,
                            file_name=file_name,
                            mime="audio/mpeg"
                        )
                        
                        # Cleanup - remove all files and directories
                        import shutil
                        shutil.rmtree(temp_dir)
                    else:
                        st.error("No file was downloaded. Please try a different song name.")
                else:
                    st.error(f"Download failed: {result.stderr}")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a song name.")