# 💡 Web-Based Light Scheduler

A full-stack IoT dashboard to **schedule a light** ON/OFF using **WebSocket** and **MQTT** communication.


## ✨ Project Overview

This project simulates a real-world IoT dashboard where a user can **set ON and OFF times** for a light via a **browser interface**.  
The schedule is sent over **WebSocket** to a **Python server**, which forwards it via **MQTT** to a **Python subscriber**.  
The subscriber then sends commands to an **Arduino** board over **serial** to control a **relay**.

---

## 🏗️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (WebSocket client)
- **Backend:** Python (WebSocket server + MQTT publisher)
- **Communication:** WebSocket, MQTT (Mosquitto)
- **Hardware:** Arduino UNO (Serial Communication)
- **Libraries:** 
  - `websockets`
  - `pyserial`
  - `paho-mqtt`

---

## 📂 Project Structure

```plaintext
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── server.py (WebSocket server sending to MQTT)
│
├── subscriber/
│   ├── subscriber.py (MQTT subscriber forwarding to Arduino)
│
├── README.md
└── requirements.txt
