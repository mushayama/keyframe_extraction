import cv2
import os
from .extract_frames import extract_frames
from .detect_people import filter_frames_with_people
from .filter_images import remove_similar_images


def poc1(input_path: str, video_name: str, output_path: str) -> None:
    video_path = input_path + video_name
    output_dir = output_path + video_name.split(".")[0]
    output_frames_dir = output_dir + "/frames/"
    output_frames_csv = output_dir + "/frames.csv"

    frames_list = extract_frames(video_path, output_frames_dir, output_frames_csv)
    print(f"Recieved {len(frames_list)} frames")

    frames_with_people = filter_frames_with_people(frames_list, output_frames_dir)
    print(f"Recieved {len(frames_with_people)} frames with people")

    different_keyframes = remove_similar_images(frames_with_people, output_frames_dir)
    print(f"Recieved {len(different_keyframes)} keyframes")
    print(different_keyframes)
