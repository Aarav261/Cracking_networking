# Cracked_networking

An automated web scraper that extracts tech events and internships from Meetup and GradConnection, stores them in a Supabase database, and sends AI-generated newsletter summaries via email using Playwright, AgentQL, and Google Gemini AI.

## Features

- 🔍 **Event Scraping**: Extracts tech events from Meetup.com in the Canterbury, Australia area
- 💼 **Internship Scraping**: Extracts engineering/software internships from GradConnection Melbourne
- 🤖 **AI-Powered Extraction**: Uses AgentQL for intelligent element detection
- 💾 **Database Storage**: Automatically stores scraped data in Supabase with auto-incrementing IDs
- 🌐 **Browser Automation**: Powered by Playwright for reliable web scraping
- 📧 **Email Newsletters**: Generates AI-powered summaries using Google Gemini and sends via Gmail
- ✨ **Smart Summarization**: Converts scraped data into friendly newsletter format with links

## Prerequisites

- Python 3.13+
- AgentQL API key ([sign up here](https://dev.agentql.com))
- Supabase account and project
- Google Gemini API key ([get it here](https://ai.google.dev))
- Gmail account with App Password enabled

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aarav261/Cracking_networking.git
cd advanced_scraper
```

2. **Create and activate virtual environment**
```bash
python -m venv advanced_scraper
source advanced_scraper/bin/activate  # On macOS/Linux
# advanced_scraper\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install playwright agentql supabase python-dotenv google-generativeai
playwright install chromium
```

4. **Set up AgentQL**
```bash
agentql init
```

5. **Configure environment variables**

Create a `.env` file in the project root:
```env
AGENT_API_KEY=your_agentql_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_gmail_app_password
GEMINI_API=your_gemini_api_key
```

**Setting up Gmail App Password:**
1. Enable 2-Factor Authentication on your Google account
2. Go to Google Account > Security > 2-Step Verification > App passwords
3. Generate a new app password for "Mail"
4. Use this 16-character password in your `.env` file

6. **Set up Supabase Database**

Create two tables in your Supabase project:

**Events table:**
```sql
CREATE TABLE "Events" (
    id bigserial PRIMARY KEY,
    title text,
    link text,
    date text,
    description text,
    location text
);
```

**Internships table:**
```sql
CREATE TABLE "Internships" (
    id bigserial PRIMARY KEY,
    name text,
    link text,
    company text,
    location text
);
```

## Usage

### Run the complete pipeline:
```bash
python main.py
```

This will:
1. Extract tech event links from Meetup.com
2. Visit each event page and extract detailed information
3. Extract internship listings from GradConnection
4. Store all data in Supabase database
5. Generate an AI-powered newsletter summary using Google Gemini
6. Send the newsletter to the configured email address

### Individual Module Usage

**Extract events:**
```python
from Event_scraper import extract_meetup_links, extract_meetup_events

url = "https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury"
links = extract_meetup_links(url)
events = extract_meetup_events(links, Limit_links=5)
```

**Extract internships:**
```python
from internship_scraper import extract_internship_links

url = "https://au.gradconnection.com/internships/engineering-software/melbourne/"
internships = extract_internship_links(url)
```

**Store data in database:**
```python
from database import insert_event, insert_internship

insert_event({"title": "Tech Meetup", "link": "...", "date": "..."})
insert_internship({"name": "Software Intern", "company": "...", "location": "..."})
```

**Send email:**
```python
from gmail import send_email

send_email(
    subject="Weekly Newsletter",
    body="Your newsletter content here",
    to_email="recipient@example.com",
    email=os.getenv("GMAIL_USER"),
    password=os.getenv("GMAIL_PASSWORD")
)
```

## Project Structure

```
advanced_scraper/
├── main.py                  # Main orchestration script
├── Event_scraper.py         # Meetup event scraper with AgentQL
├── internship_scraper.py    # GradConnection internship scraper
├── database.py              # Supabase database operations
├── gmail.py                 # Email sending functionality
├── lit_test.py              # Streamlit test file
├── .env                     # Environment variables (not in repo)
├── README.md                # This file
└── advanced_scraper/        # Virtual environment
```

## Configuration

### Adjust Scraping Limits
In [`main.py`](main.py), modify the `LIMIT_LINKS` variable:
```python
LIMIT_LINKS = 2  # Change to desired number of items to scrape
```

### Change Search Parameters

**Meetup events** ([`main.py`](main.py)):
```python
URL_OF_MEETUP_LISTING_PAGE = "https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury&source=EVENTS&distance=tenMiles"
```

**Internships** ([`main.py`](main.py)):
```python
URL_OF_INTERNSHIP_LISTING_PAGE = "https://au.gradconnection.com/internships/engineering-software/melbourne/"
```

### Customize Newsletter Generation

Modify the system instruction in [`main.py`](main.py):
```python
config=types.GenerateContentConfig(
    system_instruction="Your custom instructions here"
)
```

## Module Descriptions

### Event_scraper.py
Uses AgentQL queries to extract event data from Meetup:
- [`extract_meetup_links()`](Event_scraper.py): Gets event URLs from listing page
- [`extract_meetup_events()`](Event_scraper.py): Extracts detailed info (title, date, description, location) from each event

### internship_scraper.py
Extracts internship listings with:
- [`extract_internship_links()`](internship_scraper.py): Scrapes internship name, link, company, and location

### database.py
Manages Supabase operations:
- [`insert_event()`](database.py): Inserts events with auto-incrementing IDs
- [`insert_internship()`](database.py): Inserts internships with auto-incrementing IDs

### gmail.py
Handles email delivery:
- [`send_email()`](gmail.py): Sends plain text emails via Gmail SMTP

### main.py
Orchestrates the entire workflow:
1. Scrapes events and internships
2. Stores data in Supabase
3. Generates AI summary with Google Gemini
4. Emails newsletter to recipient

## Technologies Used

- **[Playwright](https://playwright.dev/python/)**: Browser automation and web scraping
- **[AgentQL](https://docs.agentql.com/)**: AI-powered web element detection and querying
- **[Supabase](https://supabase.com/)**: PostgreSQL database and backend services
- **[Google Gemini AI](https://ai.google.dev)**: AI-powered newsletter generation
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Environment variable management
- **[smtplib](https://docs.python.org/3/library/smtplib.html)**: Email sending via Gmail

## Troubleshooting

**Import errors:**
```bash
rm -rf __pycache__
rm -rf .pytest_cache
```

**AgentQL API errors:**
```bash
agentql init
```

**Playwright browser errors:**
```bash
playwright install --with-deps chromium
```

**Gmail authentication errors:**
- Ensure 2-Factor Authentication is enabled
- Use App Password, not your regular Gmail password
- Check that "Less secure app access" is not blocking the connection

**Gemini API errors:**
- Verify your API key is valid and has credits
- Check the API quota limits

**Database insertion errors:**
- Verify Supabase URL and key are correct
- Check that tables exist with correct schema
- Ensure network connectivity to Supabase

## Future Enhancements

- [ ] Add HTML email templates
- [ ] Support multiple newsletter recipients
- [ ] Add scheduling/cron job support
- [ ] Implement error handling and retry logic
- [ ] Add unit tests
- [ ] Create web dashboard with Streamlit
- [ ] Add more event and job board sources

## License

This project is part of the Cracking_networking repository.

## Contributing

Feel free to submit issues or pull requests to improve the scraper functionality.

## Author

Built with ❤️ for automating networking opportunities