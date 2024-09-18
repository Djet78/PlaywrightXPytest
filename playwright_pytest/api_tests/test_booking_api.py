import allure

from playwright.sync_api import APIRequestContext


@allure.feature('Booking API')
@allure.label('owner', 'Viacheslav')
@allure.tag('API')
class TestBookingAPI:
    @allure.title('GET bookings')
    @allure.description('Simple GET bookings without params')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_get_bookings_without_params(self, api_request: APIRequestContext) -> None:
        bookings = api_request.get('/booking')
        assert bookings.ok

        res: list[dict] = bookings.json()
        assert res, f'API sent empty response: {res}'

        assert isinstance(res[0]['bookingid'], int), f'Booking id should be an integer, got {type(res[0]["bookingid"])}'
