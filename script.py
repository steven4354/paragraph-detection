import cv2
import time
import pytesseract

# Load the image
image = cv2.imread('image.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to the image
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)

# Use Tesseract OCR to extract data from the image
data = pytesseract.image_to_data(thresh)

# level	page_num	block_num	par_num	line_num	word_num	left	top	width	height	conf	text
headers = ['level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text']

for line in data.split('\n'):
    # skip the first line
    if line == data.split('\n')[0]:
        continue

    d = line.split()

    # if d is empty, skip it
    if not d:
        continue

    # get the bounding box coordinates and dimensions
    x, y, w, h = d[headers.index('left')], d[headers.index('top')], d[headers.index('width')], d[headers.index('height')]

    # make them all integers
    x, y, w, h = int(x), int(y), int(w), int(h)

    # Draw the bounding box on the image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the image with bounding boxes
cv2.imwrite('image_with_boxes.jpg', image)

while True:
    # Run the code to output bounding boxes around paragraphs or sections in the image
    # ...
    print("hello world")
    time.sleep(3)