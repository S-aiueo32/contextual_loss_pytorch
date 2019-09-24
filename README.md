# Contextual Loss w/ PyTorch
PyTorch implementation of Contextual Loss and Context Bilateral (CoBi) Loss.

# Requirements
-  Python3.7+
-  `torch`, `torchvision`

# Installation
```
pip install .
```

# Usage
You can use it in the PyTorch-like style.
```python
import torch

import contextual_loss as cl
import contextual_loss.fuctional as F


# input features
img1 = torch.rand(1, 3, 96, 96)
img2 = torch.rand(1, 3, 96, 96)

# contextual loss
criterion = cl.ContextualLoss()
loss = criterion(img1, img2)

# functional call
loss = F.contextual_loss(img1, img2, band_width=0.1, loss_type='cosine')

# comparing with VGG features
# if `use_vgg` is set, VGG model will be created inside of the criterion
criterion = cl.ContextualLoss(use_vgg=True, vgg_layer='relu5_4')
loss = criterion(img1, img2)

```

# Reference
- https://github.com/roimehrez/contextualLoss
- https://github.com/ceciliavision/zoom-learn-zoom
- https://gist.github.com/yunjey/3105146c736f9c1055463c33b4c989da
