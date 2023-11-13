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


def replace_orange_with_background(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([10, 100, 100])
    upper_red = np.array([25, 255, 255])

    # Create a binary mask for the red pixels
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Find contours in the red mask
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour (assuming there's only one large red region)
    for contour in contours:
        # Find the bounding box of the red region
        x, y, w, h = cv2.boundingRect(contour)

        # Ensure the bounding box coordinates are within the image bounds
        x, y, w, h = max(0, x), max(0, y), min(w, image.shape[1] - x), min(h, image.shape[0] - y)

        # Extract the region of interest (ROI) from the original image
        roi = image[y:y + h, x:x + w]

        # Find the background color of the nearest non-red pixels
        non_red_pixels = roi[~red_mask[y:y + h, x:x + w].astype(bool)]
        print(non_red_pixels)
        background_color = np.median(non_red_pixels, axis=0)

        # Fill the ROI with the background color
        roi[:, :] = np.full_like(roi, background_color)

    return image
def replace_red_with_background(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for the red color in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a binary mask for the red pixels
    red_mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Find contours in the red mask
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through each contour (assuming there's only one large red region)
    for contour in contours:
        # Find the bounding box of the red region
        x, y, w, h = cv2.boundingRect(contour)

        # Ensure the bounding box coordinates are within the image bounds
        x, y, w, h = max(0, x), max(0, y), min(w, image.shape[1] - x), min(h, image.shape[0] - y)

        # Extract the region of interest (ROI) from the original image
        roi = image[y:y+h, x:x+w]

        # Find the background color of the nearest non-red pixels
        non_red_pixels = roi[~red_mask[y:y+h, x:x+w].astype(bool)]
        print(non_red_pixels)
        background_color = np.median(non_red_pixels, axis=0)

        # Fill the ROI with the background color
        roi[:, :] = np.full_like(roi, background_color)

    return image

def main():
    file_list = list_files("./data/updated-images")
    img_path = "./data/updated-images/" + file_list[0]

    # Load the image
    orig_img = cv2.imread(img_path)
    orange_result = replace_red_with_background(img_path)

    # Display the original image
    cv2.imshow("Original Image", orig_img)

    print(orange_result)
    # Display the image with detected orange pixels
    cv2.imshow("Orange Pixels Detection", cv2.resize(orange_result, (500, 500)))

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print(file_list)

if __name__ == "__main__":
    main()