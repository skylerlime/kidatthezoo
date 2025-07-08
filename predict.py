import torch
from torchvision import transforms
from PIL import Image
from model import get_model

# === CONFIG ===
MODEL_PATH = "animal_detector.pt"
CLASS_NAMES_FILE = "animal_names.txt"
IMG_SIZE = (224, 224)
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# === Load class names ===
with open(CLASS_NAMES_FILE, "r") as f:
    class_names = [line.strip() for line in f if line.strip()]
num_classes = len(class_names)

# === Load model ===
model = get_model(num_classes)
model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model = model.to(DEVICE)
model.eval()

# === Image transforms ===
transform = transforms.Compose([
    transforms.Resize(IMG_SIZE),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# === Predict function ===
def predict_image(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        output = model(image)
        _, pred = torch.max(output, 1)

    return class_names[pred.item()]