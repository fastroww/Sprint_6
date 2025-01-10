import pytest
from src.data.order import ORDER_DATA_LIST
import allure

@allure.feature("Оформление заказа")
@allure.story("Позитивный сценарий оформления заказа")
@pytest.mark.parametrize("test_data", ORDER_DATA_LIST)
def test_order_positive_flow(order_page, test_data):

    with allure.step("Принимаем куки"):
        order_page.accept_cookie()

    with allure.step(f"1. Заполнить первую часть формы с данными: {test_data.name}, {test_data.surname}"):
        order_page.fill_personal_data(
            test_data.name,
            test_data.surname,
            test_data.address,
            test_data.metro,
            test_data.phone
        )
        order_page.click_next_button()

    with allure.step(f"2. Заполнить вторую часть формы с датой: {test_data.date}, длительность: {test_data.duration_text}"):
        order_page.fill_rent_data(
            test_data.date,
            test_data.duration_text,
            test_data.color_black,
            test_data.color_grey,
            test_data.comment
        )
        order_page.click_order_button()

    with allure.step("3. Подтвердить заказ в модальном окне"):
       order_page.confirm_order_modal()

    with allure.step("4. Проверить, что заказ оформлен"):
        success_text = order_page.get_success_message()
        assert "Заказ оформлен" in success_text, (
            f"Не найдено подтверждение заказа. Текст: {success_text}"
        )

