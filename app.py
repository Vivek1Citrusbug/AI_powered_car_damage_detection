import streamlit as st
from page_components import configure_ui, get_sidebar_options
from detect_services import PPEDetector
from utility_functions import (
    save_uploaded_file,
    process_and_display_image,
    process_and_display_video,
)

MODEL_PATHS = {
    "YOLOv8-small": "models/YOLOv8s_100Epochs.pt",
    "YOLOv8-medium": "models/YOLOv8m_100Epochs.pt",
    # "YOLOv8-nano": "models/Yolov8n_without_aug.pt",
}
SUPPORTED_IMAGE_FORMATS = {"jpg", "jpeg", "png"}
SUPPORTED_VIDEO_FORMATS = {"mp4"}


def main():
    """
    Main execution function.
    """

    configure_ui()

    model_choice, uploaded_files, use_webcam = get_sidebar_options()

    detector = PPEDetector(MODEL_PATHS.get(model_choice, "YOLOv8-small"))

    if use_webcam:
        detector.process_webcam()

    elif uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = save_uploaded_file(uploaded_file)
            file_extension = file_path.suffix[1:].lower()

            if file_extension in SUPPORTED_IMAGE_FORMATS:
                process_and_display_image(detector, file_path)

            elif file_extension in SUPPORTED_VIDEO_FORMATS:
                process_and_display_video(detector, file_path)

            else:
                st.warning(f"⚠️ Unsupported file format: {file_extension}")

    else:
        st.info("📤 Upload images or videos for object detection.")

    st.sidebar.markdown("---")
    st.sidebar.info("👨‍💻 Developed with Streamlit & YOLOv8")


if __name__ == "__main__":
    main()