import algorithms
import chess
import torch, torchaudio, torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from torch import nn

device = "cuda" if torch.cuda.is_available() else "cpu"

