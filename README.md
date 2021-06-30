<p>
This is a personal implementation of YOLO v5 by Pi.
</p>

Python >= 3.6.0 required with all [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) dependencies installed:

To test the repository, run these commands first.

```bash
$ git clone https://github.com/Pi-31415/yolo-personal
$ cd yolov5
$ pip3 install -r requirements.txt
```

Then, place the image you want to test into the yolov5 folder. In this case, it is called 439.png.

Then run the detect command.

```
$ python3 detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.25 --source '439.png'
```

The result will be in runs/detect/exp (read the terminal output for exact location)
