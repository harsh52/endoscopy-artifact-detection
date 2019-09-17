Author: Harsh Kumar

Date of completion: 03/08/2019

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
# Overview
-------------------------------
It was my Summer internship work to detect different type of artifact in endoscopy images, it was based on EAD2019 challenge.

### My task inculded:
-------------------------------
1. Read several research paper and analyse different type of object detection algorithms eg. YOLO, fastRcnn, Rcnn etc.

2. Implement and analyse the result and compare with the research papers.

3. Analyse the matrix such and iou,mAP and loss.

# Method
---------------------------------
To complete my task i have used YOLOv2 because it's iou,mAP was more as suggested in the research paper.
link: https://arxiv.org/pdf/1904.07073.pdf
To implement object detection model i have darknet framwork for object detection which is written in c.

# Dataset
-------------------------------------
Dataset was provided by my mentors which can be downoad from my google drive 
link: https://drive.google.com/open?id=1IFliSsmF_Srr0M5psR_XgF0uUK0Hdr5Y

About dataset:
The training dataset for detection consists in total 2147 annotated framesover all 7 artifact classes (Specularity, Saturation, artifact, contrast, blur, bubbles, instrument)
more info about dataset: https://arxiv.org/pdf/1905.03209.pdf

# implementation
-----------------------------------
Follow jupyter notebook: endoscopy_artifact_detection.ipynb.

# Python_Script_details:
---------------------------------
"slice_script.py" : extract usefull data from output2 folder such as(iou,map etc).

"process.py": generate train txt file and test txt file.

"easy_install_1.py", "easy_install_2.py": script to install required dependencies.







