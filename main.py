import json
from cores.checker import check_username

def main():
    username = input("Enter a username to search:").strip()

    with open("config/sites.json", "r") as f:
        sites = json.load(f)

    print(f"\n[TraceLock] Searching for '{username}'...\n")

    for site, url_template in sites.items():
        site_name, url, found = check_username(site, url_template, username)
        if found:
            print(f"[+] Found on {site_name}: {url}")
        else:
            print(f"[-] Not Found on {site_name}")

if __name__ == "__main__":
    main()