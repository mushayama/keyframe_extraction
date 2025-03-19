import cv2
import os
import csv


def extract_frames(
    video_path: str, output_frames_dir: str, output_frames_csv: str
) -> list[str]:
    if os.path.exists(output_frames_csv) and os.path.getsize(output_frames_csv) > 0:
        print("Frames already extracted. Skipping extraction.")

        frame_list: list[str] = []

        with open(output_frames_csv, mode="r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row:
                    frame_list.append(row[0])

        return frame_list

    os.makedirs(output_frames_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return

    # frame_rate = cap.get(cv2.CAP_PROP_FPS)
    frame_list: list[str] = []
    frame_count: int = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_name = f"frame_{frame_count:04d}.jpg"
        frame_path = os.path.join(output_frames_dir, frame_name)

        cv2.imwrite(frame_path, frame)
        frame_list.append(frame_name)

        frame_count += 1

    cap.release()

    with open(output_frames_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Frame Name"])
        for frame in frame_list:
            writer.writerow([frame])

    print(f"Extracted {frame_count} frames and saved to {output_frames_dir}")
    print(f"Frame names saved to {output_frames_csv}")

    return frame_list
