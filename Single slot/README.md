# Smart Parking & Reservation System (v1)

A real-time smart parking system integrating computer vision and IoT to manage parking slot occupancy and reservations for both ground and aerial vehicles.

---

## 📌 Introduction

Urban congestion and the rise of aerial mobility demand intelligent parking solutions.
This project presents a hybrid system that combines **YOLOv8-based object detection**, **sensor validation**, and **real-time state management** to enable accurate and automated parking control.

The system is designed as a **single-slot prototype (v1)**, demonstrating real-time detection, booking, and fail-safe mechanisms.

---

## ⚙️ Features

* 🧠 YOLOv8-based vehicle detection (passenger / emergency) classes
* 🔄 Real-time slot status using Firebase Realtime Database
* 🔒 Concurrency-safe booking using transactional updates
* ⚡ Fault-tolerant pipeline with hardware (ESP32) communication
* 🚨 Emergency override handling

---

## 🧠 Tech Stack

* **Computer Vision:** YOLOv8 (Ultralytics), OpenCV
* **Backend:** Python
* **Database:** Firebase Realtime Database
* **Hardware:** ESP32 (Serial Communication)
* **Frontend:** HTML, JavaScript

---

## 🚀 Usage

### 1. Clone Repository

```bash
git clone https://github.com/Mohd-Shujath-Ali/Smart-Parking-System-for-Ground-and-Aerial-Vehicles.git
cd Smart-Parking-System-for-Ground-and-Aerial-Vehicles/Single Slot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Model Weights

Download model and place it here:

```bash
models/best.pt
```

### 4. Run Backend

```bash
python main.py
```

### 5. Run Frontend

Open:

```bash
Single Slot/index.html
```

---

## 🧪 Model Testing

To test using sample images:

```bash
Single Slot/Test-Images/
python test.py
```

---

## 💡 Use Cases

* 🏙️ Smart city parking systems
* 🚁 Urban Air Mobility (UAM) vertiports
* 🚑 Emergency vehicle priority parking
* 🏢 Automated parking management in commercial spaces

---

## 📊 Results

* ✅ **99.8% slot-validation accuracy** using multi-sensor fusion 
* 🎯 High detection performance across passenger and emergency classes
* ⚡ Real-time system behavior with reliable state synchronization
* 🔁 Robust fail-safe handling for hardware and detection failures

---

## 📊 Training Results

<p align="center">
  <img src="https://github.com/Mohd-Shujath-Ali/Smart-Parking-System-for-Ground-and-Aerial-Vehicles/blob/main/Single%20slot/model/result.png?raw=true" width="650"/>
</p>
<p align="center"><b>Figure:</b> Training metrics including loss, precision, recall, and mAP</p>

<p align="center">
  <img src="https://github.com/Mohd-Shujath-Ali/Smart-Parking-System-for-Ground-and-Aerial-Vehicles/blob/main/Single%20slot/model/confusion.png?raw=true" width="650"/>
</p>
<p align="center"><b>Figure:</b> Confusion matrix showing class-wise prediction accuracy</p>
<p align="center">
  <img src="https://github.com/Mohd-Shujath-Ali/Smart-Parking-System-for-Ground-and-Aerial-Vehicles/blob/main/Single%20slot/model/live.png?raw=true" width="650"/>
</p>
<p align="center"><b>Figure:</b> Individual class detection</p>
<p align="center">
  <img src="https://github.com/Mohd-Shujath-Ali/Smart-Parking-System-for-Ground-and-Aerial-Vehicles/blob/main/Single%20slot/model/batch.jpg?raw=true" width="650"/>
</p>
<p align="center"><b>Figure:</b> Batch inference results demonstrating detection on sample images</p>

---
## 📦 Model Weights

Model weights are not included due to size limitations.

👉 [Download from here ](https://drive.google.com/file/d/1mG93OUn4HF7QOBRiyp8tkqiRHBc1bLMj/view?usp=sharing)

Place in:

```bash
models/best.pt
```

---

## ⚠️ Limitations

* Single-slot implementation (v1)
* No authentication system till now
* Limited real-world deployment testing

---

## 🔮 Future Improvements

* Multi-slot and multi-user support
* Scalable backend APIs
* Mobile application integration
* Enhanced robustness under challenging environments

---

## 👨‍💻 Author

Mohammed Shujath Ali
