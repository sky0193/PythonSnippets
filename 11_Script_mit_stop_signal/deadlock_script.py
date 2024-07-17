import signal
import sys
import time

def signal_handler(sig, frame):
    print('Received signal to terminate the script.')
    sys.exit(0)

# Set up signal handler
signal.signal(signal.SIGINT, signal_handler)  # Handle interrupt signal (Ctrl+C)
signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signal

while True:
    while 1:
    	print('Running...')
    	time.sleep(999)

