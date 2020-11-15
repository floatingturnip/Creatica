from flask import Flask, render_template, Response
import cv2
import effects
import os
from time import time

app = Flask(__name__)
video = cv2.VideoCapture(0)
index_add_counter = 0
startTime = time()
robot_img = r'\static\robot_1.png'
colour_selector = 0

@app.route('/')
def hello_world():
    return render_template("index.html")


def gen(video):
    while True:
        #global startTime
        global index_add_counter
        global colour_selector
        success, image = video.read()
        new_image, count = effects.colourize_image(image)
        if index_add_counter % 2 == 1:
            colour_selector = count #% 5
            if colour_selector == 1:
                new_image = effects.change_colour(new_image)
            elif colour_selector == 2:
                new_image = effects.change_colour_blue(new_image)
            elif colour_selector == 3:
                new_image = effects.change_colour_green(new_image)
            elif colour_selector == 4:
                new_image = effects.change_colour_purple(new_image)
            elif colour_selector >= 5:
                new_image = effects.change_colour_yellow(new_image)
            else:
                new_image = image

        #checks every 4 seconds to see if user is waving
        #if time() - startTime > 4:
            #startTime = time()
            #effects.change_robot(colour_selector)

        #new_image = effects.colourize_image(new_image)
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

@app.route("/robot")
def robot():
    global colour_selector
    global robot_img
    global startTime

    if time() - startTime >4:
        change_robot(colour_selector)
        startTime = time()

    return robot_img

# changes the sleepy robot to a waving robot if the user is waving
def change_robot(x):
    global robot_img

    if x < 3:
        robot_img = r'\static\robot_1.png'
    elif x == 3:
        robot_img = r'\static\robot_2.png'
    elif x == 4:
        robot_img = r'\static\robot_3.png'
    else:
        robot_img = r'\static\robot_4.png'



if __name__ == '__main__':
    app.run(threaded=True, port = int(os.environ.get('PORT', 5000)))
