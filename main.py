import cv2
import numpy as np

# Name of the QR Code Image file
filename = "2.jpg"

# read the QRCODE image
img = cv2.imread(filename)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.bilateralFilter(gray, 9, 75, 75)

# Apply adaptive thresholding to segment the QR code from the background
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort the contours by area in descending order
contours = sorted(contours, key=cv2.contourArea, reverse=True)
for cnt in contours:
    # Check the area of the contour
    if cv2.contourArea(cnt) < 1000:  # Skip small contours
        continue
# Loop over the sorted contours
    for cnt in contours:
        # Approximate the contour to a polygon
        approx = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)

        # If the polygon has four vertices, it may be a QR code
        if len(approx) == 4:
            # Draw the polygon on the image
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 3)

            # Get the perspective transform matrix
            pts1 = np.float32([approx[0], approx[1], approx[2], approx[3]])
            pts2 = np.float32([[0, 0], [0, 300], [300, 300], [300, 0]])
            M = cv2.getPerspectiveTransform(pts1, pts2)

            # Warp the image using the perspective transform matrix
            qr_code = cv2.warpPerspective(gray, M, (300, 300))

            # Initialize the QRCodeDetector
            detector = cv2.QRCodeDetector()

            # Detect and decode the QR code
            data, vertices_array, binary_qrcode = detector.detectAndDecode(qr_code)
            print(len(data))
            # If QR code is detected
            if vertices_array is not None:
                print("QR Code Data: ", data)
                break

# Display the image with contours and QR code highlighted
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


if __name__ == "__main__":
    pass

