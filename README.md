# YOLO-v3 Face detection. 

## This code is used for detecting and clipping human faces in batch of images and save the clipped faces in a separate folder for other usage.
## It also resize the clipped faces with respect to ratio to a custom size.


## Prerequisites

* Tensorflow
* opencv-python
* opencv-contrib-python
* Numpy
* Keras
* Matplotlib
* Pillow

$ pip install -r requirements.txt
```

## How to use the code.

* Clone this repository

$ git clone https://github.com/sthanhng/yoloface or download it as  zippfolder
```
1. Put the images contain faces to be detected in the images folder  in ".jpg" format.
2. Run   $ python detect_batch.py
3. all detcted face will be saved in the faces folder.
4. If you want to resize the faces to custom image size:
   Run $   python  batch_resize.py  [desired dimention]  ## for example 223 will resize all faces as (223x223) with respect to ratio.


![image1](/test1.jpg)
![clipped_faces](/1.png)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more details.


Note:
This code is modified from the original repository https://github.com/sthanhng/yoloface .

Credit to Thanh Nguyen
