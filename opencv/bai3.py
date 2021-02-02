import cv2

camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml")
def save_to_file(frame,faces):
    i = 0
    for (x,y,w,h) in faces:
        i = i+1
        cropped = frame[y:y+h,x:x+w]
        cv2.imwrite(f"face{cropped}.png",cropped)
        print("Save face")
    return
while True:
    ret, frame = camera.read()
    if ret:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.2,10,minSize=(100,100))
        # print("So khuon mat",len(faces))
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("Video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        save_to_file(frame,faces)
camera.release()
cv2.destroyAllWindows()