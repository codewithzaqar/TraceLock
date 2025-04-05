import json
import time
import threading
import os
from cores.checker import check_username
from cli.args import parse_args
from colorama import Fore, init

init(autoreset=True)

def save_results(results, output_file, output_format='txt'):
    if output_format == 'json':
        with open(output_file, 'w') as json_file:
            json.dump(results, json_file, indent=4)
    else:
        with open(output_file, 'w') as txt_file:
            for site_name, url, _ in results:
                txt_file.write(f"{site_name}: {url}\n")

def main():
    args = parse_args()
    username = args.username
    output_format = 'json' if args.output_json else 'txt'

    with open("config/sites.json", "r") as f:
        sites = json.load(f)

    results = []
    threads = []

    print(f"\n{Fore.YELLOW}[TraceLock] Searching for '{username}' across {len(sites)} sites...\n")
    start_time = time.time()

    for site, url_template in sites.items():
        thread = threading.Thread(target=check_username, args=(site, url_template, username, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join() 

    found_results = sorted([r for r in results if r[2]])
    for site_name, url, _ in found_results:
        print(f"{Fore.GREEN}[+] Found on {site_name}: {url}")

    not_found = len(sites) - len(found_results)
    print(f"\n{Fore.RED}Scan complete: {len(found_results)}, found, {not_found} not found")
    print(f"Time taken: {round(time.time() - start_time, 2)}s")
        
    if args.output:
       save_results(found_results, args.output, output_format)
       if output_format == 'json':
           print(f"{Fore.CYAN}Results saved to {args.output} in JSON format")
       else:
           print(f"{Fore.CYAN}Results saved to {args.output}")

if __name__ == "__main__":
    main()