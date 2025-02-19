import allure
import constants


@allure.title("Клик по логотипу Яндекса открывает Дзен в той же вкладке")
def test_logo_yandex_in_same_tab(main_page):

    with allure.step("Кликаем на логотип Яндекса"):
        main_page.click_yandex_logo()

    with allure.step("Переключиться на вторую вкладку"):
        main_page.switch_to_second_tab()

    with allure.step("Проверяем, что произошёл редирект на Дзен"):
        main_page.wait_url_contains(constants.DZEN_URL)

        current_url = main_page.current_url
        assert constants.DZEN_URL in current_url, f"Ожидался переход на Дзен, а сейчас URL: {current_url}"

