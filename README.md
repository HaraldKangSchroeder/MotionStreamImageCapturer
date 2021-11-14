# MotionStreamImageCapturer

Simple python script to capture images of a motion (https://motion-project.github.io/index.html) stream.

## Installation

* Clone the project
* Install dependencies \
    `pip install -r requirements.txt`

## Usage

* Execute script as \
    `python main.py <url> <sleeping_time> <destination_folder>`
    * **url** : the url of the motion stream
    * **sleeping_time** : time in seconds between 2 captured images
    * **destination_folder** : existing folder where the captured images will get placed

    Example : \
    `python main.py http://<ip>:<port> 60 ./images/`

### Note
Captured images might have a delay of around 12 seconds

