import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

# Defining the thresholds
cpu_alert_threshold = 90
memory_alert_threshold = 85
disk_space_alert_threshold = 20

# Checking and alerting for high CPU usage
if cpu_usage > cpu_alert_threshold:
    print("High CPU usage alert!")
elif cpu_usage > 80:  # Assuming 80-90 as the gray zone for CPU
    pass  # Silently logging moderate CPU usage

# Checking and alerting for high memory usage
if memory_usage > memory_alert_threshold:
    print("High memory usage alert!")
elif memory_usage > 70:  # Assuming 70-85 as the gray zone for memory
    pass  # Silently logging moderate memory usage

# Checking and alerting for low disk space
if disk_space < disk_space_alert_threshold:
    print("Low disk space alert!")
elif disk_space < 30:  # Assuming 20-30 as the gray zone for disk space
    pass  # Silently logging low disk space

# General alert for normal system status
if cpu_usage < 80 and memory_usage < 70 and disk_space > 30:
    print("System status normal.")
