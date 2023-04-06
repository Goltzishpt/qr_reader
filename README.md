# QR Code Detector

This is a Python script that detects and decodes QR codes from an image using OpenCV and the QRCodeDetector.

## Installation
* Clone the repository: git clone https://github.com/Goltzishpt/qr_reader
* Navigate to the project directory: cd qr-code-detector
* Install the required dependencies: pip install opencv-python-headless numpy

## Usage
* Save the QR code image file to the project directory with the name "qrcode.jpg".
* Run the script: python qr_code_detector.py
* The QR code data will be printed to the console and the image with the QR code highlighted will be displayed.

## How it works
The script first reads the QR code image and converts it to grayscale. It then applies adaptive thresholding to segment the QR code from the background, and finds the contours in the thresholded image. The contours are sorted by area in descending order, and the script loops over the contours to find a polygon with four vertices, which may be a QR code. If a polygon with four vertices is found, the script draws the polygon on the image, gets the perspective transform matrix, and warps the image using the perspective transform matrix. The QRCodeDetector is then initialized, and used to detect and decode the QR code from the warped image. If a QR code is detected, the QR code data is printed to the console and the script exits.

### License
This project is licensed under the MIT License. See the LICENSE file for more information.
