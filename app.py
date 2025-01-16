from flask import Flask, render_template, request, send_file
import os
import yt_dlp
import re

app = Flask(__name__)
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

def is_valid_youtube_url(url):
    youtube_regex = (
        r"^(https?://)?(www\.)?"
        r"(youtube\.com|youtu\.?be)/.+$"
    )
    return re.match(youtube_regex, url)

def download_video(url, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(result)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    if not is_valid_youtube_url(url):
        return render_template('index.html', error="Invalid YouTube URL.")
    try:
        filepath = download_video(url, download_folder)
        return send_file(filepath, as_attachment=True)
    except Exception as e:
        return render_template('index.html', error=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)
