# Project Name
Traffic Sign Recognition 
### Project Description:
This project focuses on developing a system to detect and recognize traffic 
signs in images, helping autonomous vehicles navigate safely. The system 
uses color segmentation to identify regions with specific colors found in 
traffic signs and shape detection to classify them based on their geometry. 
By combining these techniques, the system can accurately recognize 
different traffic signs, even in challenging conditions. This work 
contributes to making autonomous driving safer and more reliable.
traffic sign detection and recognition system utilizing Histogram of Oriented Gradients feature 
extraction. It is quite robust in identification of the visual pattern based on edge 
orientation and intensity, becoming particularly 
effective at capturing characteristic properties specific to traffic signs.
#### Summary - 
This project involves developing a traffic sign recognition system aimed at assisting autonomous vehicles. The system uses Histogram of Oriented Gradients (HOG) for feature extraction and Canny Edge Detection for enhancing image contours. Key steps include:

Image Preprocessing: Images are resized and converted to grayscale for consistent feature extraction.
HOG Feature Extraction: Detects edges and gradients to capture the shape and structure of traffic signs while being robust to lighting variations.
Template Matching: Compares input images to predefined templates using Euclidean distance for classification.
Edge Detection: Canny edge detection dynamically adjusts thresholds to enhance object visibility under varying conditions.

#### Course concepts used - 
1. -basic image operations
2. -canny edge detection
3. -
   
#### Additional concepts used -
1. -HOG Feature Extraction
2. -Template Matching
   
#### Dataset - 
Link and/or Explanation if generated

#### Novelty - 
1. -The project introduces a combined approach of HOG feature extraction and auto-thresholded edge detection, offering a lightweight and real-time solution for object recognition.
2. -
3. -
   
### Contributors:
1. Eshaan Havanur (PES1UG22EC073)
2. Srikar Jois (PES1UG22EC100)

### Steps:
1. Clone Repository
```git clone https://github.com/Digital-Image-Processing-PES-ECE/project-name.git ```

2. Install Dependencies
```pip install -r requirements.txt```

3. Run the Code
```python main.py (for eg.)```

### Outputs:
* Important intermediate steps
* Final output images 

### References:
1. -P. Shopa, N. Sumitha and P. S. K. Patra, "Traffic sign detection and recognition 
using OpenCV," International Conference on Information Communication and 
Embedded Systems (ICICES2014), Chennai, India. 
2. -C. Taştimur, M. Karaköse, Y. Çelik and E. Akın, "Image processing based traffic 
sign detection and recognition with fuzzy integral," 2016 International Conference 
on Systems, Signals and Image Processing (IWSSIP), Bratislava, Slovakia
   
### Limitations and Future Work:
The method's effectiveness is constrained by template diversity and environmental complexity, making it ideal for controlled conditions but less suited to complex scenes.