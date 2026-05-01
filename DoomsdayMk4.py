from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
from datetime import datetime, timedelta
import math
import time

# ------------------------------
# Cosmology-based calculations
# ------------------------------

def big_rip_time(H0, Omega_Lambda, w):
    """Return time until Big Rip in Gyr, or inf if no Big Rip."""
    if w >= -1:
        return math.inf
    H0_s = (H0 / u.s).to(1 / u.Gyr).value
    delta_t_gyr = 2 / (3 * abs(1 + w) * H0_s * math.sqrt(Omega_Lambda))
    return delta_t_gyr

def big_crunch_time(cosmo):
    """
    Estimate time until Big Crunch for a closed universe (Omega_m > 1).
    Uses a simple approximation: total lifetime ~ 2 * current age.
    """
    if cosmo.Om0 <= 1:
        return math.inf
    age_now = cosmo.age(0).value
    return 2 * age_now - age_now  # Remaining time = total - current

# ------------------------------
# Countdown display
# ------------------------------

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

# ------------------------------
# Main program
# ------------------------------

if __name__ == "__main__":
    # Default cosmology (Planck 2018)
    H0 = 67.4 * u.km / u.s / u.Mpc
    Omega_m = 0.315
    Omega_Lambda = 1 - Omega_m
    w = -1.1  # Change this to test scenarios

    cosmo = FlatLambdaCDM(H0=H0, Om0=Omega_m)

    print("Choose a cosmological model:")
    print("1 - Big Rip (w < -1)")
    print("2 - Big Crunch (Omega_m > 1)")
    print("3 - Heat Death (w >= -1)")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        delta_t_gyr = big_rip_time(H0, Omega_Lambda, w)
        if math.isinf(delta_t_gyr):
            print("No Big Rip predicted for w >= -1.")
        else:
            rip_seconds = delta_t_gyr * 1e9 * 365.25 * 24 * 3600
            end_time = datetime.utcnow() + timedelta(seconds=rip_seconds)
            print(f"Big Rip predicted in ~{delta_t_gyr:.2f} Gyr")
            print(f"Estimated end date: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
            countdown(rip_seconds)

    elif choice == "2":
        delta_t_gyr = big_crunch_time(cosmo)
        if math.isinf(delta_t_gyr):
            print("No Big Crunch predicted for Omega_m <= 1.")
        else:
            crunch_seconds = delta_t_gyr * 1e9 * 365.25 * 24 * 3600
            end_time = datetime.utcnow() + timedelta(seconds=crunch_seconds)
            print(f"Big Crunch predicted in ~{delta_t_gyr:.2f} Gyr")
            print(f"Estimated end date: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
            countdown(crunch_seconds)

    elif choice == "3":
        print("Heat Death scenario: expansion continues forever.")
        print("No finite countdown possible.")
    else:
        print("Invalid choice.")
