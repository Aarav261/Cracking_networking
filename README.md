# Cracked_networking

An automated web scraper that extracts tech events and internships from Meetup and GradConnection, then stores them in a Supabase database using Playwright and AgentQL.

## Features

- 🔍 **Event Scraping**: Extracts tech events from Meetup.com in the Canterbury, Australia area
- 💼 **Internship Scraping**: Extracts engineering/software internships from GradConnection Melbourne
- 🤖 **AI-Powered Extraction**: Uses AgentQL for intelligent element detection
- 💾 **Database Storage**: Automatically stores scraped data in Supabase
- 🌐 **Browser Automation**: Powered by Playwright for reliable web scraping

## Prerequisites

- Python 3.13+
- AgentQL API key ([sign up here](https://dev.agentql.com))
- Supabase account and project

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Aarav261/Cracking_networking.git
cd advanced_scraper
```

2. **Create and activate virtual environment**
```bash
python -m venv advanced_scaper
source advanced_scaper/bin/activate  # On macOS/Linux
```

3. **Install dependencies**
```bash
pip install playwright agentql supabase python-dotenv
playwright install chromium
```

4. **Set up AgentQL**
```bash
agentql init
```

5. **Configure environment variables**

Create a `.env` file in the project root:
```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

6. **Set up Supabase Database**

Create an `Events` table in your Supabase project with the following schema:
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

## Usage

Run the main scraper:
```bash
python main.py
```

This will:
1. Extract tech event links from Meetup.com
2. Visit each event page and extract detailed information
3. Store the events in your Supabase database with auto-incrementing IDs

### Individual Scrapers

**Extract Meetup events only:**
```python
from scraper import extract_meetup_links, extract_meetup_events

links = extract_meetup_links()
events = extract_meetup_events(links)
```

**Extract internship links only:**
```python
from internship_scraper import extract_internship_links

internship_links = extract_internship_links()
```

## Project Structure

```
advanced_scraper/
├── main.py                  # Main entry point
├── scraper.py              # Meetup event scraper
├── internship_scraper.py   # GradConnection internship scraper
├── database.py             # Supabase database operations
├── .env                    # Environment variables (not in repo)
└── advanced_scaper/        # Virtual environment
```

## Configuration

### Adjust Event Limit
In `scraper.py`, modify the `Limit_links` variable to control how many events to scrape:
```python
Limit_links = 2  # Change to desired number
```

### Change Search Parameters
Modify the URLs in the scraper files to customize your search:

**Meetup (scraper.py):**
```python
agentql_page.goto("https://www.meetup.com/en-AU/find/?keywords=tech&location=au--Canterbury&source=EVENTS&distance=tenMiles")
```

**GradConnection (internship_scraper.py):**
```python
agentql_page.goto("https://au.gradconnection.com/internships/engineering-software/melbourne/")
```

## Technologies Used

- **[Playwright](https://playwright.dev/python/)**: Browser automation
- **[AgentQL](https://docs.agentql.com/)**: AI-powered web element detection
- **[Supabase](https://supabase.com/)**: PostgreSQL database and backend
- **[Python-dotenv](https://pypi.org/project/python-dotenv/)**: Environment variable management

## Troubleshooting

**Import errors:**
```bash
# Clear Python cache
rm -rf __pycache__
```

**AgentQL API errors:**
```bash
# Reinitialize AgentQL
agentql init
```

**Playwright browser errors:**
```bash
# Reinstall browsers
playwright install --with-deps chromium
```

## License

This project is part of the Cracking_networking repository.

## Contributing

Feel free to submit issues or pull requests to improve the scraper functionality.
