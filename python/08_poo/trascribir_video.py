import pytube
import whisper

youtube_url = 'https://www.youtube.com/watch?v=J-hjMWej4f0'

youtube_video = pytube.YouTube(youtube_url)

audio = youtube_video.streams.get_audio_only()
audio.download(file_name='tmp.mp4')

model = whisper.load_model('small')
result = model.transcribe('tmp.mp4')

print (result["text"])
