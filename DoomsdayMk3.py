from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
from datetime import datetime, timedelta
import time
import math

def big_rip_time(H0, Omega_Lambda, w):
    """
    Calculate time until Big Rip in Gyr.
    H0: Hubble constant in km/s/Mpc
    Omega_Lambda: Dark energy density parameter
    w: Dark energy equation-of-state parameter
    """
    if w >= -1:
        return math.inf  # No Big Rip for w >= -1

    # Convert H0 to 1/Gyr
    H0_s = (H0 / u.s).to(1 / u.Gyr).value
    delta_t_gyr = 2 / (3 * abs(1 + w) * H0_s * math.sqrt(Omega_Lambda))
    return delta_t_gyr

def countdown(seconds_remaining):
    """Live countdown display."""
    try:
        while seconds_remaining > 0:
            days, seconds = divmod(int(seconds_remaining), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            print(f"\r{days} days, {hours}h {minutes}m {seconds}s remaining", end="")
            time.sleep(1)
            seconds_remaining -= 1
        print("\n💥 The universe has reached its modeled end!")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

if __name__ == "__main__":
    # Define cosmology (Planck 2018 values)
    H0 = 67.4 * u.km / u.s / u.Mpc
    Omega_m = 0.315
    Omega_Lambda = 1 - Omega_m
    w = -1.1  # Phantom energy for Big Rip scenario

    cosmo = FlatLambdaCDM(H0=H0, Om0=Omega_m)

    # Current age of the universe
    age_now_gyr = cosmo.age(0).value

    # Time until Big Rip
    delta_t_gyr = big_rip_time(H0, Omega_Lambda, w)

    if math.isinf(delta_t_gyr):
        print("No Big Rip predicted for w >= -1 (Heat Death scenario).")
    else:
        rip_years_from_now = delta_t_gyr
        rip_seconds = rip_years_from_now * 1e9 * 365.25 * 24 * 3600

        end_time = datetime.utcnow() + timedelta(seconds=rip_seconds)
        print(f"Big Rip predicted in ~{rip_years_from_now:.2f} Gyr")
        print(f"Estimated end date: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
        print("Countdown:")
        countdown(rip_seconds)
