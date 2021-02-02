import cv2
import imutils
img = cv2.imread(r"bongbay.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thres = cv2.adaptiveThreshold(\
    gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY_INV,21,10)

contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)

# cv2.drawContours(img, contours,-1,(0,255,0),2)

#cv2.drawContours(img, contours,-1, (0,255,0),2)
number = 0
# Lắp qua các contours
for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    #  Kiểm tra điều kiện
    if (85<w<150) and(100<h<150):
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        number += 1
print("so bong =",number)
cv2.imshow("Gray",gray)
cv2.imshow("Thres",thres)
cv2.imshow("Pic",img)
cv2.waitKey()
cv2.destroyAllWindows()