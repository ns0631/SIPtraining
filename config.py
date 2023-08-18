import torch
BATCH_SIZE = 4 # Increase / decrease according to GPU memeory.
RESIZE_TO = 640 # Resize the image for training and transforms.
NUM_EPOCHS = 10 # Number of epochs to train for.
NUM_WORKERS = 4 # Number of parallel workers for data loading.
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Training images and XML files directory.
TRAIN_DIR = './fb' #'/home/nikhil/Desktop/SIP-AAI06/Datasets/images/fb_'

# Validation images and XML files directory.
VALID_DIR = './val' #'/home/nikhil/Desktop/SIP-AAI06/Datasets/images/val_'

# Classes: 0 index is reserved for background.
CLASSES = [
    '__background__', 'car'
]
NUM_CLASSES = len(CLASSES)
# Whether to visualize images after crearing the data loaders.
VISUALIZE_TRANSFORMED_IMAGES = False
# Location to save model and plots.
OUT_DIR = 'outputs'