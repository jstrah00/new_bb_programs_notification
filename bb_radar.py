import requests
import re
from logger import get_logger


logger = get_logger(__name__)

def fetch_programs():
    logger.debug("Getting nonce")
    nonce = get_nonce()
    logger.debug(f"Nonce: {nonce}")
    logger.debug("Fetching programs from BB Radar...")
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
    logger.debug(f"Response status code: {response.status_code}")
    #logger.debug("Response content:", response.content)


    
    if response.ok:
        return response.json()
    else:
        logger.error(f"Request failed with status {response.status_code}")

def get_nonce():
    page = requests.get("https://bbradar.io")
    match = re.search(r'id="wdtNonceFrontendServerSide_1"[^>]*value="([^"]+)"', page.text)
    if match:
        return match.group(1)
    else:
        logger.error("Could not find nonce")
        return 
