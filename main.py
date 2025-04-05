import json
import time
import threading
from cores.checker import check_username
from cli.args import parse_args

def main():
    args = parse_args()
    username = args.username

    with open("config/sites.json", "r") as f:
        sites = json.load(f)

    results = []
    threads = []

    print(f"\n[TraceLock] Searching for '{username}' across {len(sites)} sites...\n")
    start_time = time.time()

    for site, url_template in sites.items():
        thread = threading.Thread(target=check_username, args=(site, url_template, username, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join() 

    found_results = sorted([r for r in results if r[2]])
    for site_name, url, _ in found_results:
        print(f"[+] Found on {site_name}: {url}")

    not_found = len(sites) - len(found_results)
    print(f"\nScan complete: {len(found_results)}, found, {not_found} not found")
    print(f"Time taken: {round(time.time() - start_time, 2)}s")
        
    if args.output:
        with open(args.output, 'w') as f:
            for site_name, url, _ in found_results:
                f.write(f"{site_name}: {url}\n")
        print(f"Results saved to {args.output}")

if __name__ == "__main__":
    main()