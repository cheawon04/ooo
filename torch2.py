import torch
from torch import Torch 

class PyTorch(Torch):
    def __init__(self,name):
        super().__init__(name)
        self.pyname = "py최수길"

    def sub_print(self):
        print(self.pyname)


def main():
    t1 = torch()
    t1.print()