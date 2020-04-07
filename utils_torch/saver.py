import torch
from os.path import join
import os


class Saver():
    def __init__(self, model, module_dict={}, folder=None, save_min=False, save_freq=10,
        start_epoch=0):
        self.model = model
        self.module_dict = module_dict
        self.folder = folder
        self.save_min = save_min
        self.save_freq = save_freq
        self.best_crit = 10000 if save_min else -10000
        self.epoch = start_epoch
        self.file_saved = None

    def save(self, crit_val):
        if (self.save_min and crit_val < self.best_crit) or ((not self.save_min) and crit_val > self.best_crit):
            file_saved = join(
                self.folder, f'best_epoch_{self.epoch}_crit_{crit_val:.3f}.pth')
            torch.save({'model': self.model.state_dict(),
                        'epoch': self.epoch,
                        **{k: mod.state_dict() for k, mod in self.module_dict.items()}
                        }, file_saved)
            if self.file_saved is not None:
                os.remove(self.file_saved)
            self.file_saved = file_saved
            self.best_crit = crit_val
        if ((self.epoch+1) % self.save_freq) == 0:
            torch.save({'model': self.model.state_dict(),
                        'epoch': self.epoch,
                        **{k: mod.state_dict() for k, mod in self.module_dict.items()}
                        }, join(self.folder, f'epoch_{self.epoch}_crit_{crit_val:.3f}.pth'))
        self.epoch += 1
