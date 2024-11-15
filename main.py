import cv2
eye = "haarcascade_eye.xml"
video = cv2.VideoCapture("faces.mp4")

model = cv2.CascadeClassifier(eye)
while True:
    ret,bg = video.read()
    gray = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
    cars = model.detectMultiScale(gray, 4, 2)
    for x, y, w, h in cars:
        cv2.rectangle(bg, (x,y), (x+w, y+h), (230, 25, 189), 2)
    cv2.imshow("screen", bg)
    k = cv2.waitKey(20)
    if k == 27:
        break