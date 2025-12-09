from src.bsm import BlackScholesModel

def main():
    # --- Parameter Setup ---
    S_0 = 100.0       # Spot Price
    K_0 = 100.0       # Strike Price (ATM)
    T_0 = 1.0         # Time to Maturity (1 year)
    r_0 = 0.05        # Risk-free Rate (5%)
    sigma_0 = 0.2     # Volatility (20%)

    # Initialize the model
    bsm = BlackScholesModel(S=S_0, K=K_0, T=T_0, r=r_0, sigma=sigma_0)

    # Calculate Prices
    call_price = bsm.calculate_price(option_type='call')
    put_price = bsm.calculate_price(option_type='put')

    # Calculate Greeks
    greeks = bsm.calculate_greeks()

    # --- Display Results ---
    print(f"{'='*30}")
    print(f" Black-Scholes Model Results")
    print(f"{'='*30}")
    print(f"Parameters:")
    print(f" S={S_0}, K={K_0}, T={T_0}, r={r_0}, sigma={sigma_0}")
    print(f"{'-'*30}")
    print(f"Call Option Price: {call_price:.4f}")
    print(f"Put Option Price : {put_price:.4f}")
    print(f"{'-'*30}")
    print(f"Option Greeks (Call):")
    print(f" Delta : {greeks['Delta_Call']:.4f}")
    print(f" Gamma : {greeks['Gamma']:.4f}")
    print(f" Vega  : {greeks['Vega']:.4f}")
    print(f" Theta : {greeks['Theta_Call']:.4f} (per day)")
    print(f" Rho   : {greeks['Rho_Call']:.4f}")
    print(f"{'='*30}")

if __name__ == "__main__":
    main()