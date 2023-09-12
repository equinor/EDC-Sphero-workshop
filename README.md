# EDC Sphero BOLT workshop
Welcome to this workshop where we will be playing around with some really cool
robots. I have also mounted a camera that will stream video so we can use 
OpenCV to track the robots.

I have made a couple of scripts to get you started (see sphero_example.py and
opencv_example.py). You are free to attempt one of the challenges bellow or 
work on your own thing.

## Getting started
Find the name written on the front of your Sphero (Starts with SB-) and run the
example:
```bash
python sphero_example.py <spero_name>
python opencv_example.py <video_stream>
```

# Sphero BOLT bowling
Let's try some Sphero bowling!

You can use the video stream to locate the bowling pins (will be marked with
a colour) and to locate the Sphero itself. Then all you need to do is drive
the Sphero into the pins and knock them over.

# Sphero BOLT maze challenge
The challenge is to get your Sphero to the end of the maze as quickly as
possible. You can choose if you want to use video to track the Sphero or to
solve the challenge using only the Sphero's builtin sensors.

## Rules of the game
* The Sphero has to complete the maze autonomously. No human interaction is
  allowed.
* You will be able to do a mapping stage for up to 5 minutes before the timer
  starts. After the mapping is done the Sphero will be placed at the beginning
  of the maze. You will be allowed to touch the computer after the mapping
  stage to initiate the race sequence.
* There will be bonus points for style. Each point takes 1 second off you time.
* The timer will start when the Sphero starts moving through the maze.
  Connection time and compass calibration is not included.

## About the maze
* All paths in the maze are in north-south or east-west direction.
* Each intersection is covered by a roof.
* The distance between the intersections all the same length.
* The beginning and end of the maze are both "dead ends". Neither is covered by
  a roof.
