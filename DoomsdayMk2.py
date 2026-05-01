import time
from datetime import datetime, timedelta

# Cosmological model estimates (in years from now)
MODELS = {
    "heat_death": 1e100,  # Heat death (entropy max)
    "big_rip": 22e9,      # Big Rip in ~22 billion years
    "big_crunch": 100e9   # Big Crunch in ~100 billion years
}

def universe_death_clock(model: str):
    """Calculate and display the countdown to the universe's end."""
    if model not in MODELS:
        raise ValueError(f"Unknown model '{model}'. Choose from: {list(MODELS.keys())}")

    years_remaining = MODELS[model]
    now = datetime.utcnow()

    # Convert years to seconds (approximate, ignoring leap seconds)
    seconds_remaining = years_remaining * 365.25 * 24 * 3600
    end_time = now + timedelta(seconds=seconds_remaining)

    print(f"Model: {model.replace('_', ' ').title()}")
    print(f"Estimated end date: {end_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("Countdown:")

    try:
        while True:
            now = datetime.utcnow()
            remaining = end_time - now
            if remaining.total_seconds() <= 0:
                print("\n💥 The universe has reached its modeled end!")
                break

            days, seconds = divmod(int(remaining.total_seconds()), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)

            print(f"\r{days} days, {hours}h {minutes}m {seconds}s remaining", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

if __name__ == "__main__":
    print("Choose a cosmological model:")
    for m in MODELS:
        print(f" - {m}")
    choice = input("Enter model: ").strip().lower()

    try:
        universe_death_clock(choice)
    except ValueError as e:
        print(e)
