<div align="center">
<p>
<a align="left" href="https://ultralytics.com/yolov5" target="_blank">
<img width="850" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/splash.jpg"></a>
</p>
<br>
<div>
<a href="https://github.com/ultralytics/yolov5/actions"><img src="https://github.com/ultralytics/yolov5/workflows/CI%20CPU%20testing/badge.svg" alt="CI CPU testing"></a>
<a href="https://zenodo.org/badge/latestdoi/264818686"><img src="https://zenodo.org/badge/264818686.svg" alt="Open In Kaggle"></a>
<br>  
<a href="https://colab.research.google.com/github/ultralytics/yolov5/blob/master/tutorial.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
<a href="https://www.kaggle.com/ultralytics/yolov5"><img src="https://kaggle.com/static/images/open-in-kaggle.svg" alt="Open In Kaggle"></a>
<a href="https://hub.docker.com/r/ultralytics/yolov5"><img src="https://img.shields.io/docker/pulls/ultralytics/yolov5?logo=docker" alt="Docker Pulls"></a>
</div>
  <br>
  <div align="center">
    <a href="https://github.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-github.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.linkedin.com/company/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-linkedin.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://twitter.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-twitter.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://youtube.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-youtube.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.facebook.com/ultralytics">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-facebook.png" width="2%"/>
    </a>
    <img width="2%" />
    <a href="https://www.instagram.com/ultralytics/">
        <img src="https://github.com/ultralytics/yolov5/releases/download/v1.0/logo-social-instagram.png" width="2%"/>
    </a>
</div>

<br>
<p>
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents <a href="https://ultralytics.com">Ultralytics</a>
 open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</p>

<!-- 
<a align="center" href="https://ultralytics.com/yolov5" target="_blank">
<img width="800" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-api.png"></a>
-->

</div>


## <div align="center">Documentation</div>

See the [YOLOv5 Docs](https://docs.ultralytics.com) for full documentation on training, testing and deployment.


## <div align="center">Quick Start Examples</div>


<details open>
<summary>Install</summary>

Python >= 3.6.0 required with all [requirements.txt](https://github.com/ultralytics/yolov5/blob/master/requirements.txt) dependencies installed:
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->
```bash
$ git clone https://github.com/ultralytics/yolov5
$ cd yolov5
$ pip install -r requirements.txt
$ python3 detect.py --weights runs/train/exp2/weights/last.pt --img 640 --conf 0.25 --source 'image.jpg'
```
</details>

