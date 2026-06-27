def test_sauce_01(page):
    page.goto("https://www.saucedemo.com")
    assert "Swag Labs" in page.title()
