import streamlit as st
import subprocess
import os
import tempfile

st.title("Music Downloader")

download_method = st.selectbox("Choose download method:", ["yt-dlp (YouTube)", "freyr-js (Multiple sources)"])

if download_method == "freyr-js (Multiple sources)":
    st.info("💡 For freyr-js, please provide a URL from supported music services (Spotify, Apple Music, Deezer, etc.)")
    
song_name = st.text_input("Enter song name/artist (yt-dlp) or URL (freyr-js):")

if download_method == "freyr-js (Multiple sources)" and song_name and not song_name.startswith(('http://', 'https://')):
    st.warning("⚠️ freyr-js requires a URL starting with http:// or https://")

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
                    # Run freyr in the temp directory so it saves files there
                    cmd = [
                        "freyr",
                        song_name,
                        "--no-auth"
                    ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=temp_dir)
                
                if result.returncode == 0:
                    # Find the downloaded file(s) - check for various audio formats
                    audio_files = []
                    audio_extensions = ['.mp3', '.m4a', '.flac', '.wav', '.aac', '.ogg']
                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            if any(file.lower().endswith(ext) for ext in audio_extensions):
                                audio_files.append(os.path.join(root, file))
                    
                    if audio_files:
                        # Use the first audio file found
                        file_path = audio_files[0]
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
                        # Debug: list all files in temp_dir
                        all_files = []
                        for root, dirs, files in os.walk(temp_dir):
                            for file in files:
                                all_files.append(os.path.join(root, file))
                        error_msg = "No audio file found."
                        if "403" in result.stderr or "Forbidden" in result.stderr:
                            error_msg += " This appears to be due to YouTube blocking the download (same issue affects both methods)."
                        st.error(f"{error_msg}\nCommand run: {' '.join(cmd)}\nFreyr stderr: {result.stderr}\nFreyr stdout: {result.stdout}\nAll files created: {all_files}")
                else:
                    st.error(f"Download failed: {result.stderr}")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a song name.")