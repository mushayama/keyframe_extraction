import cv2
import numpy as np


def filter_frames_with_people(
    frames_list: list[str], output_frames_dir: str
) -> list[str]:
    yolo_weights_path = "assets/models/yolo/yolov4.weights"
    yolo_cfg_path = "assets/models/yolo/yolov4.cfg"
    net = cv2.dnn.readNet(yolo_weights_path, yolo_cfg_path)
    layer_names = net.getLayerNames()
    # print(layer_names)
    # print(net.getUnconnectedOutLayers())
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    # print(output_layers)

    def detect_person(frame):
        blob = cv2.dnn.blobFromImage(
            frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False
        )
        net.setInput(blob)
        outputs = net.forward(output_layers)

        # Find person detection (class ID for person in COCO dataset is 0)
        person_detected = False
        # height, width, channels = frame.shape
        for out in outputs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                if class_id == 0:
                    person_detected = True
                    break
        return person_detected

    frames_with_people: list[str] = []
    for frame_name in frames_list:
        frame = cv2.imread(output_frames_dir + frame_name)
        resized_frame = cv2.resize(frame, (416, 416))
        if detect_person(resized_frame):
            frames_with_people.append(frame_name)

    return frames_with_people
