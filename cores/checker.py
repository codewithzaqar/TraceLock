import requests

def check_username(site_name, url_template, username, results):
    url = url_template.format(username)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            results.append((site_name, url, True))
        else:
            results.append((site_name, url, False))
    except requests.RequestException:
        results.append((site_name, url, False))