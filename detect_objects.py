import cv2
import numpy as np

def make_contours(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Perform edge detection using Canny
    edges = cv2.Canny(gray, 1500, 2500, apertureSize=5)
    cv2.imshow('Edges', edges)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours


def detect_postits(contours):
    """ Detects post-its in the frame and returns their centers. """

    centers = []

    for contour in contours:
        # Include only contours with aspect ratio between 0.8 and 1.2
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if aspect_ratio < 0.7 or aspect_ratio > 1.3:
            continue

        # Calculate the moments of the contour
        M = cv2.moments(contour)

        # Calculate the center of mass (centroid) of the contour
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0

        # Draw a circle at the center of the object
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)  # Red color, filled circle

        # Store the center coordinates in the list
        centers.append((cx, cy))

    return centers


# Open the video stream (0 for default camera)
cap = cv2.VideoCapture("http://192.168.50.5:8081")

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    contours = make_contours(frame)
    postits = detect_postits(contours)

    for point in postits:
        point = (int(point[0]), int(point[1]))
        cv2.circle(frame, point, 4, (0, 255, 0), -1)

    # Display the frame with detected squares
    cv2.imshow('Squares Detected', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
