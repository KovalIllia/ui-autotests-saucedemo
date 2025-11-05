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


# @pytest.fixture(scope="function")
# def driver():
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--window-size=1920,1080")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-software-rasterizer")
#     options.binary_location = "/usr/bin/google-chrome"
#
#     service = Service(executable_path=ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.implicitly_wait(40)
#     yield driver
#     driver.quit()
