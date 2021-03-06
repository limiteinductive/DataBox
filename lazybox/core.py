# AUTOGENERATED! DO NOT EDIT! File to edit: core.ipynb (unless otherwise specified).

__all__ = ['DataBox', 'create_datablock', 'create_dataloaders', 'set_seed']

# Cell
from operator import add
from functools import reduce

from fastai.vision.all import *

from .utils import *

# Cell
class DataBox:

    def __init__(self, block=(), getter=None, **tfms):

        self.block = tuplify(block)
        self.getter = getter
        self.tfms = tfms

        if not tfms: self.tfms = {}


    def __repr__(self):

        return f"""block: {self.block}, getter: {self.getter}, tfms: {self.tfms}"""


    def __len__(self) -> int:
        return len(tuplify(self.getter))

    def __add__(self, other):
        blocks = self.block + other.block
        getters = listify(self.getter) + listify(other.getter)
        tfms = merge_tfms(self.tfms, other.tfms)

        return DataBox(blocks, getters, **tfms)


# Cell

#export
def create_datablock(input_box, output_box, **kwargs):

    ibox = reduce(add, map(simplify, listify(input_box)), DataBox())
    obox = reduce(add, map(simplify, listify(output_box)), DataBox())

    both_box = ibox + obox

    return DataBlock(
        n_inp=len(ibox),
        blocks=both_box.block,
        get_x=ibox.getter,
        get_y=obox.getter,
        get_items=partial(get_image_files, recurse=False),
        **merge_tfms(both_box.tfms, kwargs)
    )


# Cell
def create_dataloaders(input_box, output_box, path='.', bs=None, **kwargs):

    return DataBlock(input_box, output_box, **kwargs).dataloaders(path, bs)

# Cell
def set_seed(dls, x=0):
    """Set a random seed for all aspects of a Fastai Learner."""
    random.seed(x)
    dls.rng.seed(x)
    np.random.seed(x)
    torch.manual_seed(x)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    if torch.cuda.is_available(): torch.cuda.manual_seed_all(x)