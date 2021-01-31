# Handwritten_hebrew_recognition
## Project history
This repo contains a work in progress I plan to continue on my free time.
This is the Deep Learning project we presented on February 1st, 2021, at the end the Jedha Fullstack Bootcamp in Paris. Our goal was to go as far as we could in the creation of an app capable of transforming photographs of documents written in cursive Hebrew into a .txt file.
I got this idea thinking of the potential applications possible in the historical research fields, in order to archive documents and facilitate research and use of archives. I then got joined by two colleagues of the formation.

## Technical description
In order to create such an app, we defined a working pipeline:
- First, the photographs would pass through an object detection algorithm in order to detect words. For this project, we used YOLO as we only had two weeks and it procures a nicely working, easy to use, application. For further improvement, I would like to explore some Recurrent convolutional neural network too.
- Boxes detected by the first step would then go through somme preprocessing in order to get OpenCV to detect contours of letters. This worked badly as some letters are sometimes written too close from one another, because some letter are written with two parts (i.e. two objects were detected by OpenCv) and because the noise in the picture was also detected as objects... A further exploration would be to train a YOLO type architecture on both words and letter bounding boxes.
- Finally, the "letters boxes" would pass through a classification to recognize the letter and add it to a word that would then be written into a .txt file. We used Resnet to train this algorithm. This worked well on individual letters but performed poorly in documents as every noise was also classified as a letter...

Ground truth in the Pinkas dataset was expressed following the Page structure. In order to train YOLO model, we had to rewrite it into Pascal-VOC structure. 

## Dataset and models
In order to train handwritten letters recognition we used the [HDD dataset [1]](http://tc11.cvc.uab.es/datasets/HHD_v0_1). This dataset is made of 3969 handwritten letters for the train set and 1168 for the test set.

For the word detection, we used the [Pinkas dataset[2]](http://tc11.cvc.uab.es/datasets/Pinkas_1). This dataset is made of pages from a pinkas document, an historical record from the life of Jewish communities at the beginning of the modern era.

We mostly worked in Tensorflow and used the Resnet101 architecture. The YOLO part comes from [the repository of YOLOV5](https://github.com/ultralytics/yolov5).

We got a lot of inspiration [from the work of The AI Guy and his application to detect and extract licence plate numbers](https://github.com/theAIGuysCode/yolov4-custom-functions). You can see some of his functions applied to our issue in our code.

## Obstacles and pists for improvement
As said earlier, our current model is really bad at extracting letters without extracting noise. A solution would be to train an object detection algorithm on a dataset where we would have the ground truth for both words and letters. The Pinkas dataset doesn't provide such level of precision and I would like to constitute such a dataset myself in the future.

As we worked with different codes from different people, we used both Tensorflow and PyTorch. This needs to be simplified.

The loops overs words' and letters' boxes are not necessarily traveling through the document in the right order, which result in a final .txt file with words in an incorrect order with letters in the incorrect order... This needs to be corrected by forcing the loop to work in the right order, using boxes' coordinates.

As of now, this model is only trained on handwritten letter recognition. A good improvement would be to train it also on numbers (thanks to the MNIST dataset) and punctuation.

## Team
G. Dubernet, C. Pinheiro, C. Rodap

## References
[1] Irina Rabaev, The Handwritten Hebrew Dataset (HHD_v0) ,1,ID:HHD_v0_1,URL:http://tc11.cvc.uab.es/datasets/HHD_v0_1
I. Rabaev, B. Kurar Barakat, A. Churkin and J. El-Sana. The HHD Dataset. The 17th International Conference on Frontiers in Handwriting Recognition, pp. 228-233, 2020.

[2] Irina Rabaev, The Pinkas Dataset (Pinkas) ,1,ID:Pinkas_1,URL:http://tc11.cvc.uab.es/datasets/Pinkas_1,
B.Kurar, I. Rabaev, and J. El-Sana The Pinkas Dataset. B.Kurar, I. Rabaev, and J. El-Sana. The Pinkas Dataset. In the 15th International Conference on Document Analysis and Recognition (ICDAR), pp. 732 - 737, 2019.
