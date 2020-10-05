# NTI logo detector
Script find NTI logo in image

![alt text](https://sun9-49.userapi.com/C8H9px3ownzw2l4RsejGveeLn31xvnOlEgWZyw/BODYUUYme9o.jpg)
## Getting start
Upload your image to directory "image"
## Built With
- [CV2](https://opencv.org/) - module for working with images and detecive nti logo 
- [numpy](https://numpy.org/) - for search argmax in scores
## Download packages
```
- pip install opencv-python
- pip install numpy
```
- Install [weights](https://drive.google.com/file/d/1-9ZQNPWj2M77_1EQ3HlFuuczX_8kXj-7/view?usp=sharing) from google drive to main catalog.
## Run script
### Script template
```
python yolo_object_detection.py
path2image
```

### Script sample №1 
![nti](https://github.com/denchicez/test_job_local/blob/main/image/nti.jpg?raw=true)
###### Input
```
python C:/test_job_local/yolo_object_detection.py 
C:/test_job_local/nti.jpg
```
###### Output
```
kruzhok
```

### Script sample №2 

![abrikos](https://foodandmood.com.ua/i/70/83/24/708324/image_main/dbb370837d641548ac7701a36adb5029-quality_75Xresize_crop_1Xallow_enlarge_0Xw_740Xh_493.jpg)
###### Input
```
python C:/test_job_local/yolo_object_detection.py 
C:/test_job_local/abrikos.jpg
```
###### Output
```
 
```

