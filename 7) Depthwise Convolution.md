# Depthwise Convolution
---
In this, Convolution is performed over each channel of input layer and 
![Depthwise](https://eli.thegreenplace.net/images/2018/conv2d-depthwise.svg)

There are three conceptual stages here:

Split the input into channels, and split the filter into channels (the number of channels between input and filter must match).
For each of the channels, convolve the input with the corresponding filter, producing an output tensor (2D).
Stack the output tensors back together.

In Depthwise Seperable Convolution, After completing the depthwise convolution, an additional step is performed: a 1x1 convolution across channels using a 1x1 spatial filter.

The output channels all take the output of the depthwise step and mix it up with different 1x1 convolutions.

![Seperable](https://eli.thegreenplace.net/images/2018/conv2d-depthwise-separable.svg)
