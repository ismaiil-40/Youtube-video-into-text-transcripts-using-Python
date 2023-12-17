from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
#https://www.youtube.com/watch?v=1aA1WGON49E
vid_id = 'hEgO047GxaQ'
data = yta.get_transcript(vid_id)
transcript = ''
for value in data:
    for key,val in value.items():
        if key == 'text':
            transcript += val
l = transcript.splitlines()
final_tra = " ".join(l)
file = open("sam1.txt",'w')
file.write(final_tra)
file.close()
