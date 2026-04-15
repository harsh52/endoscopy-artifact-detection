# Endoscopy Artifact Detection

Detecting artifacts in endoscopy images using YOLOv2 — built during a summer internship based on the [EAD2019 challenge](https://arxiv.org/pdf/1905.03209.pdf).

## What It Does

Detects 7 types of artifacts in endoscopy frames: specularity, saturation, artifact, contrast, blur, bubbles, and instruments. Uses YOLOv2 via the Darknet framework for real-time object detection.

## Why YOLOv2

Compared multiple architectures (YOLO, Fast R-CNN, R-CNN). YOLOv2 had the best IoU and mAP scores, consistent with [this paper](https://arxiv.org/pdf/1904.07073.pdf).

## How to Run

```bash
# Follow the Jupyter notebook
endoscopy_artifact_detection.ipynb
```

Download the dataset from [Google Drive](https://drive.google.com/open?id=1IFliSsmF_Srr0M5psR_XgF0uUK0Hdr5Y) (2,147 annotated frames).

## Tech

Python, YOLOv2, Darknet (C), OpenCV, Jupyter
