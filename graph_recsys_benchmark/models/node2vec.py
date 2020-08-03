from .base import GraphRecsysModel
import torch
from torch_geometric.nn.inits import glorot


class Node2VecRecsysModel(GraphRecsysModel):
    def __init__(self, **kwargs):
        super(Node2VecRecsysModel, self).__init__(**kwargs)

    def _init(self, **kwargs):
        self.random_walk_model = kwargs['random_walk_model']

        with torch.no_grad():
            self.random_walk_model.eval()
            self.cached_repr = self.random_walk_model()

        self.fc1 = torch.nn.Linear(2 * kwargs['embedding_dim'], kwargs['embedding_dim'])
        self.fc2 = torch.nn.Linear(kwargs['embedding_dim'], 1)

    def eval(self):
        return self.train(False)

    def reset_parameters(self):
        glorot(self.fc1.weight)
        glorot(self.fc2.weight)
