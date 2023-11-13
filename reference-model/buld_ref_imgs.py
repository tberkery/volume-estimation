import cv2
import numpy as np
import os
from PIL import Image

def list_files(directory):
    # Get all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Sort the list of files
    files.sort()

    return files


def detect_orange_pixels(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the orange color in HSV
    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([30, 255, 255])

    # Create a binary mask for the orange pixels
    orange_mask = cv2.inRange(hsv_image, lower_orange, upper_orange)

    # Apply the mask to the original image
    result_image = cv2.bitwise_and(image, image, mask=orange_mask)

    return result_image

def detect_red_pixels(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a binary mask for the red pixels
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Apply the mask to the original image
    result_image = cv2.bitwise_and(image, image, mask=red_mask)

    return result_image

def main():
    file_list = list_files("./data/updated-images")
    img_path = "./data/updated-images/" + file_list[0]

    # Load the image
    orig_img = cv2.imread(img_path)
    orange_result = detect_orange_pixels(img_path)

    # Display the original image
    cv2.imshow("Original Image", orig_img)

    print(orange_result)
    # Display the image with detected orange pixels
    cv2.imshow("Orange Pixels Detection", orange_result)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(file_list)

if __name__ == "__main__":
    main()