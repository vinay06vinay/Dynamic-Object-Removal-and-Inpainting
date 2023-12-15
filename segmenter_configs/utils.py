import torch
import torchvision.transforms.functional as F
import numpy as np
import yaml
from pathlib import Path

IGNORE_LABEL = 255
STATS = {
    "vit": {"mean": (0.5, 0.5, 0.5), "std": (0.5, 0.5, 0.5)},
    "deit": {"mean": (0.485, 0.456, 0.406), "std": (0.229, 0.224, 0.225)},
}


def seg_to_rgb(seg, colors):
    im = torch.zeros((seg.shape[0], seg.shape[1], seg.shape[2], 3)).float()
    color = torch.tensor([1.0, 1.0, 1.0])
    cls = torch.unique(seg)
    # dynamic_classes = ["person", "individual", "someone", "somebody", "mortal", "soul", "armchair", "desk", "rock", "stone", "pillow", "coffee table", "cocktail table", "pot", "stool", "book", "bench", "countertop", "stove", "kitchen stove", "kitchen range", "cooking stove", "palm", "palm tree", "kitchen island", "swivel chair", "boat", "bar", "bus", "autobus", "coach", "charabanc", "double-checker", "jitney", "motorbus", "motorcoach", "omnibus", "passenger vehicle", "towel", "truck", "motor truck", "apparel", "wearing apparel", "dress", "clothes", "pole", "moving staircase", "moving stairway", "van", "ship", "fountain", "conveyor belt", "transporter", "plaything", "toy", "stool", "barrel", "cask", "basket", "waterfall", "falls", "bag", "minibike", "motorbike", "animal", "animate being", "beast", "brute", "creature", "fauna", "bicycle", "bike", "wheel", "cycle","blanket", "cover", "tray","ashcan", "trash can", "garbage can", "wastebin", "ash bin", "ash-bin", "ashbin", "dustbin","trash barrel", "trash bin", "plate", "shower", "glass", "drinking glass", "flag"]
    dynamic_classes = [12, 3, 5, 15, 19, 20, 30, 31, 51, 75, 76, 80, 81, 83, 90, 96, 98, 102, 104, 105, 108, 110, 115, 116, 117, 119, 120, 126, 127, 137, 138, 142, 145, 147, 149, 12]
    for cl in cls:
      # print(type(cl),cl)
      if int(cl) in dynamic_classes :
        #  color = colors[int(cl)]
        #  if len(color.shape) > 1:
        #    color = color[0]
        #  print(type(color), color)
         im[seg == cl] = color
    return im


def dataset_cat_description(path, cmap=None):
    desc = yaml.load(open(path, "r"), Loader=yaml.FullLoader)
    colors = {}
    names = []
    for i, cat in enumerate(desc):
        names.append(cat["name"])
        if "color" in cat:
            colors[cat["id"]] = torch.tensor(cat["color"]).float() / 255
        else:
            colors[cat["id"]] = torch.tensor(cmap[cat["id"]]).float()
    colors[IGNORE_LABEL] = torch.tensor([0.0, 0.0, 0.0]).float()
    return names, colors


def rgb_normalize(x, stats):
    """
    x : C x *
    x \in [0, 1]
    """
    return F.normalize(x, stats["mean"], stats["std"])


def rgb_denormalize(x, stats):
    """
    x : N x C x *
    x \in [-1, 1]
    """
    mean = torch.tensor(stats["mean"])
    std = torch.tensor(stats["std"])
    for i in range(3):
        x[:, i, :, :] = x[:, i, :, :] * std[i] + mean[i]
    return x
