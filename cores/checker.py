import requests

def check_username(site_name, url_template, username):
    url = url_template.format(username)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return (site_name, url, True)
        else:
            return (site_name, url, False)
    except requests.RequestException:
        return (site_name, url, False)