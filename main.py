import json
from cores.checker import check_username
from cli.args import parse_args

def main():
    args = parse_args()
    username = args.username

    with open("config/sites.json", "r") as f:
        sites = json.load(f)

    results = []

    print(f"\n[TraceLock] Searching for '{username}'...\n")

    for site, url_template in sites.items():
        site_name, url, found = check_username(site, url_template, username)
        if found:
            print(f"[+] Found on {site_name}: {url}")
            results.append(f"[+] {site_name}: {url}")
        else:
            print(f"[-] Not Found on {site_name}")
        
    if args.output:
        with open(args.output, 'w') as out_file:
            out_file.write("\n".join(results))
        print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main()