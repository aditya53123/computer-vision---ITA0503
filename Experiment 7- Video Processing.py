import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(100)  # Slow motion

    if key == ord('f'):
        cv2.waitKey(10)      # Fast motion

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
