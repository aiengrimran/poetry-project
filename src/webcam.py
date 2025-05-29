import cv2 as cv

cap = cv.VideoCapture(0)
while True:
    ret, frame =cap.read()
    if not ret:
        break
    cv.imshow('Live Cam', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()

