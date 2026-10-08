# PyTorch Custom Datasets Exercises

Hands-on PyTorch computer vision exercises focused on loading custom image datasets,
building `Dataset`/`DataLoader` pipelines, training a TinyVGG-style CNN, diagnosing
underfitting/overfitting, scaling the amount of data, and making predictions on a
custom image.

## Project contents

- `04_pytorch_custom_datasets_exercises.ipynb` — completed exercise notebook
- `download_data.py` — downloads and extracts the 10% and 20% Pizza/Steak/Sushi datasets
- `requirements.txt` — Python dependencies
- `.gitignore` — excludes local datasets, environments, caches, and editor files

## Exercises covered

1. Ways to reduce underfitting
2. Custom image loading pipeline
3. TinyVGG recreation
4. Training and testing functions
5. Training for different numbers of epochs
6. Increasing model capacity
7. Doubling the dataset and training for 20 epochs
8. Predicting a custom Pizza/Steak/Sushi image

## Data pipeline

```text
Images on disk
    ↓
train / test folders
    ↓
torchvision.transforms
    ↓
ImageFolder
    ↓
DataLoader
    ↓
TinyVGG
```

Images are resized to `64 × 64` and converted to tensors before entering the model.

## Model

The notebook uses a TinyVGG-style CNN with two convolution blocks followed by a
flattening/classification layer. The input is RGB:

```text
[B, 3, 64, 64]
```

The experiments also compare different model capacities and training durations.

## Notable result

For the exercise using the larger 20% dataset and `hidden_units=20`, the recorded
20-epoch run finished at approximately:

- Train accuracy: **83.75%**
- Test accuracy: **60.97%**
- Best recorded test accuracy: **64.77%** (epoch 11)

Later epochs show a widening train/test gap, which is consistent with overfitting.

## Setup

Create and activate a virtual environment, then install the requirements:

```bash
pip install -r requirements.txt
```

Download the datasets:

```bash
python download_data.py
```

Then launch Jupyter:

```bash
jupyter notebook
```

Open:

```text
04_pytorch_custom_datasets_exercises.ipynb
```

## Custom image prediction

Exercise 8 expects a custom image path. You can place an image at:

```text
data/my_pizza.jpeg
```

or change `custom_image_path` in the notebook to your own Pizza, Steak, or Sushi image.

## Dataset source

The Pizza/Steak/Sushi subsets are from the data used in Daniel Bourke's
*Learn PyTorch for Deep Learning* course. Dataset files are intentionally not committed
to this repository; use `download_data.py` to retrieve them.

## Notes

- The notebook uses device-agnostic PyTorch code and can run on CPU or CUDA.
- Exact metrics can vary slightly between environments.
- The `data/` directory is ignored by Git to keep the repository lightweight.
