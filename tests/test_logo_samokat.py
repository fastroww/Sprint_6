import constants
import allure


@allure.title("Клик по логотипу 'Самокат' переходит на главную страницу сервиса")
def test_scooter_logo_goes_to_main(order_page):

    with allure.step("Кликаем на логотип Самоката"):
        order_page.click_scooter_logo()

    with allure.step("Проверяем, что текущая страница является главной страницей сервиса"):
        assert constants.BASE_URL in order_page.current_url
