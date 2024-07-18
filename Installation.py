import os
import sys

def setup_environment():
    # Create necessary directories or perform any initial setup tasks
    base_directory = 'C:/Users/owner'
    wcpl_directory = os.path.join(base_directory, 'wcpl')
    
    os.makedirs(wcpl_directory, exist_ok=True)
    print(f"Directories set up successfully. WCPL directory: {wcpl_directory}")

def configure_environment():
    # Configure environment variables or any other necessary configurations
    base_directory = 'C:/Users/owner'
    wcpl_home = os.path.join(base_directory, 'wcpl')
    
    os.environ['WCPL_HOME'] = wcpl_home
    print(f"Environment configured. WCPL_HOME set to: {wcpl_home}")

def main():
    print("Starting WCPL installation...")
    setup_environment()
    configure_environment()
    print("WCPL installation completed successfully.")

if __name__ == "__main__":
    main()
