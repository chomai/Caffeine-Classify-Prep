import torch
import torch.nn as nn
from torchvision import models

class MobileNetV2Classifier(nn.Module):
    def __init__(self, num_classes=2):
        super(MobileNetV2Classifier, self).__init__()
        # Load the pre-trained MobileNetV2 model
        self.model = models.mobilenet_v2(pretrained=True)

        # Freeze all layers (optional, can be fine-tuned instead)
        for param in self.model.parameters():
            param.requires_grad = False

        # Replace the classifier to suit binary classification (matcha vs coffee)
        in_features = self.model.classifier[1].in_features
        self.model.classifier[1] = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.model(x)
