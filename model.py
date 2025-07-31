import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import requests

# Load labels from ImageNet
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(LABELS_URL).text.split("\n")

# Load pretrained ResNet18 model
model = models.resnet50(pretrained=True)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],  # ImageNet means
        std=[0.229, 0.224, 0.225]    # ImageNet stds
    ),
])

def predict(image: Image.Image):
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    
    top3_prob, top3_idx = torch.topk(probabilities, 3)

    return [(labels[i.item()], top3_prob[j].item()) for j, i in enumerate(top3_idx)]


