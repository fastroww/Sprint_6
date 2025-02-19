from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор для cookie

    # Локаторы для вопросов
    QUESTION_1 = (By.ID, 'accordion__heading-0')
    QUESTION_2 = (By.ID, 'accordion__heading-1')
    QUESTION_3 = (By.ID, 'accordion__heading-2')
    QUESTION_4 = (By.ID, 'accordion__heading-3')
    QUESTION_5 = (By.ID, 'accordion__heading-4')
    QUESTION_6 = (By.ID, 'accordion__heading-5')
    QUESTION_7 = (By.ID, 'accordion__heading-6')
    QUESTION_8 = (By.ID, 'accordion__heading-7')

    # Локаторы для ответов
    ANSWER_1 = (By.ID, 'accordion__panel-0')
    ANSWER_2 = (By.ID, 'accordion__panel-1')
    ANSWER_3 = (By.ID, 'accordion__panel-2')
    ANSWER_4 = (By.ID, 'accordion__panel-3')
    ANSWER_5 = (By.ID, 'accordion__panel-4')
    ANSWER_6 = (By.ID, 'accordion__panel-5')
    ANSWER_7 = (By.ID, 'accordion__panel-6')
    ANSWER_8 = (By.ID, 'accordion__panel-7')

    # Локаторы для кнопок заказа
    UPPER_ORDER_BUTTON = (By.CSS_SELECTOR, "button[class*='Button_Button__ra12g']")
    LOWER_ORDER_BUTTON = (By.CSS_SELECTOR, "div[class*='Home_FinishButton__1_cWm'] button")
