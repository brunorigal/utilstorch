from torch.utils.tensorboard import SummaryWriter
from os.path import join
from pprint import pprint


class Monitor():
    def __init__(self, folder=None):
        self.folder = folder
        self.writer = SummaryWriter(self.folder)
        self.global_step = 0

    def step_train(self, train_dict):
        for k, v in train_dict.items():
            self.writer.add_scalar(
                k+'/train', v, global_step=self.global_step)
        self.global_step += 1

    def step_val(self, val_dict):
        print('\n #### Validation')
        pprint(val_dict)
        for k, v in val_dict.items():
            self.writer.add_scalar(
                k+'/val', v, global_step=self.global_step)
