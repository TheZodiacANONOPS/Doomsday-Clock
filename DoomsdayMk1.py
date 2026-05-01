import time

class Hopper:
    def __init__(self, name):
        self.name = name
        self.items = 0

    def transfer_to(self, other):
        """Transfer one item to another hopper if possible."""
        if self.items > 0:
            self.items -= 1
            other.items += 1
            return True
        return False

class EthoHopperClock:
    def __init__(self, items, tick_time=0.05):
        """
        items: number of items in the clock (affects delay)
        tick_time: seconds per Minecraft tick (default 0.05s)
        """
        self.hopper_a = Hopper("A")
        self.hopper_b = Hopper("B")
        self.hopper_a.items = items
        self.tick_time = tick_time
        self.state = "A_to_B"  # Direction of transfer

    def run(self, cycles=2):
        """Run the hopper clock for a given number of cycles."""
        for cycle in range(cycles):
            print(f"\nCycle {cycle + 1} starting...")
            while self.hopper_a.items > 0:
                self.hopper_a.transfer_to(self.hopper_b)
                print(f"A: {self.hopper_a.items} | B: {self.hopper_b.items}")
                time.sleep(self.tick_time)

            # Output trigger (like redstone comparator)
            print("🔴 Output triggered (A empty)")

            # Swap direction
            self.hopper_a, self.hopper_b = self.hopper_b, self.hopper_a
            self.state = "B_to_A" if self.state == "A_to_B" else "A_to_B"

# Example usage
if __name__ == "__main__":
    clock = EthoHopperClock(items=10, tick_time=0.05)  # 10 items = ~0.5s per side
    clock.run(cycles=3)
