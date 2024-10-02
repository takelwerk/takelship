def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "forgejo: mark test to run only on forgejo environment")
