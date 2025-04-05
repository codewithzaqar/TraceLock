import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="TraceLock - Username checker across websites.")
    parser.add_argument('--username', '-u', type=str, required=True, help='Username to search')
    parser.add_argument('--output', '-o', type=str, help='Optional output file path')
    return parser.parse_args()