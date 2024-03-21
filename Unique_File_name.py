from datetime import datetime
import time

base_filename = 'ABC'
# Create a unique filename
while True:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_filename = f"{base_filename}_{timestamp}.csv"
    print(unique_filename)
    time.sleep(0.5)  # Delay for 0.5 seconds
