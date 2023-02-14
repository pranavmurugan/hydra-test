# Hydra Demo
Minimum working example highlighting some of the uses of Hydra as a config management tool for scientific simulation.

## Structure
Config files are in `conf/`, model and associated files are in `core/` (and e.g. `utils/` etc.) and run outputs are sent to `outputs/`. I have more detailed comments and links to hydra references in the associated config and python files -- check them out!

### Two ways of running the model:

`decorated_runner.py` is more complete and convenient but may run into scheduler issues. This file could be submitted directly in a batch script via slurm, or run via command line.

`manual_runner.py` only calls the bare minimum hydra APIs to retain control of config specification when running on slurm. This generates an sbatch script which calls `manual_runner_target.py` which runs the equivalent simulation code to `decorated_runner.py`. The one upside of this method is that editing configs in `conf/` will not change the behavior of queued jobs, but is a bit more tedious to write and maintain, and doesn't have access to some of the QoL features of hydra.

Both of these eventually call the classes in `core/model.py`, which are an example of nested class initialization directly with a hydra config.

## How to use
This is just demo code, but runs with the following steps.

```conda env create -f environment.yml```

to create the environment. Then,


```python decorated_runner.py```
OR 
```python manual_runner.py```.

As implemented, `manual_runner.py` requires you to be on a SLURM cluster.

## Other comments
- Hydra has some built-in parameter sweeping functionality which can be combined with the `--multirun` option to automatically run multiple jobs. There are also other plugins such as Ax which can do more complex parameter sweeps/optimizations at the config level. I'm less familiar with these methods, but have worked with people who use them extensively (in a ML context).
See:

    https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/

    https://hydra.cc/docs/plugins/ax_sweeper/

- Hydra also has the ability to directly submit slurm jobs. I haven't played with this myself, but might be useful to get the benefits of the decorated initialization without running into job/config desync issues when queued.
See:

    https://hydra.cc/docs/plugins/submitit_launcher/

- Having some standardization across how we all run and parameterize jobs could be useful for maximizing code sharing and reuse in the lab. In particular, the contents of `core/` can be arbitrarily complex while maintaining the same entry points via hydra. Tasks such as active learning and parameter optimization that act at the config level and are model-agnostic would be easy to deploy lab-wide.

- Matlab has some 3rd party code for reading yaml files, potentially could be integrated into a hydra workflow as well.

## Links
https://hydra.cc/docs/intro/

https://omegaconf.readthedocs.io/en/2.3_branch/