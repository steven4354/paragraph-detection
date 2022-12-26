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

# Initialize a list to store the lines
lines = []

for line in data.split('\n'):
    # skip the first line
    if line == data.split('\n')[0]:
        continue

    d = line.split()

    # if d is empty, skip it
    if not d:
        continue

    # add the line to the list
    lines.append(d)

# Initialize a list to store the distances between the top positions of consecutive lines
distances = []

# Iterate through the lines
for i, line in enumerate(lines):
    # Skip the first line
    if i == 0:
        continue

    # Get the top position of the current line and the previous line
    current_top = line[headers.index('top')]
    prev_top = lines[i - 1][headers.index('top')]

    # Calculate the distance between the top positions and add it to the list
    distance = abs(int(current_top) - int(prev_top))
    distances.append(distance)

# # Sort the list of distances
# distances.sort()
print("distances: ", distances)

# Take the median value of the distances
average_distance = sum(distances) / len(distances)

# print the median distance
print("avg distance: ", average_distance)

# Initialize a list to store the paragraphs
paragraphs = []

# Iterate through the lines
for i, line in enumerate(lines):
    # If this is the first line, start a new paragraph
    if i == 0:
        paragraphs.append([line])
        continue

    # Get the top position of the current line and the previous line
    current_top = line[headers.index('top')]
    prev_top = lines[i - 1][headers.index('top')]

    # make current_top and prev_top integers
    current_top = int(current_top)
    prev_top = int(prev_top)

    # If the top position of the current line is within a certain distance of the previous line, add it to the current paragraph
    if abs(current_top - prev_top) < (average_distance * 5):
        paragraphs[-1].append(line)
    # Otherwise, start a new paragraph
    else:
        paragraphs.append([line])

# print just the text of the paragraphs
# try catch the error and print the error
for paragraph in paragraphs:
    paragraph_to_print = ''
    try:
        # print(' '.join([line[headers.index('text')] for line in paragraph]))
        # print the text in each line
        for line in paragraph:
            # check if line[headers.index('text')] is not out of range
            try:
                if line[headers.index('text')] != '':
                    # print(line[headers.index('text')])
                    # add the text to paragraph_to_print
                    paragraph_to_print += line[headers.index('text')] + ' '
            except Exception as e:
                # print(e)
                pass
    except Exception as e:
        print(e)

    # print the paragraph_to_print
    print(paragraph_to_print)

    # repeated print some line breaks
    print(' ')
    print(' ')
    print(' ')

# Save the image with bounding boxes
cv2.imwrite('image_with_boxes.jpg', image)

while True:
    # Run the code to output bounding boxes around paragraphs or sections in the image
    # ...
    print("just keep printing....")
    time.sleep(3)