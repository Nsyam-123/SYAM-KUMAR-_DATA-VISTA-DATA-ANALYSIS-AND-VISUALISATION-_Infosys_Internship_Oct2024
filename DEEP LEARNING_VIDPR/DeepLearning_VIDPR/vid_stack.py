import cv2
import numpy as np

# Use raw strings for file paths
cap1 = cv2.VideoCapture(r'C:\Users\Personal\intetive\DEEP LEARNING_VDPR\DeepLearning_VIDPR\VIDEO1.mp4')
cap2 = cv2.VideoCapture(r'C:\Users\Personal\intetive\DEEP LEARNING_VDPR\DeepLearning_VIDPR\VIDEO2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break

    # Resize the frames
    frame1 = cv2.resize(frame1, (640, 360))
    frame2 = cv2.resize(frame2, (640, 360))

    # Concatenate vertically
    h_concat = np.vstack((frame1, frame2))

    # Display the concatenated video
    cv2.imshow('Concatenated Video', h_concat)

    # Exit if 'q' is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
