import pytest


@pytest.mark.usefixtures("init_driver")
class Test_Base:
    pass

class Test_Google(Test_Base):
    def test_google_title(self):
        self.driver.get("https://www.google.co.uk")
        assert self.driver.title == "Google"

