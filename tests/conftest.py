import pytest
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser: Browser = p.chromium.launch(
                headless=True,
                args=[
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--disable-software-rasterizer",
                    "--window-size=1920,1080",
                ],
            )
        context: BrowserContext = browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )

        page: Page = context.new_page()
        page.set_default_timeout(4000)
        page.set_default_navigation_timeout(4000)
        yield page
        context.close()
        browser.close()


