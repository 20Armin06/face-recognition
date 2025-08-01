import face_recognition as f , cv2

pic        = f.load_image_file("name.png")
pic_encode = f.face_encodeings(pic)[0]

cap = cv2.VideoCapture(0)

while 1:
    s,f = cap.read()

    if not s:
        break
    small_frame   = cv2.resize(f,(0,0),fx=0.25,fy=0.25)
    face_location = f.face_location(small_frame)
    face_encoding = f.face_encodeings(small_frame,face_location)
    for (top,right,bottom,left) , d2 in zip (face_location,face_encoding):
        name = "nashenas"
        if True in f.compare_faces([pic_encode],d2):
            name = "name"

        top , right , bottom , left = top*4 , right*4 , bottom*4 , left*4
        cv2.rectangle(f,(left,top),(right,bottom),(0,255,0),2)
        cv2.putText(f,name,(left,top - 10),cv2.FONT_HERSHEY_DUPLEX,1,(255,255,255),2)

        cv2.imshow("Detect Face",f)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()