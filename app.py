from flask import Flask, render_template, Response
import cv2
import effects
import os
from time import time

app = Flask(__name__)
video = cv2.VideoCapture(0)
index_add_counter = 0
startTime = time()

@app.route('/')
def hello_world():
    return render_template("index.html")


def gen(video):
    while True:
        global startTime
        global index_add_counter
        success, image = video.read()
        colour_selector = index_add_counter % 4
        if colour_selector == 1:
            new_image = effects.change_colour(image)
        elif colour_selector == 2:
            new_image = effects.change_colour_blue(image)
        elif colour_selector == 3:
            new_image = effects.change_colour_green(image)
        else:
            new_image = image

        #runs every 1 second
        #if time() - startTime > 1:
            #startTime = time()
        new_image = effects.colourize_image(new_image)
        ret, jpeg = cv2.imencode('.jpg', new_image)
        frame = jpeg.tobytes()

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

@app.route("/url/count/increment", methods = ['POST'])
def increment_count():
    global index_add_counter
    index_add_counter = index_add_counter + 1
    print(index_add_counter)
    return "success=true"
    #pass #count = count + 1


if __name__ == '__main__':
    app.run(threaded=True, port = int(os.environ.get('PORT', 33507)))
