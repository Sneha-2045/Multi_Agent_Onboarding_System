import pandas as pd
from database.db import insert_lead

def ingest_csv(file):

    df = pd.read_csv(file)

    for _, row in df.iterrows():

        lead = row.to_dict()

        lead["lead_score"] = 0
        lead["stage"] = "New"
        lead["missing_fields"] = ""
        lead["latest_update_source"] = "CSV"
        lead["next_action"] = "Initial Contact"

        insert_lead(lead)

    print("Leads Inserted")