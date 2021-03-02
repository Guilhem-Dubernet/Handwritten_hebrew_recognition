# Handwritten_hebrew_recognition
## Project history
This repo contains a work in progress I plan to continue on my free time.
This is the Deep Learning project we presented on February 1st, 2021, at the end the Jedha Fullstack Bootcamp in Paris. Our goal was to go as far as we could in the creation of an app capable of transforming photographs of documents written in cursive Hebrew into a .txt file.

I am passionate about languages and everything about Judaism, so this project was an opportunity to mix passions! I got this idea thinking of the potential applications possible in the historical research fields, in order to archive documents and facilitate research and use of archives. For example, the Yad Vashem memorial, in Israel, has a great numbers of photographs of testimonies and documents from pre-WWII eastern Europe Jewish communities. Such an algorithm would allow to archive texts as long as they are written in hebraic characters and would work for both Yiddish and Hebrew. Of course, such an app would need to be really precise in its detection and recognition before being put into deployment, which is not the case yet, but please remember that this repo is a work in progress.

## Dataset and models
In order to train handwritten letters recognition we used the [HDD dataset [1]](http://tc11.cvc.uab.es/datasets/HHD_v0_1). This dataset is made of 3969 handwritten letters for the train set and 1168 for the test set.

For the word detection, we used the [Pinkas dataset[2]](http://tc11.cvc.uab.es/datasets/Pinkas_1). This dataset is made of pages from a pinkas document, an historical record from the life of Jewish communities at the beginning of the modern era.

We mostly worked in Tensorflow and used the Resnet101 architecture. The YOLO part comes from [the repository of YOLOV5](https://github.com/ultralytics/yolov5).

We got a lot of inspiration [from the work of The AI Guy and his application to detect and extract licence plate numbers](https://github.com/theAIGuysCode/yolov4-custom-functions). You can see some of his functions applied to our issue in our code.

## Technical description
With my two colleagues, we defined a working pipeline for the algorithm: first, a word detection within a picture of a page, then, a letter detection within each word and, finally, a letter recognition and transcription into a text file.

### Word detection using YOLO
First, the photographs would pass through an object detection algorithm in order to detect words. For this project, we used YoloV5 and the website Roboflow as we only had two weeks and it procures a nicely working, easy to use, application. We know that YoloV5 isn't a "canonic" version of Yolo and there is some debate about its legitimacy and performance. But it offered an easy introduction for our use and worked pretty well in our application.

In order to make the ground truth understandable by Roboflow, we had to transpose the xml files from a Page structure into a Pascal-VOC structure and developed a "Page to VOC writer" in order to do so.

After training YoloV5 on the PInkas Dataset, we obtained a pretty good detection of our only class "word" as we can see below: the picture above is the ground truth from the Pinaks dataset and the picture below shows our detection. We have around 60% of the word detected with above a certainty of 0.8 and above (the detection was calibrated to only keep classes detected with a certainty higher than 0.5).
<p align="center"><img src="data/word_detection.jpg"\></p>

This result isn't perfect, of course, but it allowed us to go further in our development. For further improvement, I would like to explore some Recurrent convolutional neural network too.

### Letter detection using OpenCV
Boxes of words detected by the first step are then going through somme preprocessing in order to get OpenCV to detect contours of letters. This worked badly as some letters are sometimes written too close from one another (i.e. one object was detected instead of two), because some letter are written with two parts (i.e. two objects were detected by OpenCv) and because the noise in the picture was also detected as objects... We can see the preprocessing in the image below with the poor detection of letters at the end.
<p align="center"><img src="data/letter_detection.jpg"\></p>

We developed this part knowing from the start that OpenCV could be limited for our use, but it allowed us to explore solutions and to go further without having to train yet another model. A further exploration would be to train a YOLO type architecture on both words and letter bounding boxes, but the Pinkas dataset doesn't offer such a level of precision.

### Letter recognition using Resnet

Finally, the "letters boxes" detected by OpenCV are passed through a classification to recognize the letter and add it to a word that would then be written into a .txt file. We used Resnet to train this algorithm. This worked well on individual letters: we obtained an accuracy of O.99 on the train and 0.80 on the validation set. There is a slight overfitting that needs to be addressed, but, as before, this result allowed us to go further.
Unfortunately, the letter recognition performed poorly in documents as every noise was also classified as a letter...

## Obstacles and pists for improvement
As said earlier, our current model is really bad at extracting letters without extracting noise. A solution would be to train an object detection algorithm on a dataset where we would have the ground truth for both words and letters. The Pinkas dataset doesn't provide such level of precision and I would like to constitute such a dataset myself in the future.

As we worked with different codes from different people, we used both Tensorflow and PyTorch. This needs to be simplified.

The loops overs words' and letters' boxes are not necessarily traveling through the document in the right order (i.e. from the top right corner to the bottom left corner, Hebrew being read from right to left), which result in a final .txt file with words in an incorrect order with letters in the incorrect order... This needs to be corrected by forcing the loop to work in the right order, using boxes' coordinates.

As of now, this model is only trained on handwritten letter recognition. A good improvement would be to train it also on numbers (thanks to the MNIST dataset) and punctuation.

## Team
G. Dubernet, C. Pinheiro, C. Rodap

## References
[1] Irina Rabaev, The Handwritten Hebrew Dataset (HHD_v0) ,1,ID:HHD_v0_1,URL:http://tc11.cvc.uab.es/datasets/HHD_v0_1
I. Rabaev, B. Kurar Barakat, A. Churkin and J. El-Sana. The HHD Dataset. The 17th International Conference on Frontiers in Handwriting Recognition, pp. 228-233, 2020.

[2] Irina Rabaev, The Pinkas Dataset (Pinkas) ,1,ID:Pinkas_1,URL:http://tc11.cvc.uab.es/datasets/Pinkas_1,
B.Kurar, I. Rabaev, and J. El-Sana The Pinkas Dataset. B.Kurar, I. Rabaev, and J. El-Sana. The Pinkas Dataset. In the 15th International Conference on Document Analysis and Recognition (ICDAR), pp. 732 - 737, 2019.
