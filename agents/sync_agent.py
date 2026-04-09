from database.db import update_lead, log_activity

def sync(lead, channel, message):

    update_lead(lead)

    log_activity(
        lead["lead_id"],
        channel,
        message
    )