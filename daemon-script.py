import os
import sys
import time
import signal
import logging

# Setup logging
logging.basicConfig(filename="daemon.log", level=logging.DEBUG)


# Function to handle SIGTERM signal
def sigterm_handler(signum, frame):
    logging.info("Received SIGTERM signal. Exiting...")
    sys.exit(0)


# Register SIGTERM signal handler
signal.signal(signal.SIGTERM, sigterm_handler)


# Main daemon loop
def main():
    logging.info("Daemon started.")
    while True:
        # Your daemon's main functionality goes here
        logging.info("Daemon is running...")
        time.sleep(5)


if __name__ == "__main__":
    # Check if the daemon is already running
    pid = str(os.getpid())
    pidfile = "/tmp/daemon.pid"

    if os.path.isfile(pidfile):
        print("Daemon is already running.")
        sys.exit()

    # Create the PID file
    open(pidfile, "w").write(pid)

    try:
        main()
    except Exception as e:
        logging.exception("Exception occurred: %s", str(e))
    finally:
        # Remove PID file when the daemon exits
        os.unlink(pidfile)
