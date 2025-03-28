# 🚗 AI-Powered Car Damage Detection using YOLOv8

This project focuses on detecting different types of car damages using the YOLOv8 object detection model. The dataset includes various types of car damages, such as dents, scratches, bumper damage, and windscreen cracks.

## 📌 Features
- Object detection for multiple car damage types.
- Trained using YOLOv8 on a custom dataset.
- High mAP50 and recall values for accurate predictions.
- Supports real-time detection on images and videos.

---

## 📂 Dataset Information

### Dataset Link
- https://universe.roboflow.com/automobile-damage-detection/automobile-damage-detection/dataset/4


### **Classes in the dataset**:
1. **Front-windscreen-damage**
2. **Headlight-damage**
3. **Rear-windscreen-damage**
4. **Runningboard-damage**
5. **Sidemirror-damage**
6. **Taillight-damage**
7. **Bonnet-dent**
8. **Boot-dent**
9. **Doorouter-dent**
10. **Fender-dent**
11. **Front-bumper-dent**
12. **Quarterpanel-dent**
13. **Rear-bumper-dent**
14. **Roof-dent**

---

## 🎯 Training Details
The model was trained using **YOLOv8** on a dataset with **1,043 images**.

### **Model Architecture**
- **Model**: YOLOv8 (Small)
- **Layers**: 72
- **Parameters**: 11,131,002
- **GFLOPs**: 28.5
- **Batch Size**: 16
- **Epochs**: 50
- **Image Size**: 640x640

---

## 📊 Model Performance

### **Training Performance**
| Class | Precision (P) | Recall (R) | mAP50 | mAP50-95 |
|--------|--------------|------------|--------|----------|
| **Overall** | **0.891** | **0.762** | **0.834** | **0.675** |
| Front-windscreen-damage | 0.953 | 0.720 | 0.837 | 0.703 |
| Headlight-damage | 0.840 | 0.767 | 0.805 | 0.586 |
| Rear-windscreen-damage | 0.980 | 0.831 | 0.917 | 0.789 |
| Runningboard-damage | 0.828 | 0.770 | 0.816 | 0.686 |
| Sidemirror-damage | 1.000 | 0.923 | 0.959 | 0.873 |
| Taillight-damage | 0.845 | 0.833 | 0.852 | 0.732 |
| Bonnet-dent | 0.953 | 0.763 | 0.867 | 0.661 |
| Boot-dent | 0.678 | 0.462 | 0.464 | 0.234 |
| Doorouter-dent | 0.922 | 0.780 | 0.875 | 0.720 |
| Fender-dent | 0.848 | 0.694 | 0.801 | 0.611 |
| Front-bumper-dent | 0.894 | 0.773 | 0.870 | 0.702 |
| Quarterpanel-dent | 0.935 | 0.780 | 0.876 | 0.675 |
| Rear-bumper-dent | 0.858 | 0.757 | 0.855 | 0.727 |
| Roof-dent | 0.941 | 0.820 | 0.880 | 0.751 |

---

### **Validation Performance**
| Class | Precision (P) | Recall (R) | mAP50 | mAP50-95 |
|--------|--------------|------------|--------|----------|
| **Overall** | **0.891** | **0.762** | **0.834** | **0.675** |
| Front-windscreen-damage | 0.953 | 0.720 | 0.838 | 0.704 |
| Headlight-damage | 0.838 | 0.767 | 0.805 | 0.587 |
| Rear-windscreen-damage | 0.980 | 0.831 | 0.917 | 0.789 |
| Runningboard-damage | 0.828 | 0.769 | 0.816 | 0.682 |
| Sidemirror-damage | 1.000 | 0.923 | 0.959 | 0.872 |
| Taillight-damage | 0.845 | 0.833 | 0.852 | 0.732 |
| Bonnet-dent | 0.952 | 0.763 | 0.867 | 0.660 |
| Boot-dent | 0.680 | 0.462 | 0.465 | 0.234 |
| Doorouter-dent | 0.921 | 0.780 | 0.875 | 0.720 |
| Fender-dent | 0.848 | 0.694 | 0.801 | 0.611 |
| Front-bumper-dent | 0.895 | 0.772 | 0.872 | 0.701 |
| Quarterpanel-dent | 0.935 | 0.780 | 0.879 | 0.675 |
| Rear-bumper-dent | 0.858 | 0.758 | 0.855 | 0.726 |
| Roof-dent | 0.941 | 0.820 | 0.879 | 0.753 |

---

## 🏗 Installation & Usage

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/your-repo/AI_powered_car_damage_detection.git
cd AI_powered_car_damage_detection

