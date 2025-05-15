from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import aiohttp
import os

API_ROOT = "https://api.openbrewerydb.org/v1/breweries"

app = FastAPI(title="Brewery Finder")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Server-side render the empty search page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api/breweries", response_class=JSONResponse)
async def breweries(city: str | None = None,
                    state: str | None = None,
                    brewery_type: str | None = None,
                    per_page: int = 20):
    """Proxy to OpenBreweryDB and return filtered list."""
    params = {"per_page": per_page}
    if city:
        params["by_city"] = city
    if state:
        params["by_state"] = state
    if brewery_type:
        params["by_type"] = brewery_type

    async with aiohttp.ClientSession() as session:
        async with session.get(API_ROOT, params=params) as resp:
            if resp.status != 200:
                raise HTTPException(resp.status, "Upstream error")
            data = await resp.json()
    return data
