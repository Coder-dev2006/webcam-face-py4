# Webcam Face Detection with Heatmap

**Author:** Samandar  -> github.com/Coder-dev2006

This project performs **real-time face detection** using a webcam and visualizes a **heatmap** of the camera feed. It is designed for computer vision enthusiasts and educational purposes.  

---

##  Features

- Real-time **face detection** using Haar Cascade.  
- **Heatmap visualization** of the webcam feed.  
- Simulated **average face temperature** (0-255) displayed on each detected face.  
- Two separate windows:  
  1. **Face Detection** — shows faces with green rectangles.  
  2. **Heatmap with Face Temp** — shows heatmap and face temperature values.

---

##  Requirements

- Python 3.7+  
- OpenCV  
- NumPy  

### Installation:

```bash
pip install opencv-python numpy
 How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
Run the script:

bash
Copy code
python face_heatmap.py
Two windows will open:

Face Detection: faces outlined in green.

Heatmap with Face Temp: shows the simulated heatmap and average face temperature.

Press 'q' to quit.

 Example
Face Detection: Green rectangles highlight detected faces.

Heatmap with Face Temp: Color-coded heatmap with temperature labels on faces.

 Technologies
OpenCV — Computer vision and video processing

NumPy — Array and mathematical operations

 License
This project is licensed under the MIT License.
