import requests
from utils import *

filename = "example.wav"
audio_url = upload(filename)

save_transcript(audio_url, 'file_title')