import re
from playwright.sync_api import Page, expect
import time


def test_run(page: Page) -> None:
    # Навигация и авторизация
    page.goto("http://erp-new.karman24.ru/login")
    page.get_by_role("textbox", name="Email").fill("Stasss_1985@mail.ru")
    page.get_by_role("textbox", name="Пароль").fill("Stasss_1985@mail.ru")
    page.get_by_role("button", name="Войти").click()

    # Проверка успешной авторизации
    expect(page.get_by_role("button", name="S Stas Krivko Stasss_1985@")).to_be_visible()

    # Проверка что мы на главной после логина
    expect(page).to_have_url(re.compile(r".*/dashboard"))

    # Клики по разделам с проверками URL
    sections = [
        ("📄 Сделки", r".*/contracts"),
        ("👥 Клиенты", r".*/customers"),
        ("📦 Товары", r".*/inventory"),
        ("📊 Бухгалтерия", r".*/accounting"),
        ("📈 Отчеты", r".*/reports"),
        ("🏛️ ГИИС ДМДК", r".*/giis"),
        ("🏢 Моя организация", r".*/my-organization"),
        ("📚 База знаний", r".*/knowledge-base"),
        ("🛠️ Тех.поддержка", r".*/support"),
        ("⚙️ Настройки", r".*/settings")
    ]

    for name, url_pattern in sections:
        page.get_by_role("link", name=name).click()
        expect(page).to_have_url(re.compile(url_pattern), timeout=10000)


def test_prosto(page: Page):
    page.goto("http://erp-new.karman24.ru/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("Stasss_1985@mail.ru")
    page.get_by_role("textbox", name="Пароль").click()
    page.get_by_role("textbox", name="Пароль").fill("Stasss_1985@mail.ru")
    page.get_by_role("button", name="Войти").click()
    page.get_by_role("link", name="👥 Клиенты").click()
    page.get_by_role("button", name="Добавить клиента").click()
    page.get_by_role("button", name="Добавить контакт").click()
    page.get_by_role("textbox", name="Значение").fill("+7 (939) 222-22-22")
    time.sleep(3)
    page.get_by_role("button", name="Готово").click()
