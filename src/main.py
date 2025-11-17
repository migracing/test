import logging
import time
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,                       # Minimum level to capture
    format="%(asctime)s [%(levelname)s] %(message)s",  # Timestamp + level
    handlers=[
        logging.StreamHandler(sys.stdout),    # Send logs to Docker stdout
        logging.FileHandler("/app/log.txt")   # Optional: also write to file
    ]
)

logger = logging.getLogger()

# Example log entries
logger.info("Hello World logged via logging module!")

# Keep container alive so you can see logs
while True:
    logger.info("Still alive...")
    print("This is printing from a 'print' statement.")
    print("This is dev branch.")
    time.sleep(5)
