import cv2
from ultralytics import YOLO

# Tải mô hình YOLOv8n (nếu chưa có, model sẽ tự tải xuống)
model = YOLO("yolov8n.pt")

def detect_people(frame):
    """
    Sử dụng YOLOv8 để phát hiện người trong frame.
    Vẽ bounding box cho đối tượng 'person' với độ tin cậy > 0.5.
    """
    results = model(frame)[0]
    if results.boxes is not None:
        for box in results.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            class_id = int(box.cls[0].item())
            confidence = box.conf[0].item()
            # Với dataset COCO, class id 0 là 'person'
            if class_id == 0 and confidence > 0.5:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                label = f"Person: {confidence:.2f}"
                cv2.putText(frame, label, (int(x1), int(y1)-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
    return frame