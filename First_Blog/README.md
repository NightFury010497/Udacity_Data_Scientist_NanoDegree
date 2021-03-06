># Project Face Recognition!
![3](https://user-images.githubusercontent.com/56355704/84321970-d4fa4300-ab91-11ea-8fc5-b0417c18e7c7.gif)  
# [BLOG](https://medium.com/@nightfury010497/nano-degree-735ef9c6563b?source=friends_link&sk=d96dfc21b36360058d87061ac8dfc98c)  
# [REPOSITORY](https://github.com/NightFury010497/Udacity_Data_Scientist_NanoDegree/tree/master/First_Blog)  
>## Libraries 
pip install -r requirements.txt  
### Project motivation  
[Delhi,India : Facial recognition system helps trace 3,000 missing children in just 4 days!](https://timesofindia.indiatimes.com/city/delhi/delhi-facial-recognition-system-helps-trace-3000-missing-children-in-4-days/articleshow/63870129.cms)  
>### Files in the repository
 - dataa.zip - contains sample images  to wrangle  
 - model_paths.zip - contains the paths to model  
 - requirements.txt - to take care about the requirements of your environment
 - face_recog_EDA.ipynb - code  
>### Summary of the results
 - Can help in catching  felony in a bank.
 -  Help in finding lost children **(What's the use of technology if we can't bring our loved one's back?!**
>### Acknowledgements 
 - Udacity
 - Medium
 - Google Colab  
>###  Bussiness Understanding
 - How can we better retain information?
   - We can detect faces and send it to the National Crime Branch to help them find the felonies, those who have been hidding since years.
 - How can we improve bank payments security?
   - We can use face recognition to grant access for the payments to make it more secure.
>###  Data Understanding
 - In this we can push images of any size and shape, as I have coded in such a manner that it will resize itself to 300*300 for model processing.
 - Sources of data for better understanding [DATASET-ZOO](https://github.com/deepinsight/insightface/wiki/Dataset-Zoo)
>### Data Preparation
 - In this we will resize all the images we will receive to 300*300 so as to maintain standards for our model.
>###  Data Modeling
 - Your Image [Size- (194,243,3)] ---> Resized to (300*300) ---> Generate Embeddings [512-D Vector](https://thedatamage.com/face-recognition-tensorflow-tutorial/) ---> Reduce Dimensionality   by T-SNE --> Plot it in 2-D using matplotlib.
 - Once the Embeddings are generated along with that we have target variable or classes as the person as a class.
 - KNN or SVC is Fitted and prediction is tested on Y_test to find the results.
 - Later we find out the accuracies so as to evaluate our model.
>### Evaluate the Results
 - For Evaluation we have generated a probability of a face matching itself and kept a threshold for better verification of faces.

### LINK TO REFER:   
https://medium.com/@nightfury010497/nano-degree-735ef9c6563b?source=friends_link&sk=d96dfc21b36360058d87061ac8dfc98c  
