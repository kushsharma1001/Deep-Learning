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





