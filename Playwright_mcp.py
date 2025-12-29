import os 
from pathlib import Path
import asyncio
import base64
from playwright.async_api import async_playwright, Page, Browser
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("playwright-automation")

# Global variables to hold browser and page instances
async def _ensure_browswer():
    """
   Ensure browser and page are initialized. 
    """
    global browser, playwright_instance, page

    if browser is None or page is None:
        playwright_instance = await async_playwright().start()
        browser = await playwright_instance.chromium.launch(headless=False)
        page = await browser.new_page()

@mcp.tool()
async def navigate(url: str) -> str:
    """Navigate to a specified URL."""
    try:
        await _ensure_browswer()
        await page.goto(url, wait_until="documentloaded")
        title = await page.title()
        return f"Navigated to {url} with title: {title}"
    except Exception as e:
        return f"Error navigating to {url}: {e}"
    

@mcp.tool()
async def click(selector: str) -> str:
    """Click on an element matching the given selector."""
    try:
        await _ensure_browswer()
        await page.click(selector)
        return f"Clicked on element with selector: {selector}"
    except Exception as e:
        return f"Error clicking on element with selector {selector}: {e}"
    



if __name__ == "__main__":
    try:
        mcp.run()
    finally:
        if browser:
            asyncio.run(browser.close())
        if playwright_instance:
            asyncio.run(playwright_instance.stop())# Global browser and page instances