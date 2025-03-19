import cv2
from skimage.metrics import structural_similarity as ssim


def compare_images(image1: cv2.typing.MatLike, image2: cv2.typing.MatLike):
    # Convert to grayscale for SSIM comparison
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate SSIM between the two images
    score, _ = ssim(gray1, gray2, full=True)
    return score


# # Example usage:
# frame1 = cv2.imread("frame_0001.jpg")
# frame2 = cv2.imread("frame_0002.jpg")
# similarity_score = compare_images(frame1, frame2)
# if similarity_score < 0.8:  # Threshold for outfit change
#     print("Outfit change detected between frames")


def remove_similar_images(frames_list: list[str], output_frames_dir: str) -> list[str]:
    keyframes: list[str] = [frames_list[0]]
    for i in range(1, len(frames_list) - 1):
        image1 = cv2.imread(output_frames_dir + keyframes[len(keyframes) - 1])
        image2 = cv2.imread(output_frames_dir + frames_list[i])
        similarity_score = compare_images(image1, image2)
        if similarity_score < 0.83:
            keyframes.append(frames_list[i])
    return keyframes
