import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    """
    A class to calculate European option prices and Greeks using the Black-Scholes-Merton model.
    """

    def __init__(self, S: float, K: float, T: float, r: float, sigma: float):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self._d1 = None
        self._d2 = None
        self._calculate_d1_d2()

    def _calculate_d1_d2(self):
        if self.T <= 0:
            raise ValueError("Time to maturity (T) must be positive.")
        self._d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        self._d2 = self._d1 - self.sigma * np.sqrt(self.T)

    def calculate_price(self, option_type: str = 'call') -> float:
        if option_type == 'call':
            price = self.S * norm.cdf(self._d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(self._d2)
        elif option_type == 'put':
            price = self.K * np.exp(-self.r * self.T) * norm.cdf(-self._d2) - self.S * norm.cdf(-self._d1)
        else:
            raise ValueError("Option type must be either 'call' or 'put'.")
        return price

    def calculate_greeks(self) -> dict:
        N_prime_d1 = norm.pdf(self._d1)
        delta_call = norm.cdf(self._d1)
        delta_put = delta_call - 1
        gamma = N_prime_d1 / (self.S * self.sigma * np.sqrt(self.T))
        vega = self.S * N_prime_d1 * np.sqrt(self.T) / 100 
        theta_call = (- (self.S * self.sigma * N_prime_d1) / (2 * np.sqrt(self.T)) 
                      - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self._d2)) / 365
        rho_call = (self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self._d2)) / 100

        return {
            "Delta_Call": delta_call,
            "Delta_Put": delta_put,
            "Gamma": gamma,
            "Vega": vega,
            "Theta_Call": theta_call,
            "Rho_Call": rho_call
        }