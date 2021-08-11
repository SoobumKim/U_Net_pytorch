# UNet_pytorch

# Data

The original dataset is from isbi challenge. You can use it in folder 'data'. The shape of image is 512x512.
 
# Augmentation

We sequentially augment the original dataset using RandomHorizontalFlip, RandomVerticalFlip, Resize(1000, 1000), RandomResizedCrop(512, 512) in 'torchvision.transforms'. The 'dataaug.py' is aug dataset generation script. The images and masks are respectively annotated to '_img' and '_mask'. Finally we increase data 30 to 3000.

<p align="center"><img src=https://user-images.githubusercontent.com/19663575/128594105-e7a00baf-e599-4d8d-8a5e-c175a0062a4f.JPG width="500" height="400"></>
  
# Hyperparameters
Batch size : 2
  
Learning rate : 1e-4
 
Learning rate decay : 0.95
  
Epoch : 10
 
# Training
Loss function : Binary cross entropy function
 
Optimizer : Adam
 
Last activation function : Sigmoid
 
Learning rate decay scheduler : ExponentialLR
 
<img src=https://user-images.githubusercontent.com/19663575/128675888-e2ef99c9-c19e-4c9e-a82b-81a4ca239c46.png width="300" height="200">
 
# Test
 Notice! Please delete '_pred' files in test dataset folder before prediction.
 
 Left one is test image and right one is prediction image.
 
<p align="center"><img src=https://user-images.githubusercontent.com/19663575/128675593-b01ff443-3169-47be-8ced-e92c9b0462bc.png width="500" height="500"></>
