import os
from collections import defaultdict, Counter

MAX_FILE_SIZE_MB = 100

def is_valid_file(file_path):
    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return False
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    if size_mb > MAX_FILE_SIZE_MB:
        print(f"Error: File size exceeds {MAX_FILE_SIZE_MB} MB limit. Current size: {size_mb:.2f} MB")
        return False
    return True

def parse_log_line(line):
    """
    Parses a log line assuming common log format: 
    127.0.0.1 - - [timestamp] "GET /index.html HTTP/1.1" 200 1043
    Returns (ip, url, status_code)
    """
    try:
        parts = line.split()
        ip = parts[0]
        url = parts[6]
        status = parts[8]
        return ip, url, status
    except IndexError:
        return None, None, None  # malformed line

def analyze_log_file(file_path):
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            ip, url, status = parse_log_line(line)
            if ip and url and status:
                ip_counter[ip] += 1
                url_counter[url] += 1
                status_counter[status] += 1

    return ip_counter, url_counter, status_counter

def print_top_n(counter, label, n=5):
    print(f"\nTop {n} {label}:")
    for item, count in counter.most_common(n):
        print(f"{item} → {count} times")

def main():
    file_path = input("Enter path to log file (<=100 MB): ").strip()
    
    if not is_valid_file(file_path):
        return
    
    ip_counter, url_counter, status_counter = analyze_log_file(file_path)

    print_top_n(ip_counter, "IP addresses")
    print_top_n(url_counter, "URLs")
    print_top_n(status_counter, "HTTP Status Codes")

if __name__ == "__main__":
    main()
