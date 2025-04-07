import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = 'src'

list_of_files = [
    f"{project_name}/__init__.py",
    
    # Components
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_cleaning.py",
    f"{project_name}/components/model_training.py",
    f"{project_name}/components/model_evaluation.py",
    
    # Pipelines
    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/pipelines/training_pipeline.py",
    f"{project_name}/pipelines/prediction_pipeline.py",
    
    # Utilities
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/common.py",

    # Config and constants
    "config/config.yaml",
    f"{project_name}/constants/__init__.py",
    
    # Main, App, and Setup
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "Dockerfile",
    "README.md",

    # Folders for data & model artifacts
    "data/.gitkeep",
    "artifacts/.gitkeep",
    "notebooks/eda.ipynb",
    "mlruns/.gitkeep",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
