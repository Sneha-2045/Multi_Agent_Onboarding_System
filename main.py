from agents.ingestion_agent import ingest_csv
from agents.channel_agent import extract_info
from agents.reconcilation_agent import reconcile
from agents.qualification_agent import calculate_score, determine_stage
from agents.response_agent import generate_response, generate_callback
from agents.sync_agent import sync

from database.db import get_lead

def simulate():

    ingest_csv("data/leads.csv")

    message = open("data/whatsapp.txt").read()

    lead_id = 1

    old = get_lead(lead_id)

    new = extract_info(message)

    updated = reconcile(old, new)

    score = calculate_score(updated)

    stage, missing = determine_stage(updated)

    whatsapp, email = generate_response(updated, missing)

    callback = generate_callback(updated)

    updated["lead_score"] = score
    updated["stage"] = stage
    updated["missing_fields"] = ",".join(missing)
    updated["latest_update_source"] = "WhatsApp"
    updated["next_action"] = "Collect Documents"

    sync(updated, "WhatsApp", message)

    print("\n===== FINAL OUTPUT =====\n")

    print("Lead Score:", score)
    print("Stage:", stage)
    print("Missing Fields:", missing)
    print("Preferred Channel:", updated["preferred_channel"])
    print("Latest Source:", "WhatsApp")
    print("Extracted Info:", new)
    print("Next Action:", updated["next_action"])

    print("\nWhatsApp Draft:\n", whatsapp)
    print("\nEmail Draft:\n", email)
    print("\nCallback:\n", callback)


if __name__ == "__main__":
    simulate()