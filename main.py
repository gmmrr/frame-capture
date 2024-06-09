import os
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np



def capture_frames(video_path, start_time, end_time, output_folder):
    clip = VideoFileClip(video_path)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    time_points = np.arange(start_time, end_time, (end_time - start_time)/300)

    counter = 0
    for t in time_points:
        frame = clip.get_frame(t)

        img = Image.fromarray(frame)

        counter += 1
        img_path = os.path.join(output_folder, f"frame_{counter}.png")
        img.save(img_path)
        print(f"Saved frame at {t:.2f} seconds to {img_path}")


video_path = "/Users/gmmrr/Desktop/20. 林冠銘.MP4"
start_time = 37
end_time = 386
output_folder = "/Users/gmmrr/Desktop/outputframes/20. 林冠銘"

capture_frames(video_path, start_time, end_time, output_folder)
