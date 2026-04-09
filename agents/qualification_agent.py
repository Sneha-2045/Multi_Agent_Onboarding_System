
def calculate_score(lead):

    score = 0

    if lead.get("aadhaar_status") == "complete":
        score += 25

    if lead.get("bank_status") == "complete":
        score += 25

    if lead.get("rc_status") == "complete":
        score += 25

    if lead.get("app_installed") == "yes":
        score += 25

    return score


def determine_stage(lead):

    missing = []

    if lead.get("aadhaar_status") != "complete":
        missing.append("aadhaar")

    if lead.get("bank_status") != "complete":
        missing.append("bank")

    if lead.get("rc_status") != "complete":
        missing.append("rc")

    if lead.get("app_installed") != "yes":
        missing.append("app")

    stage = "Qualified" if len(missing) == 0 else "Pending"

    return stage, missing