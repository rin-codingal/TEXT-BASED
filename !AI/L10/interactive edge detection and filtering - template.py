import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Image not found")
        return

    #convert to grayscale
    

    print("select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge detection")
    print("3. Laplacian Edge detection")
    print("4. Gaussian smoothing")
    print("5. median filtering")
    print("6. exit")
    print()

    while True:
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == 2:
            print("Adjust thresholds for Canny (default: 100 and 200)")

            
            display_image("Canny Edge Detection", edges)

        elif choice == 3:
            
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        elif choice == 4:
            print("Adjust kernel size for Gaussian blur (must be odd, default: 5)")

            

            display_image("Gaussian Smoothed Image", blurred)

        elif choice == 5:
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            
            

            display_image("Median Filtered Image", median_filtered)

        elif choice == 6:
            print("Exiting..")
            break

        else:
            print("Invalid choice. Please select a number between 1-6")

