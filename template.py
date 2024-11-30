import os
from pathlib import Path
import logging

# Setting up logging to provide clear information during execution
# INFO level ensures visibility into key steps like directory and file creation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the project name for the directory structure
project_name = "textSummarizer"

# List of all directories and files to be created in the project
list_of_files = [
    ".github/workflows/.gitkeep",  # Placeholder file for GitHub Actions workflow folder
    f"src/{project_name}/__init__.py",  # Initialize the main package
    f"src/{project_name}/conponents/__init__.py",  # Sub-package for components
    f"src/{project_name}/utils/__init__.py",  # Sub-package for utility functions
    f"src/{project_name}/utils/common.py",  # Common utility functions
    f"src/{project_name}/logging/__init__.py",  # Sub-package for logging configuration
    f"src/{project_name}/config/__init__.py",  # Sub-package for configuration management
    f"src/{project_name}/config/configuration.py",  # Script for configuration handling
    f"src/{project_name}/pipeline/__init__.py",  # Sub-package for ML pipelines
    f"src/{project_name}/entity/__init__.py",  # Sub-package for entity classes or data models
    f"src/{project_name}/constants/__init__.py",  # Sub-package for constants
    "config/config.yaml",  # Configuration file (e.g., for hyperparameters or settings)
    "params.yaml",  # Parameters file for experiments
    "app.py",  # Main app file for running the project
    "main.py",  # Entry point for the application
    "Dockerfile",  # Dockerfile for containerizing the application
    "requirements.txt",  # List of dependencies
    "setup.py",  # Script for packaging and installation
    "research/trials.ipynb",  # Jupyter notebook for research and experimentation
]

# Iterate through the list of files to create the directory structure and empty files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path to a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and file name

    # Check if the directory part of the path exists; if not, create it
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create the file if it does not exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:  # Open the file in write mode
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        # Log that the file already exists
        logging.info(f"{filename} already exists")
