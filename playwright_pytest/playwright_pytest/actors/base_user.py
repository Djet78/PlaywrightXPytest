from typing import Self


class BaseUser:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_main_page(self) -> Self:
        self.driver.get('https://www.youtube.com/')
        return self


class UnassignedUser(BaseUser):
    pass
