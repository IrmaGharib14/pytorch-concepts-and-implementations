# PyTorch Computer Vision Exercises

Hands-on PyTorch computer vision practice with **MNIST** and **FashionMNIST**, focused on building, training, and evaluating convolutional neural networks.

## Highlights

- Built CNN classifiers with `nn.Conv2d`, `ReLU`, `MaxPool2d`, `Flatten`, and `Linear`
- Used `DataLoader` with mini-batches of 32
- Trained with `CrossEntropyLoss` and SGD
- Evaluated models with accuracy, prediction visualizations, and a confusion matrix
- Explored how different `kernel_size` values change convolution output shapes
- Analyzed misclassified FashionMNIST samples and visually similar classes

## Results

### MNIST CNN
- Final train accuracy: **98.69%**
- Final test accuracy: **98.09%**
- Best test accuracy during training: **98.58%**

### FashionMNIST CNN
- Final train accuracy: **91.10%**
- Final test accuracy: **89.40%**
- Best test accuracy during training: **89.72%**

## Model Notes

- MNIST input shape: `1 × 28 × 28`
- FashionMNIST input shape: `1 × 28 × 28`
- Both tasks contain 10 classes
- FashionMNIST model uses two convolution blocks followed by a linear classifier
- Some FashionMNIST mistakes occur between visually similar classes such as **Shirt** and **T-shirt/top**

## Kernel Size Experiment

For a random input tensor of shape `[1, 3, 64, 64]` with no padding:

- `kernel_size=3` → output spatial size `62 × 62`
- `kernel_size=5` → output spatial size `60 × 60`
- `kernel_size=7` → output spatial size `58 × 58`

Larger kernels cover a wider local region and, without padding, reduce the output height and width more.

## Files

- `03_pytorch_computer_vision_exercises.ipynb` — completed notebook
- `requirements.txt` — dependencies
- `.gitignore` — ignored local files and downloaded datasets

## Setup

```bash
pip install -r requirements.txt
```

Open the notebook in Jupyter or VS Code and run the cells in order.
