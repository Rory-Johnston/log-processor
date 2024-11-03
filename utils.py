import os

VALID_LOG_LEVELS = {'INFO', 'WARN', 'ERROR'}

def validate_log_levels(levels):
    invalid_levels = [level for level in levels if level not in VALID_LOG_LEVELS]
    if invalid_levels:
        print(f"Error: The following log levels are not valid: {', '.join(invalid_levels)}")
        print(f"Valid log levels are: {', '.join(VALID_LOG_LEVELS)}")
        return False
    return True

def validate_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return False
    if not os.path.isfile(file_path):
        print(f"Error: The path '{file_path}' is not a file.")
        return False
    if not os.access(file_path, os.R_OK):
        print(f"Error: The file '{file_path}' is not readable.")
        return False
    return True