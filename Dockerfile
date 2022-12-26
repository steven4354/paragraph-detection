FROM python:3.8

# Install OpenCV and other dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-dev libhdf5-dev
RUN pip install opencv-python
RUN pip install pytesseract

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Install language-specific data files
RUN apt-get update && apt-get install -y tesseract-ocr-eng tesseract-ocr-spa

# Set the Tesseract data path
ENV TESSDATA_PREFIX /usr/share/tesseract-ocr/4.00/tessdata

# Create a working directory and copy the script
RUN mkdir /app
COPY script.py /app/
COPY image.png /app/

# Set the working directory and run the script
WORKDIR /app
CMD ["python", "-u", "script.py"]
