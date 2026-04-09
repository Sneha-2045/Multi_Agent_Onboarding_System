
def generate_response(lead, missing):

    if missing:
        msg = f"Hi {lead['name']}, please share {', '.join(missing)}"
    else:
        msg = "You're ready for onboarding"

    email = f"Dear {lead['name']},\n{msg}"

    return msg, email


def generate_callback(lead):

    return f"""
Callback Required

Lead: {lead['name']}

Missing:
{lead.get('missing_fields')}

Priority:
Medium
"""