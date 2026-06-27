from playwright.sync_api import sync_playwright

def before_all(context):
    # Start Playwright and attach to context
    context.playwright = sync_playwright().start()

    # Launch browser instance
    context.browser = context.playwright.chromium.launch(headless=False)

    # Create a new browser context (important for isolation)
    context.browser_context = context.browser.new_context()

    # Create a new page and attach to Behave context
    context.page = context.browser_context.new_page()

def after_all(context):
    # Close browser context and browser
    context.browser_context.close()
    context.browser.close()

    # Stop Playwright
    context.playwright.stop()
