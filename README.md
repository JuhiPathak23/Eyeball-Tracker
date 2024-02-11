# Eyeball-Tracker
The Eyeball Tracking Application is a computer vision project implemented using OpenCV (Open Source Computer Vision Library) in Python. The application detects faces and eyes in both live webcam streams and static images, providing visual feedback by drawing rectangles around detected eyes and placing red dots at the centers of the eyes.

# Features

Face and Eye Detection: Utilizes pre-trained Haar cascades to detect faces and eyes in images and live video streams.

Eye Tracking: Locates the centers of detected eyes and marks them with red dots, allowing users to visualize the positions of eyes accurately.

Webcam and Static Image Modes: Offers two modes of operation – Webcam mode for real-time eye tracking from a live camera feed and Static Image mode for eye tracking in pre-captured images.

# Implementation

Face and Eye Detection: The application uses the CascadeClassifier class from OpenCV to load pre-trained Haar cascades for face and eye detection. These cascades are applied to grayscale frames obtained from the webcam or static images.

Eye Tracking: After detecting faces, the application extracts regions of interest (ROI) corresponding to each detected face and searches for eyes within these ROIs. It draws green rectangles around detected eyes and red dots at the centers of the eyes.

Webcam and Static Image Modes: The application provides users with a choice between Webcam mode and Static Image mode. In Webcam mode, it accesses the live webcam feed, processes each frame for eye tracking, and displays the result in real-time. In Static Image mode, it reads a pre-selected image file, performs eye tracking on it, and displays the annotated image.

# Usage

Webcam Mode: Users can choose Webcam mode to enable real-time eye tracking from the webcam feed. They can quit the application by pressing the 'Q' key.

Static Image Mode: Users can select Static Image mode to perform eye tracking on pre-captured images. They need to provide the path to the image file, and the application displays the annotated image.

# Conclusion

The Eyeball Tracking Application is a versatile tool for eye tracking and visualization, useful for various applications such as human-computer interaction, gaze tracking, and behavioral studies. It provides a user-friendly interface and can be easily extended with additional features for advanced eye-tracking applications.
