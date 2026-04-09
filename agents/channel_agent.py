import re

def extract_info(text):

    text = text.lower()

    info = {}

    # Aadhaar
    if any(word in text for word in ["aadhaar", "aadhar", "id proof"]):
        info["aadhaar_status"] = "complete"

    # Bank
    if any(word in text for word in ["bank", "account", "cheque"]):
        info["bank_status"] = "complete"

    # RC
    if any(word in text for word in ["rc", "registration", "vehicle"]):
        info["rc_status"] = "complete"

    # App
    if any(word in text for word in ["install", "download", "app"]):
        info["app_installed"] = "yes"

    # Callback
    if any(word in text for word in ["call", "later", "tomorrow"]):
        info["callback_required"] = "yes"
    else:
        info["callback_required"] = "no"

    # Intent Detection
    if "uploaded" in text or "shared" in text:
        info["intent"] = "document_submission"
    elif "call" in text:
        info["intent"] = "callback"
    else:
        info["intent"] = "update"

    return info