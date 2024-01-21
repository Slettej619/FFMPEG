import os
import subprocess

# Specify the directory containing the images and the output video file name
image_directory = r"D:\xxx\xxx\xxx_video_buffer"
output_video_file = r"D:\xxx\xxx\xxx-output_video.mp4"

# Construct the FFmpeg command
# Assuming the images are named in a sequence like 'frame_1.jpg', 'frame_2.jpg', etc.
ffmpeg_command = [
    "ffmpeg",
    "-framerate", "1",  # Set framerate to 1 frame per second
    "-i", os.path.join(image_directory, "frame_%d.jpg"),  # Input file pattern
    "-c:v", "libx264",  # Video codec
    "-pix_fmt", "yuv420p",  # Pixel format
    "-vf", "scale=1920:1080",  # Optional: scale images to 1920x1080
    output_video_file  # Output file
]

# Execute the FFmpeg command
subprocess.run(ffmpeg_command)
