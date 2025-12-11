from Event_scraper import extract_meetup_links, extract_meetup_events
from database import insert_event, insert_internship
from internship_scraper import extract_internship_links
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import json
from gmail import send_email


load_dotenv()

def main():
    URL_OF_INTERNSHIP_LISTING_PAGE = "https://au.gradconnection.com/internships/engineering-software/melbourne/"
    URL_OF_MEETUP_LISTING_PAGE = "https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury&source=EVENTS&distance=tenMiles"
    
    internship_links = extract_internship_links(URL_OF_INTERNSHIP_LISTING_PAGE)
    LIMIT_LINKS = 2
    
    links = extract_meetup_links(URL_OF_MEETUP_LISTING_PAGE)
    events = extract_meetup_events(links, Limit_links=LIMIT_LINKS)

    for event in events:
        insert_event(event)

    for internship in internship_links[:LIMIT_LINKS]:
        insert_internship(internship)

    client = genai.Client(api_key=os.getenv("GEMINI_API"))

    # Convert data to JSON string
    content = f"""
Here are the events and internships to summarize:

Events:
{json.dumps(events[:LIMIT_LINKS], indent=2)}

Internships:
{json.dumps(internship_links[:LIMIT_LINKS], indent=2)}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=content,  # Pass as string, not tuple
        config=types.GenerateContentConfig(
            system_instruction="You are a newsletter generator. Use the content to generate a summary of the events and internships with links in a friendly manner. Don't use hashtags "
        )
    )

    print(response.text)
    send_email("Newsletter Summary", response.text, os.getenv("GMAIL_USER"), os.getenv("GMAIL_USER"), os.getenv("GMAIL_PASSWORD"))

if __name__ == "__main__":
    main()