import os
import glob
import random
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch.nn as nn
import torch
import torchvision
import torch.optim as optim
from torchvision import transforms, models
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from tqdm import tqdm
import pickle
def catordog(img:Image):
    test_transform = transforms.Compose([
        transforms.Resize((256, 256)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    with open("c:/git/DS/3.5CD/model.pkl", "rb") as f:
        model = pickle.load(f)
        img = test_transform(img)
        output = model(img.unsqueeze(0).to(device))
        res=torch.argmax(output).item() 
        # print(res)
        if res==1:
            return "dog"
        else:
            return "cat"
