import torch.nn as nn 
import torch 

#model = nn.Linear(in_features=1, out_features=1, blass=True)
model = nn.Linear(1,1)

class SingleLayer(nn.Module):
    def __int__(self, inputs):
        super().__init__()
        self.layer =nn.Linear(input,1)
        self.activation =nn.Sigmoid()

    def forward(self,X):
        X =self.layer(x)
        X =self.activation(x)
        return X
    
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=3,out_channels=64)
