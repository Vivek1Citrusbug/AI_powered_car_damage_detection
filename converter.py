# from PIL import Image
# import os
# import shutil
# import uuid

# def convert_resize_and_copy_images(input_folder, output_folder):
#     os.makedirs(output_folder, exist_ok=True)  # Ensure output folder exists

#     supported_formats = (".png", ".webp", ".bmp", ".tiff", ".jpg", ".jpeg", ".jfif")

#     for filename in os.listdir(input_folder):
#         file_path = os.path.join(input_folder, filename)

#         if os.path.isfile(file_path) and filename.lower().endswith(supported_formats):
#             try:
#                 unique_filename = f"{uuid.uuid4()}.jpeg"
#                 output_path = os.path.join(output_folder, unique_filename)

#                 # If it's already a JPEG, copy and resize it
#                 if filename.lower().endswith((".jpg", ".jpeg")):
#                     with Image.open(file_path) as img:
#                         img = img.convert("RGB")  
#                         img = img.resize((640, 640))  # Resize to 640x640
#                         img.save(output_path, "JPEG", quality=95)
#                     print(f"Copied & Resized: {filename} → {unique_filename}")

#                 # Convert non-JPEG files, resize, and save as JPEG
#                 else:
#                     with Image.open(file_path) as img:
#                         img = img.convert("RGB")
#                         img = img.resize((640, 640))  # Resize to 640x640
#                         img.save(output_path, "JPEG", quality=95)
#                     print(f"Converted, Resized: {filename} → {unique_filename}")

#             except Exception as e:
#                 print(f"Error processing {filename}: {e}")

# # Example usage
# input_base_folder = "C:/Users/vivek/"  
# output_folder = "C:/Users/vivek/output"

# # Loop through subfolders and process images
# for category in ["Bonnet", "wheel", "Bootdent"]:
#     convert_resize_and_copy_images(input_base_folder + category, output_folder)


import os

# Mapping of new dataset classes to old dataset class indices
mapping = {
    0: 6,   # Bonnet-dent → 6
    1: 7,   # Boot-dent → 7
    2: 8,   # Doorouter-dent → 8
    3: 9,   # Fender-dent → 9
    4: 10,  # Front-bumper-dent → 10
    5: 0,   # Front-windscreen-damage → 0
    6: 1,   # Headlight-damage → 1
    7: 12,  # Rear-bumper-dent → 12
    8: 2,   # Rear-windscreen-damage → 2
    9: 13,  # Roof-dent → 13
    10: 4,  # Sidemirror-damage → 4
    11: 14  # Wheel-damaged → 14
}

def update_yolo_labels(label_folder):
    for filename in os.listdir(label_folder):
        if filename.endswith(".txt"):
            label_path = os.path.join(label_folder, filename)

            # Read the original label file
            with open(label_path, "r") as file:
                lines = file.readlines()

            # Process each line in the label file
            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if parts:
                    old_class_id = int(parts[0])  # Get the current class ID
                    if old_class_id in mapping:
                        new_class_id = mapping[old_class_id]  # Get the updated class ID
                        parts[0] = str(new_class_id)  # Replace with new class ID
                        updated_lines.append(" ".join(parts))  # Reconstruct the line

            # Write the updated labels back to the file
            with open(label_path, "w") as file:
                file.write("\n".join(updated_lines) + "\n")

            print(f"Updated labels in {filename}")

# Path to the folder containing YOLO label .txt files
label_folder = "C:/Users/vivek/output/Tempo/My First Project.v1i.yolov8/train/labels"  # Update this path
update_yolo_labels(label_folder)
