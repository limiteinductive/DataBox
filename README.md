# LazyBox
> A user friendly API to jump-start your Deep Learning project based on Fastai. 


The library is still in early development, but a lot of new features will be added in future

    [ ] Support for non-image Datasets
    [ ] Import NN architecture from the timm library
    [ ] Make it better

## Install

`pip install lazybox`

## How to use

Let's go through a typical workflow for a DeepLearning task. Let's take a Dataset on Kaggle: https://www.kaggle.com/tongpython/cat-and-dog which are images of cat and dogs so we can train a classifier to predict the species

```
# we lazy folks only use wild imports
from lazybox.all import *


dls = create_dataloaders(
    input_box=image_box,
    output_box=bbox_box,
    path='cat_dataset'
)

```
