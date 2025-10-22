import streamlit as st
import subprocess
import os
import tempfile
import shutil

st.title("🎵 Freyr Music Downloader")
st.markdown("Download music from Spotify, Apple Music, Deezer, and more using freyr-js")

# URL input
url_input = st.text_area(
    "Enter music URLs (one per line)",
    placeholder="https://open.spotify.com/track/...\nhttps://music.apple.com/...",
    help="Paste URLs from Spotify, Apple Music, Deezer, Tidal, or other supported services"
)

# Download options
col1, col2 = st.columns(2)
with col1:
    bitrate = st.selectbox(
        "Audio Quality",
        ["320k", "256k", "192k", "160k", "128k", "96k"],
        index=0,
        help="Higher quality = larger file size"
    )

with col2:
    concurrent_downloads = st.slider(
        "Concurrent Downloads",
        min_value=1,
        max_value=10,
        value=3,
        help="Number of simultaneous downloads"
    )

# Download button
if st.button("🚀 Start Download", type="primary"):
    if not url_input.strip():
        st.error("Please enter at least one URL")
    else:
        urls = [url.strip() for url in url_input.split('\n') if url.strip()]

        with st.spinner("Initializing download..."):
            try:
                # Create temp directory
                temp_dir = tempfile.mkdtemp()

                # Prepare freyr command
                cmd = [
                    "freyr",
                    "--no-auth",
                    "--bitrate", bitrate,
                    "--chunks", str(concurrent_downloads),
                    "--yes"  # Non-interactive mode
                ] + urls

                # Show command being executed
                st.code(" ".join(cmd), language="bash")

                # Execute freyr
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
                        st.info("This might be due to service restrictions or invalid URLs.")
                else:
                    st.error(f"❌ Download failed with return code {return_code}")
                    st.code('\n'.join(output_lines[-20:]), language="text")

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
**Supported Services:**
- Spotify
- Apple Music
- Deezer
- Tidal
- YouTube Music
- And more...

**Note:** Some services may have download restrictions. Make sure you have permission to download the content.
""")