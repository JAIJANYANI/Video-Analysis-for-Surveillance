# Video-Analysis-for-Surveillance
Analyzing CCTV videos to find timestamps of interesting events using deep learning

## Description
Performed this analysis using image/video processing and deep learning algorithms.


The Project consist of three steps : 

1.) Extracting frames from a video at regular intervals<br />
2.) Detecting change in every two consecutive frames in a sequence<br />
3.) Reporting timestamp for every change<br />


## Prerequisites

# Software
* Python-opencv
* Tensorflow v 1.0 or later
* Python 3.6.0 |Anaconda 4.3.0 (64-bit)|<br />

Tested on Ubuntu 16.04 LTS amd64 xenial image built on 2017-09-19 8-core CPU


## Installation

* Simply clone the repository
* Paste your video/videos in "videos" folder
* Done


## Running

* Simply run this command from root directory.

```
python extract.py ./videos -o ./images --skip 75

```
* NOTE : Video should be present in "videos" folder<br />
       : Frames will be extracted in "images" folder<br />
       : --skip = 3*FPS<br />
       : The provided video "05_05.mp4" has 25FPS , so skip = 75<br />
       

## Screenshots

![untitled](https://user-images.githubusercontent.com/15799933/30987030-31fd434c-a4b3-11e7-80d9-29eba48668d8.png)



![untitled2](https://user-images.githubusercontent.com/15799933/30987032-32275fd8-a4b3-11e7-88ea-8f4f8e638c0e.png)



![untitled3](https://user-images.githubusercontent.com/15799933/30987031-321dc90a-a4b3-11e7-84e4-3b0c6e1607eb.png)




## Output
```
start time : 0:01:39
end time : 0:02:09


start time : 0:03:45
end time : 0:03:48


start time : 0:04:27
end time : 0:04:33


start time : 0:06:57
end time : 0:07:06


start time : 0:07:39
end time : 0:08:15


start time : 0:08:18
end time : 0:08:18


start time : 0:10:45
end time : 0:10:48


start time : 0:11:36
end time : 0:11:39

```


       
## Author

# Jai Janyani

## Licence

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for detail


