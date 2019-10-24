# YOLO-v3 Face detection. This code is used for detecting and clipping human faces in batch of images and save the clipped faces in a separate folder for other usage.
It also resise the clipped faces with respict to ratio to a custom size.


#This code is modified fro the original repository of  https://github.com/sthanhng. 
 

## Getting started

The YOLOv3 (You Only Look Once) is a state-of-the-art, real-time object detection algorithm. The published model recognizes 80 different objects in images and videos. For more details, you can refer to this [paper](https://pjreddie.com/media/files/papers/YOLOv3.pdf).

## YOLOv3's architecture

![Imgur](assets/yolo-architecture.png)

Credit: [Ayoosh Kathuria](https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)

## Prerequisites

* Tensorflow
* opencv-python
* opencv-contrib-python
* Numpy
* Keras
* Matplotlib
* Pillow

- For Ubuntu
```bash
$ pip install virtualenv
```


Install the dependencies for the this project:
```bash
$ pip install -r requirements.txt
```

## Usage

* Clone this repository
```bash
$ git clone https://github.com/sthanhng/yoloface
```

* Run the following command:

>**image input**
```bash
$ python yoloface.py --image samples/outside_000001.jpg --output-dir outputs/
```

>**video input**
```bash
$ python yoloface.py --video samples/subway.mp4 --output-dir outputs/
```

>**webcam**
```bash
$ python yoloface.py --src 1 --output-dir outputs/
```

## Sample outputs

![Imgur](assets/outside_000001_yoloface.jpg)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for more details.

## References

