import argparse
from omegaconf import OmegaConf
from hydra.utils import instantiate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate and run reaction simulations.')
    parser.add_argument('run_id', nargs = 1)
    args = parser.parse_args()

    run_id = args.run_id[0]

    config_filepath = f'{run_id}/config.yaml'
    cfg = OmegaConf.load(config_filepath)

    model = instantiate(cfg.model) # initializes DemoModel object with parameters specified in cfg
    print(model(cfg.run.n_trials, cfg.run.num_steps))