# Moviefy

Moviefy is an end to end machine learning project where movies are recommended to a user based on their expression of happy, sad or angry. This project has been deployed using Flask framework on Heroku cloud platform. There are two different version of this web-app; one which runs locally with and interactive dynamic interface of detecting emotions and recommending movies anf the other web app is hosted on heroku where you would have to select an image of a facial expression and the movie recommendations will be generated. 

The python production files ending with  ```_1``` are the files that are being used int the Heroku production environment. 
  
The locally deployed version is present in a folder named **local_web_app**. 

# Prereqisites

This project has been implimented in python (version3.7.6) which uses the deep-learning libraries like Keras and tensorfflow (2.0.0) and tested on ubuntu and Windows OS. 

# Run Demo

1) You could visit https://em-exp-recommender.herokuapp.com/ (it might take some time to load up the application).
2) Download the **local_web_app**folder. If you are using an anaconda environment launch the anaconda cmd prompt and go to this specific folder and run ```python app.py```.
 
  
# Overview

#### Emotion model 
The emotion detection was done using a transer learning technique where a pretrained Convolution Neural Network model VGG16 was utilised to extract features from images. 

The top layers required for predictions were hand modeled (fine tuning) an the input to this model was a flattened numpy arrays of the extracted features from the images. 

![Fine-tuning](https://www.researchgate.net/profile/Kitsuchart_Pasupa/publication/328775300/figure/fig3/AS:735835158757377@1552448181099/Modified-VGG-16-architecture-which-provides-a-fine-tuned-VGG-face-CNN-descriptor-on-face.ppm)

The data on which the model was trained is the FER2013 emotions dataset. This dataset can be downloaded using the kaggle api.

#### Movies Classifier model
Imdb movies dataset was utilised in order to train the classifier model. Movie genre were the attributes that were used to train the classifier model to tell if the movie is happy sad or angry(hand-labeled). 

These movies were then encapsulated within a ```.csv``` file, which was utilised during the generation of the recommendations.

**The model training notebooks are present in the model_train_notebooks folder** 
  
## Model Deployment Note 
While deploying the project in the Heroku cloud environment you would need to take care of using buildpacks as you will encounder the follwing error :
```
ImportError: libGL.so.1: cannot open shared object file: No such file or directory heroku
```
*NOTE : Do this steps only after the build succeed the first time. Do not add the build pack beforehand*

For this you would need to write ```libgl1``` into a Aptfile and place it into your root github directory. After this you will have to add a buildpack that will be used to install the specific library. 

```heroku buildpacks:add --index 1 https://github.com/heroku/heroku-buildpack-apt``` use as is in the console.

Once this is added deploy it once again.

Do not use git LFS to load your model weights into your github repo, it is not recognised bu Heroku. 

Use the standered ``` git add .``` and ``` git commit ``` to successfully upload the model weights file. 

# References

**Deployment** : https://youtu.be/mrExsjcvF4o
  
**Heroki Ligbl error** : https://stackoverflow.com/questions/63845382/importerror-libgl-so-1-error-when-accessing-heroku-app
  
**Buildpack work-around** : https://youtu.be/Kl7mqpAK-bk

