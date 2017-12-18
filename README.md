# Moviefy
A Machine Learning project on recommendation of movies based on the mood of the user
# Libraries required
open cv,
dlib,
windows visual studio 2017,
windows visual studio toolbox(for a 64X naive command prompt),
glob(to acces the file path),
scikit-learn,
numpy.
pandas. 
For installing OpenCV on Ubuntu 16.04, use the link : http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

Download the dlib predictor that has been used in the project from : http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 and move it to the location in the project 'data/DlibPredictor'

The CK+ dataset has been used for training this model, link : http://www.consortium.ri.cmu.edu/ckagree/
# Note:
While installing the dlib on reaching the bootstrap.bat , work these commands on a different command prompt called 64X naive command prompt and after the unpacking the python libraries for the dlib just type pip install < dlib extension >
extension:- dlib-18.17.100-cp27-none-win_amd64.whl(google it and get the file )
# Procedure for this project
First we clean the data  that we have as it is a dirty one.
Reduced the movies from 5000 to 600(based on user ratings ), this was done in R.
Then train the model an nd store the weights.
Organize the images in a seperate folder for training. 
Train them using glob to trace the image paths to be loaded. 
