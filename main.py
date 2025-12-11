def main():
    from Event_scraper import extract_meetup_links, extract_meetup_events
    from database import insert_event , insert_internship
    from internship_scraper import extract_internship_links


    URL_OF_INTERNSHIP_LISTING_PAGE = "https://au.gradconnection.com/internships/engineering-software/melbourne/"

    URL_OF_MEETUP_LISTING_PAGE = "https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury&source=EVENTS&distance=tenMiles"
    internship_links = extract_internship_links(URL_OF_INTERNSHIP_LISTING_PAGE)

    LIMIT_LINKS = 5
    
    links = extract_meetup_links(URL_OF_MEETUP_LISTING_PAGE)
    events = extract_meetup_events(links, Limit_links=LIMIT_LINKS)

    for event in events:
        insert_event(event)

    for internship in internship_links[:LIMIT_LINKS]:
        insert_internship(internship)

        

if __name__ == "__main__":
    
    main()