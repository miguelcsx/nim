# src/utils/logger.py

import os
import logging
from glob import glob

def setup_logger(name, log_file: str, level=logging.INFO) -> logging.Logger:
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def cleanup_logs(log_dir: str, max_files=10) -> None:
    log_files = glob(os.path.join(log_dir, "*.log"))
    if len(log_files) > max_files:
        # Sort log files by creation time
        log_files.sort(key=os.path.getctime)
        # Delete the oldest files until the number of files is <= max_files
        files_to_delete = log_files[:len(log_files) - max_files]
        for file in files_to_delete:
            os.remove(file)
