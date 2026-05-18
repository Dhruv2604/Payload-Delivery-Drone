import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')

cascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0)

while True:

    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2, 5)

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        if confidence < 50:
            print("AUTHORIZED - Payload Released")
        else:
            print("ACCESS DENIED")

    cv2.imshow('camera', img)

    if cv2.waitKey(10) & 0xff == 27:
        break

cam.release()
cv2.destroyAllWindows()
