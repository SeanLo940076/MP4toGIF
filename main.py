# import the necessary module
from moviepy.editor import *

# load the video
clip = VideoFileClip("Demo.mp4")

# getting only 10 seconds from video
clip = clip.subclip(1, 10)
clip = clip.resize((640, 480))

# save the video clip as gif
#clip.write_gif("KITTI_0407.gif")
clip.write_gif('Demo.gif', fps=30, opt='fast', fuzz=10)
