YouTube Video to Text Transcript Project

This Python project aims to convert YouTube videos into text transcripts using the Youtube Transcript Api Package. This README provides a guide on how to set up and use the project effectively.

Overview :-

The project utilizes Python scripts to interact with the YouTube API for video information retrieval and the Youtube Trancscript Api for converting video audio to text. The resulting transcript can be useful for content creators, researchers, or anyone who needs a textual representation of a YouTube video.

Prerequisites :-

Python Dependencies: Install the required Python package(youtube_transcript_api).

Package Installation :-
pip install -r requirements.txt

Configuration :-

Place your YouTube video id in vid_id variable in code.

Run the YouTube API Script:-

code.py --video_url <YouTube Video URL>
This script retrieves information about the video, including the video ID and summarizes video captions into text file by using 
regular expression package.

Output:-

The generated text transcript will be saved in the specified output file format (e.g., OUTPUT.TXT).

Notes:-

This project assumes a stable internet connection and proper API configuration.

Feel free to contribute, report issues, or suggest improvements. Happy transcribing!





