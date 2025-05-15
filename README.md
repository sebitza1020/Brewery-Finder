# Brewery Finder

A minimal FastAPI web app that lets you search the free Open Brewery DB for breweries by city, state, or brewery type and shows the results in a simple HTML table.

## Features

* Search Open Brewery DB without an API key

* Filter by city, state, or brewery type

* FastAPI proxy keeps your API key‑free front‑end decoupled and ready for caching, auth, or rate‑limiting later

* Tiny footprint with just one Python file and a handful of static assets

## Tech Stack

* FastAPI + Uvicorn – backend and proxy

* Jinja2 – HTML templating

* aiohttp – async HTTP client

* Vanilla JS + Fetch API – front‑end calls

* Plain CSS – zero‑dependency styling

## Project Structure
```
├── app.py               # FastAPI application
├── requirements.txt
├── templates/
│   └── index.html       # Jinja2 template
└── static/
    ├── css/styles.css
    └── js/main.js
```
## Installation
```
#Clone the repo
$ git clone https://github.com/your-username/brewery-finder.git
$ cd brewery-finder

# Create and activate virtual environment
$ python -m venv venv
$ source venv/bin/activate    # Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Run the development server
$ uvicorn app:app --reload
```

Open http://localhost:8000 in your browser.

## Environment Variables

None required — the Open Brewery DB is public.
(Optional) Set PORT if your hosting platform provides one.

## Usage

1. Fill in any combination of City, State, and/or Type.

2. Click Search.

3. Results appear instantly in the table; each row links to the brewery’s website when available.

## API Notes

The backend forwards queries to:

`GET https://api.openbrewerydb.org/v1/breweries`

| Query Param |       Example       |      Description     |
|-------------|---------------------|----------------------|
| `by_city`   | `by_city=denver`    | Filter by city name  |
| `by_state`  | `by_state=colorado` | Filter by U.S. state |
| `by_type`   | `by_type=micro`     | Brewery category     |
| `per_page`  | `per_page=20`       | Results per page     |

See the Open Brewery DB docs for more details.
