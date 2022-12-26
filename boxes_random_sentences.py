import cv2

# Load the image
image = cv2.imread('image.png')

# Pre-process the image
# You can try different pre-processing techniques and see which one works best for your image
image = cv2.GaussianBlur(image, (5,5), 0)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the image
# Increase the blockSize parameter to smooth out the image and reduce noise
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 4)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through the contours and draw bounding boxes around the paragraphs
# Use the contourArea function to filter out contours that are too small or too large
for contour in contours:
    if cv2.contourArea(contour) > 500 and cv2.contourArea(contour) < 10000:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the image with bounding boxes
cv2.imwrite('image_with_boxes.jpg', image)

while True:
    # Run the code to output bounding boxes around paragraphs or sections in the image
    # ...
    print("hello world")