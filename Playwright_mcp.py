import os 
from pathlib import Path
import asyncio
import base64
from playwright.async_api import async_playwright, Page, Browser
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("playwright-automation")

browser = None
page = None
playwright_instance = None

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
        await page.goto(url, wait_until="domcontentloaded")
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
    

@mcp.tool()
async def fill(selector: str, value: str) -> str:
    """Fill an input element with the given value."""
    try:
        await _ensure_browswer()
        await page.fill(selector, value)
        return f"Filled element with selector: {selector} with value: {value}"
    except Exception as e:
        return f"Error filling element with selector {selector}: {e}"
    
# Capture screenshot
@mcp.tool()
async def screenshot(selector: str = None) -> str:
    """Capture a screenshot of the page or a specific element."""
    try:
        await _ensure_browswer()
        if selector:
            element = await page.query_selector(selector)
            if not element:
                return f"Error: No element found for selector {selector}"
            screenshot_bytes = await element.screenshot()
        else:
            screenshot_bytes = await page.screenshot()
        
        screenshot_b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
        return screenshot_b64
    except Exception as e:
        return f"Error capturing screenshot: {e}"
    
# Get page content
@mcp.tool()
async def get_content() -> str: 
    """Get the HTML content of the current page."""
    try:
        await _ensure_browswer()
        content = await page.content()
        return content
    except Exception as e:
        return f"Error getting page content: {e}"
    
    #to close browser
@mcp.tool()
async def close_browser() -> str:
    """Close the browser instance."""
    global browser, playwright_instance, page
    try:
        if browser:
            await browser.close()
            browser = None
            page = None
        if playwright_instance:
            await playwright_instance.stop()
            playwright_instance = None
        return "Browser closed successfully."
    except Exception as e:
        return f"Error closing browser: {e}"
    
##todo 
# Add more playwright functions as needed
# popup handling
# file download/upload
# form submission
# mouse and keyboard actions


if __name__ == "__main__":
    try:
        mcp.run()
    finally:
        if browser:
            asyncio.run(browser.close())
        if playwright_instance:
            asyncio.run(playwright_instance.stop())# Global browser and page instances