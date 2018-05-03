# Random Number Generation in Python
[Deep-Learning/RandomNumbers.md at master · kushsharma1001/Deep-Learning · GitHub](https://github.com/kushsharma1001/Deep-Learning/blob/master/RandomNumbers.md)
--- 
```
import numpy as np
import random

numberOfInputs = 3
channelsInInputs = 4

inputX1 = [1, 0, 1, 0]
inputX2 = [1, 0 ,1, 1]
inputX3 = [0, 1, 0, 1]

#Weights_4channels = [[0.42, 0.88, 0.55],
#                     [0.10, 0.73, 0.68],
#                     [0.60, 0.18, 0.47],
#                     [0.92, 0.11, 0.52]
#                   ]

Weights_4channels = np.zeros([4,3], dtype=int)

#Random filling of Matrix
for i in range(len(Weights_4channels)):
    print("\n")
    for j in range(len(Weights_4channels[0])):

        Weights_4channels[i][j] = (random.randint(1, 10)*float(10))/100
        print(str(Weights_4channels[i][j]) + ", ", end = " ")

Bias = [0.46, 0.72, 0.08]

Y = [1,1,0]

#Initialize empty 3X3 matrix below:
hidden_layer_input = np.zeros([3,3])

#Random filling of Matrix method-2
hidden_layer_input = np.random.random((3,3))

for i in range(len(hidden_layer_input)):
    print("\n")
    for j in range(len(hidden_layer_input[0])):
        print(str(hidden_layer_input[i][j]) + ", ", end = " ")
```

# Backpropogation
--- 

The Backpropagation table with new random values  is as follows


**Step 0**: Read input and output

![Step0](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step0.png)



**Step 1**: Initialize weights and biases with random values (There are
methods to initialize weights and biases but for now initialize with
random values)

![step1](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step1.png)

**Step 2**: Calculate hidden layer input:

`hidden_layer_input = matrix_dot_product(X,wh) + bh`

![step2](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step2.png)

**Step 3**: Perform non-linear transformation on hidden linear input

`hiddenlayer_activations = sigmoid(hidden_layer_input)`

![step3](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step3.png)

**Step 4**: Perform linear and non-linear transformation of hidden layer
activation at output layer

`output_layer_input = matrix_dot_product (hiddenlayer_activations * wout ) + bout output = sigmoid(output_layer_input)`

![step4](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step4.png)

**Step 5**: Calculate gradient of Error(E) at output layer

`E = y-output`

![step5](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step5.png)



**Step 6**: Compute slope at output and hidden layer

\`Slope\_output\_layer= derivatives\_sigmoid(output)

Slope\_hidden\_layer = derivatives\_sigmoid(hiddenlayer\_activations)\`



**Step 7**: Compute delta at output layer

`d_output = E * slope_output_layer*lr`

![step7](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step7.png)

**Step 8**: Calculate Error at hidden layer

`Error_at_hidden_layer = matrix_dot_product(d_output, wout.Transpose)`

![step8](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step8.png)

**Step 9**: Compute delta at hidden layer

`delta_hiddenlayer = Error_at_hidden_layer * slope_hidden_layer`

![step9](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step8.png)

**Step 10**: Update weight at both output(OL) and hidden layer(HL)

`Updated OL weights
wout = wout + matrix_dot_product (hiddenlayer_activations.Transpose, d_output) * learning_rate`

`Updated HL weights
wh = wh+ matrix_dot_product (X.Transpose,d_hiddenlayer) * learning_rate`

![step10](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step10.png)

**Step 11**: Update biases at both output and hidden layer

`Updated HL Bias
bh = bh + sum(d_hiddenlayer, axis=0) * learning_rate`

`Updated OL Bias
bout = bout + sum(d_output, axis=0)*learning_rate`

![step11](https://raw.githubusercontent.com/meenasambamurthy/mlblr/master/images/step11.png)






