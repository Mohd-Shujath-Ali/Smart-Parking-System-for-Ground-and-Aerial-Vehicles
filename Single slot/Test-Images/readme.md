##  Model Testing (Sample Images)

To enable easy verification of the detection pipeline, sample test images are provided.

### 📁 Directory Structure

Place all test images in:

```bash
Single Slot/Test-Images/
```

Example:

```bash
Single Slot/Test-Images/01.jpg
Single Slot/Test-Images/02.jpg
```

---

### ▶️ Run Test Script

Use the dedicated testing script:

```bash
python test.py
```

---

### 🧠 Test Script (`test.py`)

Create a separate file `Single Slot/test.py`:

```python
from ultralytics import YOLO
import cv2
import os

# Load the model
model = YOLO("../models/best.pt")

# Path to test images
test_path = "Test-Images"

images = [img for img in os.listdir(test_path) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

for img_name in images:
    img_path = os.path.join(test_path, img_name)
    img = cv2.imread(img_path)

    if img is None:
        print(f"Failed to load: {img_name}")
        continue

    # This Runs the inference
    results = model(img)

    # Plot the results (bounding boxes)
    annotated_frame = results[0].plot()

    print(f" Processed: {img_name}")

    cv2.imshow("Detection", annotated_frame)
    cv2.waitKey(0)

cv2.destroyAllWindows()
```

---

### ✅ Expected Behavior

* Displays detections with bounding boxes
* Supports:

  * Passenger vehicles
  * Emergency vehicles
* Processes images sequentially

---

### ⚠️ Requirements

* Ensure model weights are available at:

```bash
model/best.pt
```

* Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 💡 Notes

* This script isolates testing from the main pipeline (best practice)
* Supports quick validation without hardware dependencies
* Designed for reproducibility and ease of use
