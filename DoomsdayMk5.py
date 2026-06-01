import time
from datetime import datetime, timedelta

# Constants (Planck 2018 best-fit values)
H0_km_s_Mpc = 67.4  # Hubble constant
Omega_m = 0.315
Omega_lambda = 0.685

# Estimated time until heat death (very rough, in years)
# Here we pick ~1e100 years for proton decay/black hole evaporation
YEARS_UNTIL_HEAT_DEATH = 10**100  

def countdown(seconds_until_end):
    """High-precision countdown."""
    target_time = time.time() + seconds_until_end
    try:
        while True:
            now = time.time()
            remaining = target_time - now
            if remaining <= 0:
                print("\n💥 Universe has reached heat death! 💥")
                break

            # Convert to years, days, hours, minutes, seconds
            years = int(remaining // (365.25 * 24 * 3600))
            days = int((remaining % (365.25 * 24 * 3600)) // (24 * 3600))
            hours = int((remaining % (24 * 3600)) // 3600)
            minutes = int((remaining % 3600) // 60)
            seconds = int(remaining % 60)

            print(f"\rTime until heat death: {years}y {days}d {hours:02}h {minutes:02}m {seconds:02}s", end="")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

if __name__ == "__main__":
    # Convert years to seconds
    seconds_until_end = YEARS_UNTIL_HEAT_DEATH * 365.25 * 24 * 3600
    countdown(seconds_until_end)
