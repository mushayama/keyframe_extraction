import argparse
from .poc1 import poc1


def main() -> None:
    POC_TYPES = ["poc1", "poc2"]

    parser = argparse.ArgumentParser("parser")
    parser.add_argument(
        "poc",
        help="mention the poc approach to run: " + " ".join(POC_TYPES),
        choices=POC_TYPES,
    )
    args = parser.parse_args()

    # print(args.poc)

    video_index = 1

    INPUT_DIR_PATH = "assets/input_videos/"
    OUTPUT_DIR_PATH = "assets/output/"
    INPUT_VIDEO_NAME = f"input_{video_index}.mp4"

    if args.poc == "poc1":
        poc1(INPUT_DIR_PATH, INPUT_VIDEO_NAME, OUTPUT_DIR_PATH)
