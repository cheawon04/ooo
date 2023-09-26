# 1
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)

# 2
df = pd.read_csv("data/diabetes.csv")
print(df.head())
X = df[df.columns[:-1]]
y = df[df.columns[-1]]
X = X.values
y = torch.tensor(y.values)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


# 3
ms = MinMaxScaler()
ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)
y_train = ms.fit_transform(y_train.reshape(-1, 1))
y_test = ms.fit_transform(y_test.reshape(-1, 1))


# 4
class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.len = len(self.X)

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return self.len


# 5
train_data = CustomDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train))
test_data = CustomDataset(torch.FloatTensor(X_test), torch.FloatTensor(y_test))

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False)


# 6
class BinaryClassification(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(8, 64, bias=True)
        self.layer_2 = nn.Linear(64, 64, bias=True)
        self.out_layer = nn.Linear(64, 1, bias=True)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(p=0.1)
        self.batchnorm1 = nn.BatchNorm1d(64)
        self.batchnorm2 = nn.BatchNorm1d(64)

    def forward(self, input):
        x = self.relu(self.layer_1(input))
        x = self.batchnorm1(x)
        x = self.relu(self.layer_2(x))
        x = self.batchnorm2(x)
        x = self.dropout(x)
        x = self.out_layer(x)
        return x


# 7 loss, optimizer
epoch_num = 100
print_epoch = 10
lr = 0.01  # 1e-2

model = BinaryClassification().to(device)
print(model)
BCE = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=lr)


# 8 model correct measure
def accuracy(y_pred, y_test):
    y_pred = torch.round(torch.sigmoid(y_pred))
    correct_results_sum = (y_pred == y_test).sum().float()
    acc = correct_results_sum / y_test.shape[0]
    acc = torch.round(acc * 100)
    return acc


# 9 model training
for epoch in range(epoch_num):
    iteration_loss = 0
    iteration_acc = 0

    model.train()
    for i, data in enumerate(train_loader):
        X, y = data
        X, y = X.to(device), y.to(device)

        y_pred = model(X.float())
        loss = BCE(y_pred, y.reshape(-1, 1).float())

        iteration_loss += loss
        iteration_acc += accuracy(y_pred, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    if epoch % print_epoch == 0:
        print(f"Train: epoch: {epoch}", end="")
        print(
            f"  - loss: {iteration_loss / (i+1):.5f} - acc: {iteration_acc / (i+1):.3f}"
        )

    iteration_loss = 0
    iteration_acc = 0

    model.eval()
    for i, data in enumerate(test_loader):
        X, y = data
        X, y = X.to(device), y.to(device)

        y_pred = model(X.float())
        loss = BCE(y_pred, y.reshape(-1, 1).float())

        iteration_loss += loss
        iteration_acc += accuracy(y_pred, y)
    if epoch % print_epoch == 0:
        print(f"Test: epoch: {epoch}", end="")
        print(
            f"  - loss: {iteration_loss / (i+1):.5f} - acc: {iteration_acc / (i+1):.3f}"
        )