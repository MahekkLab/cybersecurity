import hashlib
import time
import os

FILE = "important.txt"   # file to monitor
CHECK_INTERVAL = 2       # seconds

def get_hash(filename):
    """Returns the SHA-256 hash of the file."""
    if not os.path.exists(filename):
        return None
    with open(filename, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def monitor_file():
    print("=== File Integrity Monitor ===")
    print(f"Monitoring: {FILE}\n")

    old_hash = get_hash(FILE)

    if old_hash is None:
        print("❌ File not found! Create the file first.")
        return

    while True:
        new_hash = get_hash(FILE)

        if new_hash != old_hash:
            print("\n⚠ ALERT: File has been modified!")
            print(f"Old Hash: {old_hash}")
            print(f"New Hash: {new_hash}\n")
            old_hash = new_hash   # update hash

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_file()
