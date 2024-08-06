import os
from datetime import datetime
import inspect

class Logger:
    def __init__(self, log_folder="logs"):
        self.log_folder = log_folder
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

    def log(self, system_prompt, user_prompt, response):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        calling_frame = inspect.currentframe().f_back
        calling_function = calling_frame.f_code.co_name if calling_frame else "Unknown"
        
        log_message = (
            f"{timestamp} - Function: {calling_function}\n"
            f"System Prompt: {system_prompt}\n"
            f"User Prompt: {user_prompt}\n"
            f"Response: {response}\n"
            "------\n"
        )
        
        print(log_message)  # Print to console
        
        log_file = os.path.join(self.log_folder, f"{datetime.now().strftime('%Y-%m-%d')}.log")
        with open(log_file, "a") as f:
            f.write(log_message)

logger = Logger()