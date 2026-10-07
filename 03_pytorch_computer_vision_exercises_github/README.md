# PyTorch Computer Vision Exercises

Hands-on PyTorch computer vision exercises using MNIST and FashionMNIST, covering CNNs, training/evaluation, predictions, confusion matrices, and model error analysis.

## Exercises

## 1. What are 3 areas in industry where computer vision is currently being used?

## 2. Search "what is overfitting in machine learning" and write down a sentence about what you find.

## 3. Search "ways to prevent overfitting in machine learning", write down 3 of the things you find and a sentence about each. 
> **Note:** There are lots of these, so don't worry too much about all of them; just pick 3 and start with those.

## 4. Spend 20 minutes reading and clicking through the [CNN Explainer website](https://poloclub.github.io/cnn-explainer/).

* Upload your own example image using the "upload" button on the website and see what happens in each layer of a CNN as your image passes through it.

## 5. Load the [`torchvision.datasets.MNIST()`](https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html#torchvision.datasets.MNIST) train and test datasets.

## 6. Visualize at least 5 different samples of the MNIST training dataset.

## 7. Turn the MNIST train and test datasets into dataloaders using `torch.utils.data.DataLoader`, set the `batch_size=32`.

## 8. Recreate `model_2` used in notebook 03 (the same model from the [CNN Explainer website](https://poloclub.github.io/cnn-explainer/), also known as TinyVGG) capable of fitting on the MNIST dataset.

## 9. Train the model you built in exercise 8 for 5 epochs on CPU and GPU and see how long it takes on each.

## 10. Make predictions using your trained model and visualize at least 5 of them, comparing the prediction to the target label.

## 11. Plot a confusion matrix comparing your model's predictions to the truth labels.

## 12. Create a random tensor of shape `[1, 3, 64, 64]` and pass it through a `nn.Conv2d()` layer with various hyperparameter settings (these can be any settings you choose), what do you notice if the `kernel_size` parameter goes up and down?

## 13. Use a model similar to the trained `model_2` from notebook 03 to make predictions on the test [`torchvision.datasets.FashionMNIST`](https://pytorch.org/vision/main/generated/torchvision.datasets.FashionMNIST.html) dataset. 
* Then plot some predictions where the model was wrong alongside what the label of the image should've been. 
* After visualizing these predictions, do you think it's more of a modelling error or a data error? 
* As in, could the model do better, or are the labels of the data too close to each other (e.g., a "Shirt" label is too close to "T-shirt/top")?

## Files

- `03_pytorch_computer_vision_exercises.ipynb` — completed exercise notebook
- `requirements.txt` — Python dependencies
- `.gitignore` — files excluded from Git tracking

## Setup

```bash
pip install -r requirements.txt
```

Open the notebook in Jupyter or VS Code and run the cells in order.

MNIST and FashionMNIST are downloaded automatically by `torchvision` when the corresponding dataset cells are run.
