import cv2

# Use raw strings for file paths to avoid Unicode escape issues
cap_video1 = cv2.VideoCapture(r'C:\Users\Personal\intetive\DEEP LEARNING_VDPR\DeepLearning_VIDPR\VIDEO1.mp4')
cap_video2 = cv2.VideoCapture(r'C:\Users\Personal\intetive\DEEP LEARNING_VDPR\DeepLearning_VIDPR\VIDEO2.mp4')
cap_webcam = cv2.VideoCapture(0)

current_video = cap_video1

while True:
    ret, frame = current_video.read()
    
    if not ret:
        # Switch to the next video in sequence
        if current_video == cap_video1:
            current_video = cap_video2
        elif current_video == cap_video2:
            current_video = cap_webcam
        else:
            current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset webcam
        continue
    
    cv2.imshow('Media', frame)

    # Switch to the next video on pressing 'n'
    if cv2.waitKey(1) & 0xFF == ord('n'):
        if current_video == cap_video1:
            current_video = cap_video2
        elif current_video == cap_video2:
            current_video = cap_webcam
        else:
            current_video = cap_video1

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap_video1.release()
cap_video2.release()
cap_webcam.release()
cv2.destroyAllWindows()
