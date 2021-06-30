
<br>
<p>
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents <a href="https://ultralytics.com">Ultralytics</a>
 open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</p>

Python >= 3.6.0 required with all [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) dependencies installed:


```bash
$ git clone https://github.com/ultralytics/yolov5
$ cd yolov5
$ pip3 install -r requirements.txt
```

```
$ python3 detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.25 --source '439.png'
```

