import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80:
    pass  # Silently ignoring moderate CPU usage
