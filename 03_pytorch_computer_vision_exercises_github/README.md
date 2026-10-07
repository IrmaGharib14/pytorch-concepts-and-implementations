# PyTorch Computer Vision Exercises

Hands-on PyTorch computer vision exercises covering MNIST and FashionMNIST classification with convolutional neural networks.

## What this notebook covers

- Computer vision use cases and overfitting
- MNIST dataset loading and visualization
- PyTorch `DataLoader`
- CNN / TinyVGG-style model building with `nn.Conv2d`
- Training and evaluation loops
- Multi-class accuracy and `CrossEntropyLoss`
- Prediction visualization
- Confusion matrix
- `kernel_size` experiments
- FashionMNIST classification and analysis of incorrect predictions

## Files

- `03_pytorch_computer_vision_exercises.ipynb` — completed exercises
- `requirements.txt` — Python dependencies
- `.gitignore` — files that should not be committed

## Setup

```bash
pip install -r requirements.txt
```

Then open the notebook in Jupyter or VS Code and run the cells.

The MNIST and FashionMNIST datasets are downloaded automatically by `torchvision` when the relevant dataset cells are run.
