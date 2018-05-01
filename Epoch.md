# Epochs

We always use a fixed traning dataset (this dataset may contain numerous samples) to train our Neural Network. We use this traning dataset by dividing it into batches as large datasets might not fit into the memory. 

When the neural network has been trained on complete dataset (.i.e. on all the samples), then it is said to complete 1 Epoch. In other words, one forward pass and one backward pass of all the training samples is 1 Epoch.

After 1 Epoch, your Neural Network has been trained on each sample out of your complete training dataset. Training process may consist more than one epochs also if required. That means, we will be iterating through our complete training dataset for more than once.

### Lets quickly take an example:

Suppose, we have 20 samples in our training dataset. Now assume, we divide the dataset into 4 batches of 5 samples each.
Hence, our batch size becomes 5 because in each batch, we would be having 5 samples. The number of batches is 4.

![Epoch](images/Epoch.jpg "Epoch")

Now, Each batch passes through our algorithm and therefore, we will have 4 batches passing through our algorithm. Hence, when all samples have been passed by the algorithm (or we can say when all the 4 batches containing 5 samples each has passed the algorithm), then, it will be 1 Epoch. It will involve 4 iterations to complete 1 Epoch in our case.


##### Generally, the dataset that we use is divided by using 70/30 principle which means 70% of this dataset can be treated as training dataset and 30% can be used for testing purposes.


