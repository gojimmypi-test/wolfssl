# Import("env")
import subprocess
import sys

# Function to install a package
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    # Check if cryptography is installed
    import cryptography
except ImportError:
    # If not installed, install it
    print("cryptography package not found. Installing...")
    install("cryptography")
