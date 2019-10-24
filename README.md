# YOLO-v3 Face detection. This code is used for detecting and clipping human faces in batch of images and save the clipped faces in a separate folder for other usage.
# It also resize the clipped faces with respict to ratio to a custom size.


#This code is modified from the original repository of  https://github.com/sthanhng. 
# Credit and thanks to Thanh Nguyen, 2018 (https://towardsdatascience.com/yolo-v3-object-detection-53fb7d3bfe6b)

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

