import cv2


def cartoonize_image(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Resize the image (optional, but often used to standardize processing)
    img = cv2.resize(img, (500, 500)) # Resizes the image to 500x500 pixels

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5) # Applies a 5x5 median filter

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    # 255: Maximum pixel value
    # cv2.ADAPTIVE_THRESH_MEAN_C: Threshold value is the mean of the neighborhood area minus the constant C.
    # cv2.THRESH_BINARY: Pixel values above the threshold are set to maxval, others to 0.
    # 9: Block size used to calculate the threshold.
    # 10: Constant subtracted from the mean.

    # Apply bilateral filter to smooth colors
    color = cv2.bilateralFilter(img, 9, 250, 250)
    # 9: Diameter of each pixel neighborhood.
    # 250: SigmaColor (filter sigma in the color space).
    # 250: SigmaSpace (filter sigma in the coordinate space).

    # Combine edges and color using bitwise AND
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display the cartoonized image
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

# Example usage (replace "your_image.jpg" with the actual image path)
cartoonize_image("image.jpg")