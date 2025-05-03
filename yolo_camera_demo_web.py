from yolo_camera_class import detect_people
import cv2

def gen(stream):
    while True:
        frame = stream.get_frame()
        if frame is None:
            break
        # Phát hiện người trong frame
        frame = detect_people(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')
        
