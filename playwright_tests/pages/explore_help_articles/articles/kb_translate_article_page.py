from playwright_tests.core.basepage import BasePage
from playwright.sync_api import Page, Locator


class TranslateArticlePage(BasePage):
    __translating_an_unready_article_banner = "//ul[@class='user-messages']/li"
    __list_romanian_locale = "//li/a[normalize-space(text())='română (ro)']"
    __article_translation_page_title = "//h1[@class='sumo-page-heading']"
    __translation_title_field = "//input[@id='id_title']"
    __translation_slug_field = "//input[@id='id_slug']"
    __allow_article_comments_label = "//label[@for='id_allow_discussion']"
    __translation_keyword_field = "//input[@id='id_keywords']"
    __translation_summary_field = "//textarea[@id='id_summary']"
    __translation_english_readonly_field = "//div[@id='content-or-diff']/textarea"
    __translation_ro_text = "//textarea[@id='id_content']"
    __change_body_view = "//a[text()='Comută evidențierea sintaxei']"
    __send_translation_for_approval_button = "//button[text()='Trimite pentru aprobare']"
    __save_translation_as_draft_button = "//button[text()='Salvează ca ciornă']"
    __draft_saved_successfully_message = "//div[@id='draft-message']"
    __translation_changes_description_input_field = "//input[@id='id_comment']"
    __translation_changes_description_submit_button = "//button[@id='submit-document-form']"

    def __init__(self, page: Page):
        super().__init__(page)

    def _click_on_romanian_locale_from_list(self):
        super()._click(self.__list_romanian_locale)

    def _get_text_of_article_unready_for_translation_banner(self) -> str:
        return super()._get_text_of_element(self.__translating_an_unready_article_banner)

    def _get_unready_for_translation_banner(self) -> Locator:
        return super()._get_element_locator(self.__translating_an_unready_article_banner)

    def _get_translate_page_title(self) -> str:
        return super()._get_text_of_element(self.__article_translation_page_title)

    def _fill_translation_title_field(self, text: str):
        super()._fill(self.__translation_title_field, text)

    def _fill_translation_slug_field(self, text: str):
        super()._fill(self.__translation_slug_field, text)

    def _click_on_allow_translated_article_comments_checkbox(self):
        super()._click(self.__allow_article_comments_label)

    def _fill_translated_article_keyword(self, text: str):
        super()._fill(self.__translation_keyword_field, text)

    def _fill_translated_article_summary(self, text: str):
        super()._fill(self.__translation_summary_field, text)

    def _get_text_of_english_version(self) -> str:
        return super()._get_text_of_element(self.__translation_english_readonly_field)

    def _fill_body_translation_field(self, text: str):
        super()._click(self.__change_body_view)
        super()._clear_field(self.__translation_ro_text)
        super()._fill(self.__translation_ro_text, text)

    def _click_on_submit_translation_for_approval_button(self):
        super()._get_element_locator(self.__send_translation_for_approval_button).first.click()

    def _fill_translation_changes_description_field(self, text: str):
        super()._fill(self.__translation_changes_description_input_field, text)

    def _click_on_description_submit_button(self):
        super()._click(self.__translation_changes_description_submit_button)

    def _click_on_save_translation_as_draft_button(self):
        super()._get_element_locator(self.__save_translation_as_draft_button).first.click()

    def _get_draft_success_message_locator(self) -> Locator:
        return super()._get_element_locator(self.__draft_saved_successfully_message)
