import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def insert_event(event_data):
    # drop null/empty values
    clean = {k: v for k, v in event_data.items() if v not in (None, "", [], {})}

    # get next id
    resp = supabase.table("Events").select("id").order("id", desc=True).limit(1).execute()
    last_id = resp.data[0]["id"] if resp.data else 0
    clean["id"] = last_id + 1

    supabase.table("Events").insert(clean).execute()

def insert_internship(internship_data):
    # Get the current max ID and increment
    result = supabase.table("Internships").select("id").order("id", desc=True).limit(1).execute()
    
    if result.data and len(result.data) > 0:
        next_id = result.data[0]['id'] + 1
    else:
        next_id = 1
    
    # Filter out null values and assign id
    filtered_data = {k: v for k, v in internship_data.items() if v is not None and v != ""}
    filtered_data['id'] = next_id
    
    supabase.table("Internships").insert(filtered_data).execute()

def insert_email(email_data):
    # Get the current max ID and increment
    result = supabase.table("Outreach").select("id").order("id", desc=True).limit(1).execute()
    
    if result.data and len(result.data) > 0:
        next_id = result.data[0]['id'] + 1
    else:
        next_id = 1
    
    # Filter out null values and assign id
    filtered_data = {k: v for k, v in email_data.items() if v is not None and v != ""}
    filtered_data['id'] = next_id
    
    supabase.table("Outreach").insert(filtered_data).execute()