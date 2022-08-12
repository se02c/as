#by omar
#Telegram >> @toolsegy

import pytube
import time

urrl = input('paste link vid : ')
pytube.YouTube(urrl).streams.get_highest_resolution().download("Youtube Videos")
print('Wait ..')
sleep.time(13)
print("Done ..\nGo to your desktop !!")