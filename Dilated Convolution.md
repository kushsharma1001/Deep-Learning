# Dilated Convolution
--- 
It's a type of convolution in which we have the capability to decide the gaps in filter. The main idea behind introducing gaps in the filter is to dilate the filter (so as to get an increase in its receptive field) retaining same size of feature map in output. Introducing gaps here means skipping pixels.

### D-dilated KxK convolution
In normal convolution, we have no gaps. So, a normal convolution is 1 - Dilated Convolution. 


In 2 - Dilated Convolution, a filter will have specific size and on dilation (adding gaps), it will have increased receptive field but at the same time, the feature map will be of same size.

![Dilation in Convolution](https://qph.ec.quoracdn.net/main-qimg-d9025e88d7d792e26f4040b767b25819.webp)

Here, In fig 1 we can see 1- Dilated Convolution, Filter is of size (3X3) and receptive field is also of (3X3)
In fig 2 we can see 2- Dilated Convolution, Filter is of size (3X3) and receptive field is also of (7X7)
In fig 3 we can see 3- Dilated Convolution, Filter is of size (3X3) and receptive field is also of (11X11)

![Dilated](http://deeplearning.net/software/theano/_images/dilation.gif)
