# Transposed Convolution
---
It is required when we wish to go opposite to what normal Convolution does. Its also called as Fractionally Strided Convolution or sometimes, Deconvolution as well.

The simplest way to think about a transposed convolution is by computing the output shape of the direct convolution for a given input shape first, and then inverting the input and output shapes for the transposed convolution.

Let’s consider the convolution of a 3 X 3 kernel on a 4 X 4 input with unitary stride and no padding (i.e., i = 4, k = 3, s = 1 and p = 0). As depicted in the convolution below, this produces a 2 X 2 output:

![Convolution](http://deeplearning.net/software/theano/_images/no_padding_no_strides.gif)

The transpose of this convolution will then have an output of shape 4X4 when applied on a 2X2 input.

Another way to obtain the result of a transposed convolution is to apply an equivalent – but much less efficient – direct convolution. The example described so far could be tackled by convolving a 3X3 kernel over a 2X2 input padded with a 2X2 border of zeros using unit strides (i.e., i' = 2, k' = k, s' = 1 and p' = 2), as shown here:

![Deconvolution](http://deeplearning.net/software/theano/_images/no_padding_no_strides_transposed.gif)
