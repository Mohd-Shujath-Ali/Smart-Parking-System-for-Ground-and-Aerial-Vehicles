# Smart Parking System for Ground and Aerial Vehicles

A computer-vision and sensor-assisted smart parking and reservation system designed for environments where **ground vehicles and aerial vehicles** share intelligent parking infrastructure.

The project combines **YOLOv8-based vehicle detection, sensor-based slot verification, ESP32 control, Firebase cloud synchronization and fail-safe mechanisms**. The current prototype is validated using accessible hardware, while NVIDIA Jetson Orin Nano Super and Benewake TF03-180 LiDAR are planned for future edge deployment.

---

## Overview

Conventional parking systems are designed mainly for ground vehicles. This project explores an infrastructure model that can support both conventional vehicles and future aerial vehicles such as UAVs/eVTOLs.

The system is designed around four main objectives:

- Detect and classify vehicles using computer vision.
- Verify parking-slot occupancy using multiple sensing inputs.
- Synchronize slot states and reservations through cloud services.
- Maintain safe operation through health monitoring and fail-safe logic.

---

## Key Features

### Computer Vision
- Custom-trained **Ultralytics YOLOv8L** object detection model.
- Vehicle classes include:
  - `Passenger`
  - `Emergency`
- Image labelling and dataset preparation.
- Data augmentation for improved model robustness.
- Detection evaluation using:
  - Precision
  - Recall
  - mAP@50
  - mAP@50–95
  - F1-score
  - Inference latency

### Slot Validation
Each prototype parking slot uses multiple sensing inputs for occupancy verification.

The validation logic is designed to reduce false positives by combining:

`Camera Detection + Sensor Verification`

A vehicle is considered present only when the required sensing conditions are satisfied.

### Fail-Safe Operation
The system continuously monitors sensor and detection health.

Examples include:
- Sensor heartbeat/response monitoring.
- YOLO health monitoring.
- Degraded operation when one sensing component fails.
- Local operation when cloud communication becomes unavailable.
- Buzzer-based warning for unsafe vehicle movement.

### Cloud Synchronization
The system supports cloud-based parking-state management using:

- **Firebase**
- **REST/API-based communication**

Slot information can include:
- `AVAILABLE`
- `OCCUPIED`
- `RESERVED`
- `EMERGENCY`
- Fail-safe status
- Sensor health
- Detection-system health
- Timestamp

### Administrative Control
The project includes administrative control and monitoring functionality for:
- Slot status
- Sensor status
- YOLO health
- Heartbeat checks
- Reservation/release operations
- Fail-safe activation
- Emergency/disaster handling

---

## System Architecture

The system can be viewed as the following pipeline:

```text
Camera
   │
   ▼
YOLOv8L Detection
   │
   ├── Vehicle Class
   ├── Confidence
   └── Detection Status
   │
   ▼
Sensor Verification
   │
   ├── Sensor 1
   └── Sensor 2
   │
   ▼
Fusion / Decision Logic
   │
   ├── Slot Status
   ├── Safety Status
   └── Alert Status
   │
   ▼
ESP32 / Control Layer
   │
   ├── RGB Indicators
   ├── Buzzer
   └── Communication
   │
   ▼
Firebase / REST
   │
   ▼
User & Admin Interface
```

---

## Current Experimental Setup

The current implementation was tested using accessible development hardware rather than the planned final edge platform.

### Current Hardware
- Intel i5-12450HX development laptop
- NVIDIA RTX 3050 GPU, 6 GB VRAM
- 16 GB RAM
- ESP32-WROOM
- HP Webcam W300, 1080p, 30 FPS
- HC-SR04 ultrasonic sensors
- Prototype power and indicator components

### Planned Hardware
- NVIDIA Jetson Orin Nano Super for edge inference and system control
- Benewake TF03-180 LiDAR for long-range ranging and motion sensing

The distinction between **current experimental hardware** and **planned deployment hardware** is intentional so that experimental results remain reproducible and clearly reported.

---

## Machine Learning Pipeline

### 1. Dataset Preparation
The computer-vision pipeline includes:

1. Image collection
2. Manual image labelling
3. Class assignment
4. Dataset splitting
5. Image preprocessing
6. Data augmentation
7. Model training
8. Validation and testing

The research dataset contains **1,500 images**, divided between the `Passenger` and `Emergency` classes, with an **80/10/10 train-validation-test split**.

### 2. Training Configuration

| Parameter | Value |
|---|---|
| Model | Ultralytics YOLOv8L |
| Training epochs | 150 |
| Batch size | 71 |
| Input resolution | 800 × 800 px |
| Confidence threshold | 0.85 |
| Optimizer | AdamW |
| Initial learning rate | 0.001667 |
| Momentum | 0.9 |

### 3. Evaluation

The models are evaluated using standard object-detection metrics:

- Precision
- Recall
- F1-score
- mAP@50
- mAP@50–95
- Inference latency

---

## Prototype Safety Logic

The prototype uses redundant sensing at the slot level.

### Normal Operation

```text
YOLO detects vehicle
        AND
Sensor 1 confirms
        AND
Sensor 2 confirms
        │
        ▼
Slot = OCCUPIED
```

### Partial Sensor Failure

```text
Sensor health check
        │
        ├── Sensor 1 = OK
        └── Sensor 2 = FAIL
                 │
                 ▼
        Admin notification
                 │
                 ▼
     Degraded validation mode
```

The prototype also includes a buzzer-based warning mechanism for unsafe movement outside the designated parking region.

---

## Cloud Communication

The system uses cloud synchronization to maintain a common view of parking-state information.

A typical slot-status payload may contain:

```json
{
  "helipad_id": "H01",
  "slot_id": "S01",
  "status": "AVAILABLE",
  "vehicle_class": null,
  "yolo_status": "OK",
  "sensor_status": "OK",
  "failsafe": false,
  "timestamp": "..."
}
```

Actual implementation fields may vary as the system evolves.

---

## Performance Results

The research evaluation reported strong model and system-level performance.

### Best YOLOv8 Configuration

| Metric | Result |
|---|---:|
| Precision | 0.982 |
| Recall | 0.985 |
| mAP@50 | 0.988 |
| mAP@50–95 | 0.874 |
| F1-score | 0.984 |

The reported prototype-level system evaluation achieved an **end-to-end latency of 86.5 ms** and **99.8% slot-validation accuracy**.

These values should be interpreted in the context of the prototype hardware and experimental conditions described above.

---

## Technologies Used

**Programming**
- Python
- C/C++ for embedded development

**Machine Learning / Computer Vision**
- Ultralytics YOLOv8
- PyTorch
- OpenCV

**Data Analysis**
- NumPy
- Pandas
- Matplotlib
- Seaborn

**Embedded / Hardware**
- ESP32-WROOM
- HC-SR04
- Camera-based sensing

**Cloud / Communication**
- Firebase
- REST/API communication

---

## Research Outcomes

This project resulted in:

- Research publication associated with the **6th International Conference on Mobile Radio Communications & 5G Networks (MRCN-2025)**.
- Publication in Springer's **Lecture Notes in Networks and Systems (LNNS)** series.
- Related patent filing for the smart aerial parking system.

### Publication

**Smart Parking and Reservations System for Aerial Vehicles**

DOI: `https://doi.org/10.1007/978-3-032-31097-2_36`

---

## Future Development

Planned extensions include:

- Deployment on **NVIDIA Jetson Orin Nano Super**.
- Integration of **Benewake TF03-180 LiDAR**.
- Improved datasets with greater environmental and viewpoint diversity.
- Advanced vision–LiDAR fusion.
- More extensive latency and reliability testing.
- Secure reservation and vehicle authentication.
- VANET-based I2V/V2I communication.
- Bloom Filter-based vehicle verification.
- Blockchain-based reservation and payment integrity.
- Dynamic pricing and emergency slot management.
- Expansion toward multi-vertiport and city-scale coordination.

---

## Project Status

**Current status:** Research prototype with experimental validation and ongoing system development.

The repository should distinguish clearly between:

- **Implemented and experimentally validated components**
- **Prototype components**
- **Planned/future components**

This distinction is important for reproducibility and for accurately representing the research.

---

## Disclaimer

This repository represents an academic research and prototype-development project. It is not intended to provide certified aviation, landing-control, or safety-critical flight functionality. Real-world deployment would require appropriate hardware validation, aviation certification, cybersecurity assessment, and regulatory approval.

---

## Author

**Mohammed Shujath Ali**  
B.Tech Computer Science and Engineering  
Lovely Professional University

- LinkedIn: [Mohammed Shujath Ali](www.linkedin.com/in/mohammed-shujath-ali)
- GitHub: [Mohd-Shujath-Ali](https://github.com/Mohd-Shujath-Ali)

---

## Citation

If you use or reference this project, please cite the associated publication:

```text
Ali, M. S., Kumar, R., Joshi, R.:
Smart Parking and Reservations System for Aerial Vehicles.
Mobile Radio Communications and 5G Networks.
Lecture Notes in Networks and Systems, 2030 (2026).
https://doi.org/10.1007/978-3-032-31097-2_36
```
