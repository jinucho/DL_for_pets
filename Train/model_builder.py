# -*- coding: utf-8 -*-
"""data_loader_module.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Vp4Gzf_nz75b_l0iPhtnZ2Uboys9S1y
"""

# model 파일
import torchvision.models as models
import torch.nn as nn

# AlexNetModel 정의
class AlexNetModel(nn.Module):
    def __init__(self, num_classes):
        super(AlexNetModel, self).__init__()
        self.alexnet = models.alexnet(pretrained=True)
        in_features = self.alexnet.classifier[6].in_features
        self.alexnet.classifier[6] = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.alexnet(x)

# VGG19Model 정의
class VGG19Model(nn.Module):
    def __init__(self, num_classes):
        super(VGG19Model, self).__init__()
        self.vgg19 = models.vgg19(pretrained=True)
        in_features = self.vgg19.classifier[6].in_features
        self.vgg19.classifier[6] = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.vgg19(x)

# Vision Transformer 모델 정의
class ViTModel(nn.Module):
    def __init__(self, num_classes):
        super(ViTModel, self).__init__()
        # 사전 훈련된 ViT 모델 로드
        self.vit = models.vit_b_16(pretrained=True)
        in_features = self.vit.heads[0].in_features
        self.vit.heads[0] = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.vit(x)


class ResNet50Model(nn.Module):
    def __init__(self, num_classes):
        super(ResNet50Model, self).__init__()
        self.resnet50 = models.resnet50(pretrained=True)
        in_features = self.resnet50.fc.in_features
        self.resnet50.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.resnet50(x)

class DenseNet201Model(nn.Module):
    def __init__(self, num_classes):
        super(DenseNet201Model, self).__init__()
        self.densenet201 = models.densenet201(pretrained=True)
        in_features = self.densenet201.classifier.in_features
        self.densenet201.classifier = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.densenet201(x)

class GoogLeNetModel(nn.Module):
    def __init__(self, num_classes):
        super(GoogLeNetModel, self).__init__()
        self.googlenet = models.googlenet(pretrained=True)
        in_features = self.googlenet.fc.in_features
        self.googlenet.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.googlenet(x)