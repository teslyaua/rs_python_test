import logging
from pathlib import Path

import allure
import pytest
from slugify import slugify

from pages.app import Application

logger = logging.getLogger()


@pytest.fixture
def app(page):
    return Application(page)


# This is hook for base playwright browser_context configuration.
# More details: https://playwright.dev/python/docs/api/class-browser/#browsernew_contextkwargs
@pytest.fixture
def browser_context_args(browser_context_args, base_url):
    logger.info('BASE URL: ' + base_url)
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "accept_downloads": True,
        "record_video_dir": "playwright-video",
        "record_video_size": {
            "width": 1920,
            "height": 1080,
        }
    }


# This is hook for Screenshot on test failure. slugify to convert test names to file paths.
# More details: https://playwright.dev/python/docs/test-runners/
def pytest_runtest_makereport(item, call) -> None:
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path("playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            page.screenshot(path=str(screenshot_dir / f"{slugify(item.nodeid)}.png"))
            allure.attach.file(str(screenshot_dir / f"{slugify(item.nodeid)}.png"),
                               attachment_type=allure.attachment_type.PNG)
