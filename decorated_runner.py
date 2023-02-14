import hydra
from hydra import compose, initialize
from hydra.utils import instantiate
from omegaconf import OmegaConf
from hydra.core.hydra_config import HydraConfig
from datetime import datetime
import os

# https://hydra.cc/docs/tutorials/basic/your_first_app/using_config/
@hydra.main(version_base=None, config_path="conf/", config_name="base")
def runner_1(cfg):
    ''' The hydra-recommended way to run a config job. The decorator takes care of the following steps:
        - Loads (nested) configs
        - Changes working directory to specified output dir (see base config)
        - Copies config to working directory
        - Sets default logger to log to working directory
        - Enables tab completion on command-line overrides
    
    The main downside of this approach is that scheduling with slurm becomes a bit trickier if jobs are queued.
    If you need manual control of config specification to avoid this, then the API in runner_2.py
    could be preferable.
    '''
    model = instantiate(cfg.model) # initializes DemoModel object with parameters specified in cfg
    print(model(cfg.run.n_trials, cfg.run.num_steps))


if __name__ == '__main__':
    runner_1()