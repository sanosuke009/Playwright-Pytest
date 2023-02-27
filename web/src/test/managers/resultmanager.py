"This class controls the allure report or any other report generation"


from allure_commons.types import AttachmentType
import allure
from playwright.sync_api import Page


class resultmanager:

    def __init__(self, page : Page):
        self.page = page

    def addscreenshot(self, message):
        allure.attach(self.page.screenshot(), name=message, attachment_type=AttachmentType.PNG)
    