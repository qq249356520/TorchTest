import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input channels  6 output channels 5 * 5 square convolution
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)

        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        #MaxPooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        #If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  #except the batch dimension
        num_feature = 1
        for s in size:
            num_feature *= s
        return num_feature

# net = Net()
# print(net)
#
#
# params = list(net.parameters())  #一个网络中可以学习的参数都存在net.parametets中
# print(len(params))
# print(params[0].size())
#
#
# input = Variable(torch.randn(1, 1, 32, 32))
# out = net(input)
# print(out)
#
# net.zero_grad()
# out.backward(torch.randn(1, 10))
#
# output = net(input)
# target = Variable(torch.arange(1, 11))
# criterion = nn.MSELoss()
#
# loss = criterion(output, target)
# print(loss)




