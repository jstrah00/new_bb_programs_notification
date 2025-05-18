from logger import get_logger


logger = get_logger(__name__)


def get_platform(content):
    if "intigriti" in content.lower():
        return "Intigriti"
    if "hackerone" in content.lower():
        return "Hackerone"
    if "bugcrowd" in content.lower():
        return "Bugcrowd"
    if "remedy" in content.lower():
        return "Remedy"
    return "Unknown"

def get_url(content):
    href_content = content.split("href=")[1]
    return href_content.split("'")[1]

def sanitize_bb_radar_response(bb_radar_response):
    logger.debug("Sanitizing BB Radar response...")
    results = []
    #logger.debug(len(bb_radar_response["data"]))
    for item in bb_radar_response["data"]:
        data = {
                "program": item[3],
                "type": item[5],
                "platform": get_platform(item[2]),
                "url": get_url(item[6])
                }
        results.append(data)
    return results

def get_interesting_programs(programs: []):
    interesting_programs = []
    for program in programs:
        if "wildcard" in program["type"].lower():
            interesting_programs.append(program)
    return interesting_programs
