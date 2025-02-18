import torch
from torchfold import Fold

class SimpleModel(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super(SimpleModel, self).__init__()
        self.leaf_layer = torch.nn.Linear(input_dim, hidden_dim)
        self.combine_layer = torch.nn.Linear(hidden_dim * 2, hidden_dim)

    def leaf(self, x):
        # 确保输入是二维张量 (batch_size, input_dim)
        return torch.relu(self.leaf_layer(x))

    def combine(self, left, right):
        # 拼接两个隐藏状态
        combined = torch.cat([left, right], dim=-1)
        return torch.relu(self.combine_layer(combined))

# 初始化模型和 Fold 对象
model = SimpleModel(input_dim=10, hidden_dim=20)
fold = Fold()

# 创建输入张量（注意：添加批次维度）
leaf1_input = torch.randn(1, 10)  # 形状为 (batch_size=1, input_dim=10)
leaf2_input = torch.randn(1, 10)

# 在 Fold 中注册节点（使用字符串指定方法名）
leaf1 = fold.add('leaf', leaf1_input)  # 使用字符串 'leaf' 对应 model.leaf 方法
leaf2 = fold.add('leaf', leaf2_input)

# 组合节点
parent = fold.add('combine', leaf1, leaf2)  # 使用字符串 'combine' 对应 model.combine 方法

# 运行计算图
result = fold.apply(model, parent)  # 第二个参数必须是一个列表
print(result)