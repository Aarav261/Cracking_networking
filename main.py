def main():
    from scraper import extract_meetup_links, extract_meetup_events
    from database import insert_event

    links = extract_meetup_links()
    events = extract_meetup_events(links)

    for event in events:
        insert_event(event)

if __name__ == "__main__":
    
    main()