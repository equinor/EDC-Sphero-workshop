import cv2
import numpy as np
import sys


# Lower bound for red
lower_color = np.array([0, 20, 20])
# Upper bound for red
upper_color = np.array([10, 255, 255])

# Minimum contour area threshold to filter out small objects
min_contour_area = 500


def main():
    address = sys.argv[-1]
    cap = cv2.VideoCapture(f"http://{address}")

    while True:
        ret, frame = cap.read()

        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask to extract the object of the desired color
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours in the mask
        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        object_centers = []

        for contour in contours:
            # Filter out small or noisy contours based on area
            if cv2.contourArea(contour) >= min_contour_area:
                # Calculate the center of the contour
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    object_centers.append((cX, cY))

        # Draw a circle at the center of each detected object
        for center in object_centers:
            cv2.circle(frame, center, 5, (0, 255, 0), -1)

        # Display the original frame with detected objects
        cv2.imshow('Object Detection', frame)

        # Check for key events (non-blocking)
        key = cv2.waitKey(1) & 0xFF

        # Exit when 'q' is pressed
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
