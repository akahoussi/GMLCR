import algorithms
from algorithms import chess
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"

import GPUtil
GPUs = GPUtil.getGPUs()

print("You are running on device:", GPUs[0].name)
print("Current statistics:")
GPUtil.showUtilization()
print(GPUs[0].temperature, "C")

