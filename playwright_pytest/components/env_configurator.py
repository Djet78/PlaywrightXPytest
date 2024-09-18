from playwright_pytest.components.utils import singleton


@singleton
class EnvConfigurator:
    def __init__(self, desired_env: str = 'dev'):
        self.env = desired_env.lower()
        self.booking_endp = 'https://restful-booker.herokuapp.com/'
