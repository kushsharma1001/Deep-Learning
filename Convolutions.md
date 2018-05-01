# CONVOLUTION NEURAL NETWORKS

#### Convolutional Neural Networks (CNNs or also called convNets) are the deep learning model for computer vision.
#### A CNN is a network of neurons that are used primarily to classify images, cluster them or recognize them. It works just like how our human brain works. Human brain has thousands of internconnected neurons. For specific signals, specific neurons send signals to brain. 

## Lets see how CNN works the same way :

#### 1. A CNN takes an image as an input. Images are represented by an array of shape (height, width, depth/channels), where there are 3 channels (RGB) for colour images, and 1 channel for grayscale images.

#### 2. Now, we apply filter/kernels to the input image. The basic concept behind CNNs is filters/kernels. We can think of them as smaller sized images which are then slided over the input image. By sliding over, we mean that the same filter is slided/convuled over different regions in the image until entire input image has been fully scanned. Filters are just feature detectors as they see only a part of our input image at a time.

#### 3. The output of applying filter on input image is the sum of the elementwise multiplication of the filter elements and the image (can be thought of as dot product). At the same time, the channels get absorbed in this step.

#### 4. Also, we can use any number of filters but they should always be more than number of channels. The output depth dimension will be equal to the number of filters we use. But, For a filter to be able to “convolve” over the image, it should have the same number of channels as the input.

#### Let's look at a example, every image can be considered as a matrix of pixel values. Consider a 5 x 5 image whose pixel values are only 0 and 1 (note that for a grayscale image, pixel values range from 0 to 255. Also, consider another 3 x 3 matrix as a filter/kernel. Suppose, we use 15 such filters. Here, for simplicity, assume number of channels is 1. Hence, Number of channels should be same in our input image and filters.

![Input](images/input.png "Input")

![Filter](images/filter.png "Filter")

# [5X5X1] -----(applying 15 filters of [3X3X1] ) -----> [3X3X15]

#### Hence, we get output as [3X3] matrix and we get 15 such matrices because we used 15 filters and the channel gets absorbed. Actually, We slide the filter matrix over our original input image by 1 pixel (also called ‘stride’) and for every position, we compute element wise multiplication (between the two matrices) and add the multiplication outputs to get the final integer which forms a single element of the output matrix. Note that the 3×3 matrix “sees” only a part of the input image in each stride.

![Output](images/output.jpg "Output")

#### Now, we apply an Activation function such as ReLU on our output matrix of size 3X3 to finally get Feature Map or Activation Map. 

#### An activation function does nothing but removes all negative values (if any) from the matrix and make it 0. Similarly, it removes all positive values from the matrix by making all positives as 1.

# [3X3X15] -----(Activation Function such as ReLU)-----> [3X3X15]

#### Final output matrix after application of Activation Function is called Feature Map or Activation Map.

#### Again, Incase we want to select the number of outputs, then, we can apply a [1X1] matrix and mention the count of outputs that we need. Suppose, we need only 10 outputs from 15 matrices that we have. Then, we perform (number of channels should be same every time we perform convolution, here it is, 15) :

# [3X3X15] ----- 10 [1X1X15] -----> [3X3X10]

#### To obtain a single output, we apply a matrix of same order of that of input and again mention the number of outputs that we need.

#### Hence, here, we now have 10 [3X3] matrices. And we need 6 single outputs. So we apply 6 [3X3] matrices:

# [3X3X10] ----- 6 [3X3X10] -----> [1X1X6]

# We have retrieved 6 [1X1] matrices as desired in the final output now.
