from flask import Flask, render_template, Response
import cv2
import effects

app = Flask(__name__)
video = cv2.VideoCapture(0)
count = 0

@app.route('/')
def hello_world():
    return render_template("index.html")


def gen(video):
    while True:
        success, image = video.read()
        new_image = effects.get_ball(image)

        ret, jpeg = cv2.imencode('.jpg', new_image)
        frame = jpeg.tobytes()
        #cv2.imshow("test_image", test_image)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run()
