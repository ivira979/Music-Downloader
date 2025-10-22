import streamlit as st
import subprocess
import os
import tempfile

st.title("Music Downloader")

song_name = st.text_input("Enter song name and artist:")

if st.button("Download"):
    if song_name:
        with st.spinner("Searching and downloading..."):
            try:
                # Create temp directory
                temp_dir = tempfile.mkdtemp()
                
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
                
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=temp_dir)
                
                if result.returncode == 0:
                    # Find the downloaded file
                    files = os.listdir(temp_dir)
                    if files:
                        file_path = os.path.join(temp_dir, files[0])
                        with open(file_path, "rb") as f:
                            audio_data = f.read()
                        
                        # Provide download button
                        st.success("Download ready!")
                        st.download_button(
                            label="Download Song",
                            data=audio_data,
                            file_name=files[0],
                            mime="audio/mpeg"
                        )
                        
                        # Cleanup
                        os.remove(file_path)
                        os.rmdir(temp_dir)
                    else:
                        st.error("No file was downloaded. Please try a different song name.")
                else:
                    st.error(f"Download failed: {result.stderr}")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a song name.")