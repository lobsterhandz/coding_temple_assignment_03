import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif memory_usage > 85:
    print("High memory usage!")
elif disk_space < 20:
    print("Low disk space!")
else:
    pass  # Silently logging normal system status
