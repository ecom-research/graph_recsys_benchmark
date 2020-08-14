import torch


class GraphRecsysModel(torch.nn.Module):
    def __init__(self, **kwargs):
        super(GraphRecsysModel, self).__init__()
        self._init(**kwargs)

        self.reset_parameters()

    def _init(self, **kwargs):
        raise NotImplementedError

    def reset_parameters(self):
        raise NotImplementedError

    def loss(self, pos_neg_pair_t):
        raise NotImplementedError

    def update_graph_input(self, dataset):
        raise NotImplementedError

    def predict(self, unids, inids):
        raise NotImplementedError

    def eval(self):
        super(GraphRecsysModel, self).eval()
        with torch.no_grad():
            self.cached_repr = self.forward()


class MFRecsysModel(torch.nn.Module):
    def __init__(self, **kwargs):
        super(MFRecsysModel, self).__init__()
        self._init(**kwargs)

        self.reset_parameters()

    def _init(self, **kwargs):
        raise NotImplementedError

    def reset_parameters(self):
        raise NotImplementedError

    def loss(self, pos_neg_pair_t):
        raise NotImplementedError

    def predict(self, unids, inids):
        return self.forward(unids, inids)