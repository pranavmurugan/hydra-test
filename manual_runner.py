import hydra
from hydra import compose, initialize
from omegaconf import OmegaConf
from datetime import datetime
import os
import subprocess

# https://hydra.cc/docs/advanced/compose_api/
def runner_2():
    ''' The less powerful way of initializing hydra, but more conducive to program-scheduler control.
    Have to manually create and specify output directory. More easy to control slurm submissions;
    I have another config to specify sbatch commands.
    '''
    initialize(version_base=None, config_path="conf")
    experiment_cfg = compose(config_name="base")
    slurm_cfg = compose(config_name="slurm")
    
    output_dir = 'output/Example1/' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    os.mkdir(output_dir)
    
    OmegaConf.save(config = experiment_cfg, f = f'{output_dir}/config.yaml')
    
    with open('run_rxn.sbatch', 'w+') as f:
        f.write('#!/bin/bash \n')
        f.write(f'#SBATCH -n {slurm_cfg.num_cpus} \n')
        f.write(f'#SBATCH -t {slurm_cfg.num_hours}:00:00 \n')
        f.write(f'#SBATCH -p {slurm_cfg.partition} \n')
        if slurm_cfg.num_gpus > 0:
            f.write(f'#SBATCH --gres=gpu:{slurm_cfg.num_gpus} \n')
        f.write('#SBATCH --mem-per-cpu=2000 \n')
        f.write('#SBATCH -o /home/submit/pmurugan/output/output_%j.txt \n')
        f.write('#SBATCH -e /home/submit/pmurugan/error/error_%j.txt \n\n')
        f.write(f'python manual_runner_target.py  {output_dir} \n')
    
    subprocess.run(['sbatch', 'run_rxn.sbatch'])

if __name__ == '__main__':
    runner_2()