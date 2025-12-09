from playwright.sync_api import sync_playwright
import agentql



QUERY = """
{
    events[]{
        name
        date
        location
        link}

}"""

QUERY_DETAILS = """{
        event_details[]{
        id
        title
        link
        date
        description
        location}
}"""

def extract_meetup_links():
    links= []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        agentql_page = agentql.wrap(page)
        agentql_page.goto("https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury&source=EVENTS&distance=tenMiles")
        response = agentql_page.query_data(QUERY, mode = 'fast')
        
        for link in response['events']:
            links.append(link['link'])

        browser.close()

    return links

Limit_links = 2
def extract_meetup_events(links):
    event_list = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        
        for link in links[:Limit_links]:
            page = browser.new_page()
            agentql_page = agentql.wrap(page)
            agentql_page.goto(link)
            response = agentql_page.query_data(QUERY_DETAILS)
            for event in response['event_details']:
                event_list.append(event)
            page.close()
        

        browser.close()

    return event_list

            
            
