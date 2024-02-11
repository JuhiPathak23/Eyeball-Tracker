import cv2

# For the face and eye detected load the Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Function to detect eyes and draw red dots at the center of the eyes.
def detect_eyes_in_face(gray_frame, colored_frame):
	# Detect faces in the grayscale frame
	faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

	# Iterate through the detected faces
	for (x, y, w, h) in faces:
		# Extract the region of interest (ROI) for face and eyes
		roi_gray = gray_frame[y:y + h, x:x + w]
		roi_color = colored_frame[y:y + h, x:x + w]

		# Detect eyes in the ROI
		eyes = eye_cascade.detectMultiScale(roi_gray)

		# Iterate through the detected eyes
		for (ex, ey, ew, eh) in eyes:
			# Draw a green rectangle around each eye
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

			# Calculate the center of the eye
			center = (x + ex + ew // 2, y + ey + eh // 2)

			# Draw a red dot at the center of the eye
			cv2.circle(colored_frame, center, 2, (0, 0, 255), -1)

	# Return the colored frame with the eye tracking annotations
	return colored_frame

def main():
	# Display mode options
	print("Choose mode:")
	print("1. Webcam mode")
	print("2. Static image mode")

	# Get user choice
	choice = input("Enter your choice (1 or 2): ")

	if choice == '1':
		# Open webcam
		webcam_capture = cv2.VideoCapture(0)

		print("To quit webcam eyeball tracking window, press 'Q'.")

		while True:
			# Read a frame from the webcam
			ret, frame = webcam_capture.read()

			# Convert the frame to grayscale
			gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			# Perform eye tracking and display the result
			result_frame = detect_eyes_in_face(gray_frame, frame)
			cv2.imshow('Eyeball Tracking - Webcam Mode', result_frame)

			# Break the loop when 'q' is pressed
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		# Release the webcam and close all windows
		webcam_capture.release()
		cv2.destroyAllWindows()

	elif choice == '2':
		# Get the path to the static image
		image_path = 'image.png'

		# Read the static image from file
		static_frame = cv2.imread(image_path)

		# Check if the image was read successfully
		if static_frame is None:
			print("Error: Unable to read the image file.")
			return

		# Convert the static frame to grayscale
		gray_static_frame = cv2.cvtColor(static_frame, cv2.COLOR_BGR2GRAY)

		# Perform eye tracking on the static image and display the result
		result_static_frame = detect_eyes_in_face(gray_static_frame, static_frame)
		cv2.imshow('Eyeball Tracking - Static Image Mode', result_static_frame)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	else:
		print("Invalid choice. Please enter '1' for Webcam mode or '2' for Static image mode.")

	print("Thanks for using Eyeball Tracking!!!")

if __name__ == '__main__':
	main()