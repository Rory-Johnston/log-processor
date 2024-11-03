import argparse
import time

from utils import validate_file, validate_log_levels

def main():
    # parse arguments from the command line
    parser = argparse.ArgumentParser(description='Process log file.')
    parser.add_argument('--file', type=str, required=True, help='The log file to process.')
    parser.add_argument('--level', type=str, help='The logging levels to filter, comma-separated.')
    parser.add_argument('--output', type=str, help='Optional output file to write the summary.')
    args = parser.parse_args()

    # validate that the file exists, is infact a file and is readable
    if not validate_file(args.file):
        return
    
    # validate that the inputted log level filter is proper
    if args.level:
        levels = [level.strip().upper() for level in args.level.split(',')]
        if not validate_log_levels(levels):
            return
    else:
        levels = None

    read_file(args.file, levels, args.output)

def read_file(file_path, log_levels, output_file=None):
    start = time.time()
    total_processed_logs = 0
    log_level_counts = {}
    unique_users = set()

    # open the file and for every line, parse the text
    with open(file_path, 'r') as file:
        for line in file:
            raw_line = line.strip()
            parsed_line = raw_line.split(',')

            if len(parsed_line) < 4:
                continue 

            log_level = parsed_line[1].strip().upper()
            uid = parsed_line[3].strip()

            if not log_levels or log_level in log_levels:
                log_level_counts[log_level] = log_level_counts.get(log_level, 0) + 1
                unique_users.add(uid)
                total_processed_logs += 1 
    
    end = time.time()

    summary = "\nLog Level Counts:\n"
    for level, count in log_level_counts.items():
        summary += f"{level}: {count}\n"
    summary += f"\nTotal Processed Logs: {total_processed_logs}\n"
    summary += f"\nUnique Users: {list(unique_users)}\n"
    summary += f"Processing time: {(end - start)} seconds\n"

    print(summary)

    if output_file:
        with open(output_file, 'w') as file:
            file.write(summary)
        print(f"Summary written to {output_file}")

if __name__ == "__main__":
    main()
