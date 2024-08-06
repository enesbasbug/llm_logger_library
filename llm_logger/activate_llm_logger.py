import os
from datetime import datetime
import inspect

def activate_llm_logger(user_prompt, system_prompt, result):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    calling_frame = inspect.currentframe().f_back
    calling_function = calling_frame.f_code.co_name if calling_frame else "Unknown"
    
    log_message = (
        f"{timestamp} - Function: {calling_function}\n"
        f"System Prompt: {system_prompt}\n"
        f"User Prompt: {user_prompt}\n"
        f"Response: {result}\n"
        "------\n"
    )
    
    print(log_message)  # Print to console
    
    log_folder = "logs"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    log_file = os.path.join(log_folder, f"log-{datetime.now().strftime('%Y-%m-%d')}.log")
    with open(log_file, "a") as f:
        f.write(log_message)