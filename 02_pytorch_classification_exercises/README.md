# 02 - PyTorch Classification Exercises

Hands-on PyTorch classification exercises covering binary and multiclass classification.

## Topics covered

- Binary classification with `make_moons`
- Non-linear neural networks with `nn.Module`
- `BCEWithLogitsLoss` for binary classification
- Training and testing loops
- Logits, sigmoid probabilities, and predicted labels
- Accuracy measurement
- Decision boundary visualization
- Manual implementation of the `tanh` activation function
- Multiclass classification on a spiral dataset
- `CrossEntropyLoss`, Softmax/Argmax, and Adam optimization
- Device-agnostic PyTorch code

## Verified accuracy report

The finalized notebook was executed end-to-end after the fixes.

| Dataset | Train Accuracy | Test Accuracy | Exercise Target |
|---|---:|---:|---:|
| Make Moons | 97.50% | 98.50% | > 96% |
| Spiral (3 classes) | 99.17% | 100.00% | > 95% |

Both exercise accuracy targets were met in the verified run.

## Key fixes in the final version

- Corrected binary and multiclass loss usage.
- Corrected the spiral model to output 3 classes.
- Added non-linear ReLU layers to the spiral model.
- Used `Softmax/Argmax` logic appropriately for multiclass predictions.
- Implemented the Tanh formula manually in pure PyTorch.
- Corrected device handling and training/testing loops.
- Removed the notebook dependency on TorchMetrics by using a small custom accuracy function.
