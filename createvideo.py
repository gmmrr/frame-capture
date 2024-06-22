import cv2
import os

frame_path = '../../../Desktop/framevideo/3/'
output_path = '../../../Desktop/framevideo/'
output_file = os.path.join(output_path, '3.mp4')

frame_width = 1433
frame_height = 1842
frame_rate = 15
duration = 20
total_frames = frame_rate * duration

os.makedirs(output_path, exist_ok=True)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, frame_rate, (frame_width, frame_height))

for i in range(1, total_frames + 1):
    frame_filename = os.path.join(frame_path, f'frame_{i}.jpg')
    frame = cv2.imread(frame_filename)

    if frame is None:
        print(f'Warning: Could not read frame {frame_filename}')
        break

    out.write(frame)

out.release()

print(f'Video saved as {output_file}')
