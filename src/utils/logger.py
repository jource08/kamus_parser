import logging
import os

def setup_logger():
    log_dir = os.path.join(os.path.dirname(__file__), '../../logs')  # Adjusted path
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        filename=os.path.join(log_dir, 'errors.log'),
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )