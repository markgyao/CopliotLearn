
# app/logging_config.py

import logging

def setup_logging():
    """
    Configures logging for the entire application.
    """
    logging.basicConfig(
        level=logging.INFO,  # Set the minimum log level
        format='%(asctime)s %(levelname)s %(name)s %(message)s',  # Log format
        handlers=[
            logging.FileHandler("app.log"),  # Log to a file
            logging.StreamHandler()          # Also log to the console
        ]
    )
