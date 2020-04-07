import os
from os.path import join
import torch
from glob import glob


def load_model(model, load_from, load_dict={}):
    if os.path.isfile(load_from):
        ckpt_file=load_from
    else:
        ckpt_file=glob(load_from+"*/best*.pth")[-1]
        
    ckpt = torch.load(ckpt_file,map_location = torch.device('cpu'))
    print(f"loading model: {ckpt_file}")
    print(model.load_state_dict(ckpt['model']))

    for k, module in load_dict.items():
        module.load_state_dict(ckpt[k])

    return ckpt['epoch']
