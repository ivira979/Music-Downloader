import streamlit as st
import subprocess
import os
import tempfile
import shutil

st.title("🎵 Music Downloader")
st.markdown("Download music from YouTube, Spotify, Apple Music, Deezer, and more")

# Service info
st.info("💡 **Supported Sources:**\n"
        "- YouTube URLs\n"
        "- YouTube search terms\n"
        "- Other music service URLs (may have limitations)")

# Input method selection
input_method = st.radio(
    "Choose input method:",
    ["YouTube URL", "Search term", "Music service URL"],
    horizontal=True
)

# Input field
if input_method == "YouTube URL":
    user_input = st.text_input("Enter YouTube URL:", placeholder="https://www.youtube.com/watch?v=...")
elif input_method == "Search term":
    user_input = st.text_input("Enter song/artist name:", placeholder="Never Gonna Give You Up")
else:  # Music service URL
    user_input = st.text_input("Enter music service URL:", placeholder="https://open.spotify.com/track/...")
    st.warning("⚠️ Music service URLs may not work due to download restrictions")

# Download options
col1, col2 = st.columns(2)
with col1:
    audio_format = st.selectbox(
        "Audio Format",
        ["mp3", "m4a", "flac", "wav"],
        index=0,
        help="MP3 is most compatible, FLAC is highest quality"
    )

with col2:
    audio_quality = st.selectbox(
        "Audio Quality",
        ["128k", "192k", "256k", "320k"],
        index=3,
        help="Higher quality = larger file size"
    )

# Download button
if st.button("🚀 Start Download", type="primary"):
    if not user_input.strip():
        st.error("Please enter a URL or search term")
    else:
        with st.spinner("Searching and downloading..."):
            try:
                # Create temp directory
                temp_dir = tempfile.mkdtemp()

                # Prepare yt-dlp command
                if input_method == "Search term":
                    # Search YouTube
                    query = f"ytsearch1:{user_input}"
                else:
                    # Direct URL
                    query = user_input

                cmd = [
                    "yt-dlp",
                    "-x",  # Extract audio
                    "--audio-format", audio_format,
                    "--audio-quality", audio_quality,
                    "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                    "--referer", "https://www.youtube.com/",
                    "--no-check-certificates",
                    "--extractor-args", "youtube:player_client=android",
                    "-o", f"{temp_dir}/%(title)s.%(ext)s",
                    query
                ]

                # Execute yt-dlp
                process = subprocess.Popen(
                    cmd,
                    cwd=temp_dir,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True,
                    bufsize=1,
                    universal_newlines=True
                )

                # Progress display
                progress_bar = st.progress(0)
                status_text = st.empty()
                output_area = st.empty()

                output_lines = []
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        output_lines.append(output.strip())
                        output_area.code('\n'.join(output_lines[-10:]))  # Show last 10 lines

                        # Try to extract progress info
                        if '%' in output:
                            try:
                                # Look for percentage in output
                                for word in output.split():
                                    if word.endswith('%'):
                                        percent = float(word.rstrip('%'))
                                        progress_bar.progress(min(percent / 100, 1.0))
                                        break
                            except:
                                pass

                return_code = process.poll()

                if return_code == 0:
                    # Find downloaded files
                    audio_files = []
                    audio_extensions = ['.mp3', '.m4a', '.flac', '.wav', '.aac', '.ogg']

                    for root, dirs, files in os.walk(temp_dir):
                        for file in files:
                            if any(file.lower().endswith(ext) for ext in audio_extensions):
                                audio_files.append(os.path.join(root, file))

                    if audio_files:
                        st.success(f"✅ Download completed! Found {len(audio_files)} audio file(s)")

                        # Show download links
                        for file_path in audio_files:
                            file_name = os.path.basename(file_path)
                            with open(file_path, "rb") as f:
                                file_data = f.read()

                            st.download_button(
                                label=f"📥 Download {file_name}",
                                data=file_data,
                                file_name=file_name,
                                mime="audio/mpeg"
                            )

                        # Cleanup
                        shutil.rmtree(temp_dir)
                    else:
                        st.error("❌ No audio files were created. Check the output above for errors.")
                        st.info("This might be due to URL issues or service restrictions.")
                else:
                    st.error(f"❌ Download failed with return code {return_code}")
                    st.code('\n'.join(output_lines[-20:]), language="text")

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Supported Input Methods:**
- **YouTube URL**: Direct video URLs (most reliable)
- **Search term**: Song/artist name (searches YouTube)
- **Music service URL**: Spotify, Apple Music, etc. (may not work)

**Audio Formats:**
- MP3: Most compatible
- M4A: Good quality, smaller files
- FLAC: Lossless quality
- WAV: Uncompressed
""")