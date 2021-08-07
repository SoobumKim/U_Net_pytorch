#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from torch.utils.data import Dataset
from PIL import Image
import os
from glob import glob
import numpy as np
import random
import natsort
    
class TestDataset(Dataset):
    def __init__(self,path_test='./data/test',transform=None):
        self.path_test = path_test
        self.test_filenames = os.listdir(path_test) 
        self.transform = transform
        
    def __len__(self):
        return len(self.test_filenames)
    def __getitem__(self,idx):
        test_data_paths = []
        sorted_test_filenames = natsort.natsorted(self.test_filenames)    
        
        for test_filename in sorted_test_filenames:                                 
            test_data_paths.append(os.path.join(self.path_test,test_filename))
        
        test_data_path = test_data_paths[idx]
        test_data = Image.open(test_data_path)
        
        test_data = self.transform(test_data)

        return test_data

