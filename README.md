# Creatica

## Set up

To work on this project, first you need [Git](https://gitforwindows.org/).
You will also need either Git Bash (comes with Git) or [Github Desktop](https://desktop.github.com/). If you are unfamiliar with git commands it may be more intuitive to start off with Github Desktop

You will also need [Python3](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/) (should already come with python)
and a text editor or IDE of your choice. I recommend [Pycharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/)

To clone the repository click on the green button at the top and either open it with Github Desktop or in a command terminal, in your desired folder run `git clone https://github.com/floatingturnip/Creatica.git`

After cloning the repository, set up a virtual environment, if using Pycharm you can follow these [instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html)
otherwise follow these [instructions](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to create and activate your virtual environment.

Once your virtual environment is activated run `pip install -r requirements.txt`

## Run the app
Now in your terminal if you type `python app.py` you should be able to run it

## Inspiration
“The world’s most creative people are hell bent on finding ways to use technology to allow audiences to see in new ways. And hear in new ways. And feel in new ways.” They explore the intersection of Art and Technology while simultaneously triggering a meditative emotion in the viewer. It is amazing to experience the artist’s creativity, self-control, and confrontation. But what if you aren’t an artist but want to create your own piece of art to impress yourself, to discover something completely your own.
So let us all enjoy our artistic creativity using technology on our Web Application!!

## What it does
This is a web application that uses a computer’s web camera and is able to identify the number of fingers being held up. Upon pressing the enable colour button, the user can now change the colour of the video with the movement of their hand. Each finger they hold up changes the colour of the frame. 

The user changes their world (Video frame) only by waving their hand and is each time curious to discover what their next piece of art will be. Our web app allows the user to explore their artistic creativity through movement and continuously intrigues them. So the user is in the artistic control of their surroundings. 

## How we built it
This is a web application built with Flask framework. It uses Python and OpenCV on the back end and html, css on the front end. JavaScript was used to send requests and information from the front end to the back end.

## Challenges we ran into
Integrating frontend and backend functions together

## Accomplishments that I'm proud of
Working remotely with people we don’t know in different timezones
Building something in a short period of time.
Learning something new!

## What we learned
How to make Post requests
How to integrate frontend and backend functions together
How to use Python, OpenCV and Flask
Html and css
Collaborating on code with Github

## What's next
We would like to incorporate additional features such as more colours, more options for image detection, etc. One interesting feature we would like to add is when the user waves, they will be greeted with a robot that waves back. We would also like to improve our image recognition algorithm so that it's more reliable in different lighting settings. We also hope to deploy our web app so that anyone can use it. We intend to use one of our registered domains for our webapp:
changetheworldwithyourfingertips.tech

