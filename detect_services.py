import cv2
import tempfile
import numpy as np
from ultralytics import YOLO
import streamlit as st
import ffmpeg as ff


class PPEDetector:

    def __init__(self, model_path):
        """
        Initialize the PPE Detector with a given YOLO model
        """

        self.model = YOLO(model_path)
        self.available_classes = [
            "Front-windscreen-damage",
            "Headlight-damage",
            "Rear-windscreen-damage",
            "Runningboard-damage",
            "Sidemirror-damage",
            "Taillight-damage",
            "Bonnet-damage",
            "Boot-damage",
            "Doorouter-damage",
            "Fender-damage",
            "Front-bumper-damage",
            "Quaterpanel-damage",
            "Rear-bumper-damage",
            "Roof-damage",
            # "Wheel-damaged"
        ]


    def detect_objects(self, frame):
        """
        Detect PPE objects in an image frame and annotate them with bounding boxes and labels.
        """

        results = self.model(frame)
        img_height, img_width = frame.shape[:2]

        text_positions = []

        for result in results:
            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())
                label = f"{self.available_classes[cls]}: {conf:.2f}"

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                text_size, baseline = cv2.getTextSize(
                    label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1
                )
                text_width, text_height = text_size

                text_x = x1
                text_y = y1 - 10

                if text_y < text_height:
                    text_y = y1 + text_height + 10
                if text_x + text_width > img_width:
                    text_x = img_width - text_width - 10

                for prev_x, prev_y, prev_w, prev_h in text_positions:
                    if (
                        text_x < prev_x + prev_w
                        and text_x + text_width > prev_x
                        and text_y < prev_y + prev_h
                        and text_y + text_height > prev_y
                    ):
                        text_y = prev_y + prev_h + 5

                cv2.rectangle(
                    frame,
                    (text_x, text_y - text_height),
                    (text_x + text_width, text_y + baseline),
                    (0, 0, 0),
                    -1,
                )

                cv2.putText(
                    frame,
                    label,
                    (text_x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1,
                )

                text_positions.append(
                    (text_x, text_y - text_height, text_width, text_height + baseline)
                )

        return frame

    def process_image(self, image_path):
        """
        Process an image for PPE detection
        """

        image = cv2.imread(image_path)
        return self.detect_objects(image)

    def process_video(self, video_path):
        """
        Process a video and detect PPE in each frame
        """

        cap = cv2.VideoCapture(video_path)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(
            cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        )

        temp_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        output_path = temp_video.name
        temp_video.close()

        progress_bar = st.progress(0)

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            processed_frame = self.detect_objects(frame)

            out.write(processed_frame)
            frame_count += 1
            progress_bar.progress(frame_count / total_frames)

        cap.release()
        out.release()

        return output_path

    def process_webcam(self):
        """
        Process a webcam and detect PPE
        """

        st.write("📷 **Live Webcam Object Detection**")
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.error(
                    "❌ **Failed to access webcam.** Please check your camera settings."
                )
                break

            processed_frame = self.detect_objects(frame)
            processed_frame = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            stframe.image(processed_frame, channels="RGB")

        cap.release()
        cv2.destroyAllWindows()
