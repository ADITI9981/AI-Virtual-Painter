<h1 align="center">🖌️ AI Virtual Painter</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/MediaPipe-Hands-orange?style=for-the-badge&logo=google" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

> Draw on the screen with your fingers in real time—no mouse required. Uses **OpenCV** + **MediaPipe Hands** to detect gestures and paint on a virtual canvas. 🎨

---

## ✨ Features
- ✋ **Gesture-based controls:** select color, draw, erase, clear canvas  
- 🎯 **Robust hand tracking** with stable landmarks  
- ⚡ **Low-latency** drawing with webcam input  
- 💾 (Optional) **Save artwork** as images

---

## 🖼️ Preview (Images)  

<p align="center">
<img src="https://github.com/user-attachments/assets/a0d0bef3-adc4-4f63-a66b-8a7c46e79c62" width="32%" />
<img src="https://github.com/user-attachments/assets/3f1a8bc6-6398-45f2-a8a7-4dbf24f06ee3" width="32%" />
<img src="https://github.com/user-attachments/assets/702902f9-7bc0-47fd-a5db-528cb5a87e0e" width="32%" />
</p>

---

## 🎥 Demo
<p align="center">
  <!-- Replace with your video or GIF -->
  <video src="https://github.com/user-attachments/assets/3faa642a-4910-4f82-9c35-de658c9d46bb" width="45%" controls></video><br/>
  <em>Real-time drawing using finger gestures</em>
</p>

<p align="center">
  <!-- Replace with your video or GIF -->
  <video src="https://github.com/user-attachments/assets/f184a263-8380-4698-b9b7-f2abd031d8e7
" width="45%" controls></video><br/>
  <em>Real-time drawing using finger gestures</em>
</p>

---

## 🧠 Gesture Guide (Default)
- **Index finger up** → Draw  
- **Index + Middle up** → Selection mode (choose color/thickness)  
- **Pinch** (thumb + index close) → Erase (or toggle eraser mode)  
- **Three fingers up** → Clear canvas *(optional mapping)*

> You can tweak gestures in the config section of the code.

---

## 🚀 Quick Start

```bash
# 1) Clone
git clone https://github.com/your-username/AI-Virtual-Painter.git
cd AI-Virtual-Painter

# 2) (Optional) Create venv
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install deps
pip install -r requirements.txt

# 4) Run
python painter.py
