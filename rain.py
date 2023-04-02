#Import MoviePy Library
from moviepy.editor import *

#Read The Rain/Sound Clips
rain_clip = VideoFileClip("")
rain_sound = AudioFileClip("")
# Add the number of clips you wanna make
number_clips = 5

#Concatenate Rain/Sound Clips
rain_clip = concatenate_videoclips([rain_clip for i in range(number_clips)])
rain_sound = concatenate_audioclips([rain_sound for i in range(number_clips)])

#Set Duration Time of the rain_sound to the rain_clip
rain_sound = rain_sound.set_duration(rain_clip.duration)

#Exporting The Final Clip
final_clip = rain_clip.set_audio(rain_sound)
final_clip.write_videofile("", threads = 8, fps=15, preset='ultrafast')