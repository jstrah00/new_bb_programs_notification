import requests
import json
import re

def fetch_programs():
    print("Getting nonce")
    nonce = get_nonce()
    print("Nonce: ", nonce)
    print("Fetching programs from BB Radar...")
    url = "https://bbradar.io/wp-admin/admin-ajax.php?action=get_wdtable&table_id=1"
    
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    data = {
        "draw": 1,
        "order[0][column]": 1,
        "order[0][dir]": "desc",
        "length": 25,
        "wdtNonce": nonce
    }

    response = requests.post(url, headers=headers, data=data)
    print("Response status code:", response.status_code)
    #print("Response content:", response.content)


    
    if response.ok:
        return response.json()
    else:
        print(f"Request failed with status {response.status_code}")

def get_nonce():
    page = requests.get("https://bbradar.io")
    match = re.search(r'id="wdtNonceFrontendServerSide_1"[^>]*value="([^"]+)"', page.text)
    if match:
        return match.group(1)
    else:
        print("Could not find nonce")
        return 
