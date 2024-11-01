import cv2
import os

folder_path = 'C:\Users\Personal\intetive\DEEP LEARNING_IMGPR\DeepLearning_IMGPR'
image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpg', '.jpg'))]
#image_files = image_files[:10]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    if image is not None:
        cv2.imshow(image_file, image)
        cv2.waitKey(0)  
    else:
        print(f"Failed to load image: {image_file}")
cv2.destroyAllWindows()


