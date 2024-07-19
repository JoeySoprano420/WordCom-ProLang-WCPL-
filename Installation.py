import os
import sys

def setup_environment():
    """
    Create necessary directories or perform any initial setup tasks.
    """
    base_directory = 'C:/Users/owner'
    wcpl_directory = os.path.join(base_directory, 'wcpl')

    # Create the main WCPL directory
    os.makedirs(wcpl_directory, exist_ok=True)
    
    # Create additional directories if needed
    os.makedirs(os.path.join(wcpl_directory, 'scripts'), exist_ok=True)
    os.makedirs(os.path.join(wcpl_directory, 'projects'), exist_ok=True)
    os.makedirs(os.path.join(wcpl_directory, 'data'), exist_ok=True)
    
    print(f"Directories set up successfully. WCPL directory: {wcpl_directory}")

def configure_environment():
    """
    Configure environment variables or any other necessary configurations.
    """
    base_directory = 'C:/Users/owner'
    wcpl_home = os.path.join(base_directory, 'wcpl')
    
    # Set environment variables
    os.environ['WCPL_HOME'] = wcpl_home
    print(f"Environment configured. WCPL_HOME set to: {wcpl_home}")

    # Example: Set PATH variable if necessary
    path_variable = os.getenv('PATH', '')
    if wcpl_directory not in path_variable:
        new_path = f"{path_variable};{wcpl_home}\\scripts"
        os.environ['PATH'] = new_path
        print(f"PATH updated to include: {wcpl_home}\\scripts")

def main():
    """
    Main function to start the WCPL installation process.
    """
    print("Starting WCPL installation...")
    setup_environment()
    configure_environment()
    print("WCPL installation completed successfully.")
    
    # Optionally, print out environment variables or other configuration details
    print("Current Environment Variables:")
    for var in ['WCPL_HOME', 'PATH']:
        print(f"{var}: {os.getenv(var)}")

if __name__ == "__main__":
    main()
