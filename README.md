# 🚦 Traffic Sign Recognition (TSR)

Traffic Sign Recognition (TSR) is a feature of Advanced Driver Assistance Systems (ADAS). When I originally worked on this project in **2021**, TSR was mostly found in high-end vehicles like those from Tesla. 

However, by the time you're reading this README, TSR has likely become a **standard feature** in most modern automobiles 🚘.

This repository is a **revamp** of my original college project from 2021, now being improved and updated in **2025**.

---

## 🧠 About the Project

At a high level, this project detects **traffic signboards** from images or video input and provides **voice alerts** based on the recognized signs.  

📢 *Example*:  
If a **"School Ahead"** sign is detected, the model will generate a voice message like:  
**"School ahead — go slow."**


## 🎯 Objectives

### A. 📊 Dataset Preparation for Indian Traffic Signs

- The datasets available in kaggle are mainly from countries where they are having good highways. But contradictory Indian roads are still developing and emerging. 
- One of my observation is that restricted signs like no U turn, Construction Ahead, Multiple roads merging, No parking, One way is rarely used in these countries.
- Moreover, India's diverse geographical landscape -  including terrains, mountains, coastal areas, and rural roads - necessitates a wider variety of traffic signs. 
- Unlike many countries where signs are often circular or rectangular, Indian traffic signs frequently use triangular shapes, especially for warnings.

All these factors highlight the need for custom dataset preparation tailored to Indian road conditions and signage diversity.  

### B. 🤖 Model Evaluation

- Experiment with different **machine learning** and **deep learning** algorithms.
- Evaluate performance based on:
  - Accuracy
  - Speed
  - Robustness in real-world conditions

---

### C. 🎥 Real-world Testing

- Test the trained model with:
  - 🖼️ Static images
  - 📹 Recorded videos
  - 📷 Live webcam input

Voice alerts will be generated accordingly for detected signs.

---

## 📥 Clone the Repository

To get started, clone this repository with:

```bash
git clone https://github.com/Robin005cr/traffic_sign_recognition.git