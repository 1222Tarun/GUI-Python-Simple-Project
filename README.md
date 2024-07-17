<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>YouTube Video Downloader</h1>
        <p>This project is a simple and efficient YouTube Video Downloader built using Python, with a graphical user interface (GUI) created using Tkinter and CustomTkinter.</p>
        <h2>Features</h2>
        <ul>
            <li><strong>User-friendly Interface:</strong> Easy-to-use GUI designed with CustomTkinter.</li>
            <li><strong>Video Downloading:</strong> Supports downloading YouTube videos by URL.</li>
            <li><strong>Quality Selection:</strong> Allows selection of video quality before downloading.</li>
            <li><strong>Progress Bar:</strong> Displays download progress in real-time.</li>
            <li><strong>Error Handling:</strong> Gracefully handles errors such as invalid URLs or network issues.</li>
        </ul>
        <h2>Requirements</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Tkinter</li>
            <li>CustomTkinter</li>
            <li>Pytube (for handling YouTube downloads)</li>
        </ul>
        <h2>Installation</h2>
        <p>Clone the repository:</p>
        <pre>
<code>
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
</code>
        </pre>
        <p>Install the required dependencies:</p>
        <pre>
<code>
pip install -r requirements.txt
</code>
        </pre>
        <p>Run the application:</p>
        <pre>
<code>
python main.py
</code>
        </pre>
        <h2>Usage</h2>
        <ol>
            <li>Enter the YouTube video URL in the input field.</li>
            <li>Choose the desired video quality.</li>
            <li>Click the "Download" button to start the download.</li>
            <li>Monitor the progress through the progress bar.</li>
        </ol>
    </div>
</body>
</html>
