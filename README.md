### 1. Where the Dataset Came From
To teach a computer to "see" a pothole, you need thousands of pictures of them. We used **Roboflow Universe**, which contains several datasets required. 
* **The Source:** We pulled a dataset often used in research called **RDD (Road Damage Dataset)**. 
* **The Labels:** Every image in that dataset came with "annotations." These are essentially coordinates.

### 2. How the Training Worked
We used **Google Colab** to do the heavy lifting.
* **The Model (YOLOv8 Nano):** We chose the Nano version of YOLO. It’s not the smartest model in the world, but it’s the fastest, which is perfect for a device moving at 40mph on a bus.
* **The Learning Process:** We ran the training for about 30 epochs.
* **The Result:** After 30 rounds, the model reached a point where it could see a new, unseen video of a road and accurately draw a box around a pothole.

### 3. The Workflow
Once the training finished, we got a file called `best.pt`. This file is the "trained brain" of our project. 

**The Step-by-Step Logic:**
1.  **Video Input:** The Python script opens a video file (simulating a live camera).
2.  **Frame-by-Frame Scanning:** The script chops the video into individual images (frames). 
3.  **The Detection:** It feeds each frame into the `best.pt` model. If the model sees a shape that matches its training, it draws a "Bounding Box" around it.
4.  **The Confidence Check:** The model only tells us if it is more than 50% sure. This prevents the AI from mistaking a shadow or a leaf for a pothole.


### 4. The Simulation
Because this is a prototype and we aren't actually driving a car with a GPS module right now, we **simulated** the connectivity. 
* **Fake GPS:** Every time the AI sees a pothole, the code generates a random set of coordinates near our current location.
* **Data vs. Video:** This is the most important part of your pitch. Instead of sending a 50MB video file to the city office (which would be expensive and slow), the prototype only sends a tiny text string (less than 1KB) containing the Location and the Time. 

**The Result:** A red pin drops on a digital map in real-time. That is the "Proof of Concept"—demonstrating that we can turn raw video into actionable data for city repairs.

You can also try this out by changing the path of the video in the .py file, and uploading a video which you would like to detect on. Make sure the best.pt and the .py files are at the same folder.
