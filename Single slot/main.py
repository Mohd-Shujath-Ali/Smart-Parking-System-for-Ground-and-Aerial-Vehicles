from ultralytics import YOLO
import cv2
import serial
import time

# ---------------- SERIAL Communication between laptop device to ESP32 ----------------
def connect_serial(port='COM3', baud=115200):
    while True:
        try:
            esp = serial.Serial(port, baud, timeout=1)
            time.sleep(2)
            print("Serial Connected")
            return esp
        except Exception as e:
            print("Serial Error:", e)
            time.sleep(2)

esp = connect_serial()

# ---------------- MODEL ----------------
try:
    model = YOLO("../Yolo-Weights/best.pt")
    classNames = model.names
except Exception as e:
    print("Model Load Failed:", e)
    exit()

# ---------------- Video Input ----------------
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

last_send_time = 0
SEND_INTERVAL = 0.2  # sts in  seconds

# ---------------- Working Loop ----------------
while True:
    success, img = cap.read()

    if not success:
        print("Camera Error - Retrying...")
        time.sleep(1)
        continue

    passenger = 0
    emergency = 0

    try:
        results = model(img, stream=True)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = classNames.get(cls, "").lower()

                if label == "passenger":
                    passenger = 1
                elif label == "emergency":
                    emergency = 1

    except Exception as e:
        print("Inference Error:", e)

    # -------- SERIAL SEND (THROTTLED) --------
    current_time = time.time()
    if current_time - last_send_time > SEND_INTERVAL:
        msg = f"P:{passenger},E:{emergency}\n"

        try:
            esp.write(msg.encode())
        except Exception:
            print("Serial Lost. Reconnecting...")
            esp = connect_serial()

        last_send_time = current_time

    # -------- Detection without bounding boxex --------
    cv2.imshow("Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------- Exiting ----------------
cap.release()
cv2.destroyAllWindows()
esp.close()