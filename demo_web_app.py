# demo_app.py
from flask import Flask, Response
from read_camera_class import VideoStream
import cv2

app = Flask(__name__)

# Khởi tạo đối tượng VideoStream với camera mặc định (index 0)
stream = VideoStream(0)

def gen(stream):
    """Đọc frame và trả về dữ liệu MJPEG."""
    while True:
        frame = stream.get_frame()
        if frame is None:
            break
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@app.route('/')
def index():
    return "Homepage, access /video to see the camera stream"

@app.route('/video')
def video():
    return Response(gen(stream),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
