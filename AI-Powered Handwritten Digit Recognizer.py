# pip install torch torchvision torchaudio
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms

# Define the model and load pre-trained weights
class ComplexNN(nn.Module):
    def __init__(self):
        super(ComplexNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Create the network and load the weights
net = ComplexNN()

# Ensure 'model.pth' is in the same directory or specify the correct path
try:
    net.load_state_dict(torch.load('model.pth', weights_only=True))
    net.eval()
except FileNotFoundError:
    print("Error: 'model.pth' file not found. Please ensure it is in the correct path.")

# Define the transformations
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),
    transforms.Resize((28, 28)),
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Build the Tkinter application
class AIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Number Recognizer")

        self.label = tk.Label(root, text="Load an image to recognize the number")
        self.label.pack()

        self.button = tk.Button(root, text="Load Image", command=self.load_image)
        self.button.pack()

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            self.show_image(image)
            number = self.predict_number(image)
            self.result_label.config(text=f"Predicted Number: {number}")

    def show_image(self, image):
        image = ImageOps.fit(image, (200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def predict_number(self, image):
        image = transform(image).unsqueeze(0)  # Apply the transformations and add batch dimension
        output = net(image)  # Get the network output
        _, predicted = torch.max(output.data, 1)  # Get the index of the max log-probability
        return predicted.item()

root = tk.Tk()
app = AIApp(root)
root.mainloop()
