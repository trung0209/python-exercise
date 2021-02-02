import cv2
import imutils
video_file = r"C:\Users\Asus\Documents\sample.mp4"

video = cv2.VideoCapture(0)

current_angle = 0

while (video.isOpened()):
    ret, frame = video.read()
    if ret:
        if current_angle != 0:
            frame = imutils.rotate(frame,current_angle)
        cv2.imshow("Video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("a"):
        current_angle = 90
    elif key == ord("d"):
        current_angle = -90
    elif key == ord("s"):
        current_angle = 0
        
video.release()
cv2.destroyAllWindows()