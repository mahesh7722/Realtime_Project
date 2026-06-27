def validate_result(expected_result, context):
    """
    AI-style validation explanation:
    Instead of hardcoding only DOM checks,
    we validate by reasoning:
    - Success → URL contains inventory.html
    - Failure → Error message visible
    """
    if expected_result == "success":
        assert "inventory.html" in context.page.url, "AI validation: Expected inventory page"
    elif expected_result == "failure":
        assert context.page.is_visible("h3[data-test='error']"), "AI validation: Expected error message"
