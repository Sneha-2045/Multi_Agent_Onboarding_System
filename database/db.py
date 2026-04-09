import sqlite3

conn = sqlite3.connect("leads.db", check_same_thread=False)
cursor = conn.cursor()

# Leads Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS leads (
lead_id INTEGER PRIMARY KEY,
name TEXT,
phone TEXT,
email TEXT,
city TEXT,
vehicle_type TEXT,
vehicle_count INTEGER,
aadhaar_status TEXT,
bank_status TEXT,
rc_status TEXT,
app_installed TEXT,
preferred_channel TEXT,
remarks TEXT,
lead_score INTEGER,
stage TEXT,
missing_fields TEXT,
latest_update_source TEXT,
next_action TEXT
)
''')

# Activity Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS activity (
id INTEGER PRIMARY KEY AUTOINCREMENT,
lead_id INTEGER,
channel TEXT,
message TEXT,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()


def insert_lead(lead):
    cursor.execute('''
    INSERT OR REPLACE INTO leads VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''',(
    lead.get("lead_id"),
    lead.get("name"),
    lead.get("phone"),
    lead.get("email"),
    lead.get("city"),
    lead.get("vehicle_type"),
    lead.get("vehicle_count"),
    lead.get("aadhaar_status"),
    lead.get("bank_status"),
    lead.get("rc_status"),
    lead.get("app_installed"),
    lead.get("preferred_channel"),
    lead.get("remarks"),
    lead.get("lead_score"),
    lead.get("stage"),
    lead.get("missing_fields"),
    lead.get("latest_update_source"),
    lead.get("next_action")
    ))

    conn.commit()


def get_lead(lead_id):

    cursor.execute("SELECT * FROM leads WHERE lead_id=?", (lead_id,))
    row = cursor.fetchone()

    if not row:
        return None

    columns = [column[0] for column in cursor.description]

    return dict(zip(columns, row))


def update_lead(lead):
    insert_lead(lead)


def log_activity(lead_id, channel, message):

    cursor.execute(
        "INSERT INTO activity (lead_id, channel, message) VALUES (?, ?, ?)",
        (lead_id, channel, message)
    )

    conn.commit()