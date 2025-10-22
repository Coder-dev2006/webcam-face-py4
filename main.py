import cv2
import numpy as np

def run_face_heatmap_with_temp(camera_index=0):
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Kamera ochilmadi. Kamera indexini tekshiring (0, 1, ...).")
        return

    print("Kamera ishga tushdi. Chiqish uchun 'q' ni bosing.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Kadr olinmadi, to'xtatildi.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # ----------------------
        # 1 . find face 
        # ----------------------
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )
        face_frame = frame.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(face_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Face Detection", face_frame)

        # ----------------------
        # 2 . heatmap + face heat
        # ----------------------
        heatmap = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
        heatmap_overlay = heatmap.copy()

        for (x, y, w, h) in faces:
            face_region = gray[y:y+h, x:x+w]
            mean_temp = int(np.mean(face_region))  # 0-255 o'lchov
            cv2.putText(
                heatmap_overlay,
                f"Yuz issiqligi: {mean_temp}",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 255, 255),
                2
            )
            cv2.rectangle(heatmap_overlay, (x, y), (x+w, y+h), (255, 255, 255), 2)

        cv2.imshow("Heatmap with Face Temp", heatmap_overlay)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_face_heatmap_with_temp()
