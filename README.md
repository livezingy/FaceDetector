# FaceDetector

This is a small project about face detection , age and gender estimation using pre-trained models.

- choose the detect source videos/images/camera from the menu
- choose the face detection model haarcascade or a TensorFlow net from the menu.
- choose the age and gender estimation caffemodel net or SSR-Net from the menu.
- The project will show the process time of one frame/image. (Test on Intel Core i7-8550U CPU with 8G RAM, win10 x64)

![image](https://github.com/livezingy/FaceDetector/blob/master/face1.gif)

# Acknowledgements

1. [ diovisgood/agender ](https://github.com/diovisgood/agender) is a Excellent project. The author has studied a lot about existing Open-Source Projects for Gender and Age Estimation.Thanks very much for sharing!
Based on the [ diovisgood/agender ](https://github.com/diovisgood/agender), The FaceDetector change the functions structure of main.py and Add menu to choose the detect source, the  model to detect faces, and the model of age and gender estimation.

2. The test videos and images come from [Giving Harvard Students an iPhone 11 If They Can Answer THIS Question](https://www.youtube.com/watch?v=cSSFRim8OK8). It's a interesting video.Thanks very much for sharing!

3. [Predict Age and Gender using Convolutional Neural Network and openCV](https://towardsdatascience.com/predict-age-and-gender-using-convolutional-neural-network-and-opencv-fd90390e3ce6) 
The face detection is HAAR and the age and gender prediction is Caffenet. The interesting part in this article is the usage of CNN for age and gender predictions on video URLs with pafy and youtube_dl packages. But the youtube_dl often fail to get the video because the youtube measures. This article is very informative and interesting! Thanks very much for sharing!


# Requirements

python

OpenCV-python

keras/tensorflow

Install keras and tensorflow cpu on Windows

# User Manual

## 1. choose detect source: videos/images/camera

videos: put the video(.mp4) to be detected in the folder videos/, Then choose the "videos" as the detect source.

images: put the images to be detected in the folder images/, Then choose the "images" as the detect source.

camera: if the camera is choosed as the detect source, the program will open the camera of the computer and detect what it capture.

## 2. choose the face detection model

HAAR: Haar-cascades loaded by CascadeClassifier in opencv.

Tensornet: CNN model loaded by readNetFromTensorflow in opencv.

## 3. choose the age gender detection model

ssrnet: This model comes from [SSR-Net](https://github.com/shamangary/SSR-Net). It need keras and tensorflow.
It outputs gender(one number in range [0..1], where 0 = Female, 1 = Male.) and age(one number).

Caffenet: This model comes from [AgeGenderDeepLearning](https://github.com/GilLevi/AgeGenderDeepLearning). It is published as caffe models and could be loaded  by readNetFromCaffe in opencv.
It outputs gender(two binary classes: Male and Female, choose maximum.) and age(8 classes: [0..2], [4..6], [8..12], [15..20], [25..32], [38..43], [48..53], [60..100], use softmax, choose maximum.).

A caffe model has 2 associated files,

1 .prototxt — The definition of CNN goes in here. This file defines the layers in the neural network, each layer’s inputs, outputs and functionality.

2 .caffemodel — This contains the information of the trained neural network (trained model).

## 4. RUN
After confirming the inspection source and inspection model, press this option and the program will start processing video or images. During processing, press the ESC key to abort.

If RUN with default, the project will detect with the videos, the Tensornet, the ssrnet. 

# Project Architecture

1. make choices from the menu and RUN from the menu.

2. load the models of face/age/gender detection. Print the load time in the cmd.exe

2. Get a smaller resized frame/image to Find faces. As it is faster to process small images and this merely does not affect quality.

3. Use faces coordinates of a small frame to extract faces patches from original (big) frame/image.

4. Convert and adjust faces patches to a format that model expects. Construct a blob with all faces.

5. Pass a blob of faces through model(s) to get predicted genders and ages for all faces.

6. Draw a rectangle around each face and a label with estimated gender and age. Print the process time in the cmd.exe.

# Develop

If you want to add more face detection models or age gender detection models, you could do as following steps:

1. Prepare the model files and put them into the suitable folder.

2. Add the model name into faceList or ageList in menu.py.

3. Add the load and detect functions of the new model to main.py.

4. Add the models name and the functions name to the load_face_dict/detect_face_dict/load_agender_dict/predictAgeGender_dict in main.py.

   The model name in the dictionary should be consistent with the name in step2.






