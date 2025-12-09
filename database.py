import os
import uuid
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def insert_event(event_data):
    # Add a unique ID if not present
    if 'id' not in event_data or event_data['id'] is None:
        event_data['id'] = str(uuid.uuid4())
    
    supabase.table("Events").insert(event_data).execute()