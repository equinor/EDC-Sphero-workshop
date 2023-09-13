import cv2
import numpy as np

def make_contours(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Perform edge detection using Canny
    edges = cv2.Canny(gray, 1500, 2500, apertureSize=5)
    kernel = np.ones((3, 3), np.uint8)
    edges = cv2.dilate(edges, kernel, iterations=1)
    cv2.imshow('Edges', edges)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours


def detect_objects(contours):
    """ Detects objects in the frame and returns their centers and contours. """

    centers = []
    position_contours = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        aspect_ratio = w / float(h)
        if aspect_ratio < 0.6 or aspect_ratio > 1.4:
            continue

        M = cv2.moments(contour)

        # Calculate the center of mass (centroid) of the contour
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0

        # Store the center coordinates in the list
        centers.append((cx, cy))
        position_contours.append(contour)

    return centers, position_contours


# Open the video stream (0 for default camera)
cap = cv2.VideoCapture("http://192.168.50.5:8081")

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if not ret:
        break

    contours = make_contours(frame)
    centers, contours = detect_objects(contours)

    for point in centers:
        point = (int(point[0]), int(point[1]))
        cv2.circle(frame, point, 4, (0, 255, 0), -1)

    for contour in contours:
        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

    # Display the frame with detected squares
    cv2.imshow('Postits Detected', frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video stream and close all windows
cap.release()
cv2.destroyAllWindows()
