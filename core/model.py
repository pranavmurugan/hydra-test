import numpy as np
import hydra
from omegaconf import OmegaConf

class Step:
    mu: float
    sigma: float
    
    def __init__(self, mu, sigma):
        # These parameters will be filled in directly by the config object
        self.mu = mu
        self.sigma = sigma


class DemoModel:
    n: int
    
    def __init__(self, step1, step2, n):
        # These parameters will be filled in directly by the config object
        self.step1 = step1
        self.step2 = step2
        self.n = n
    
    def __call__(self, n_trials, n_steps):
        # Does random stuff
        for _ in range(n_trials):
            for _ in range(n_steps):
                x = np.random.randn(self.n)*self.step1.sigma + self.step1.mu
                y = np.random.randn(self.n)*self.step2.sigma + self.step2.mu
                
                z = x + y
        
        return z