"This module contains the page object class of the referral launch page"

from web.src.test.baseClass.baseclass import baseclass


class ref_launchpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    id_iframe = "icims_content_iframe"
    xpath_input_searchbar = "//input[@id='jsb_f_keywords_i']"
    xpath_button_search = "//input[@id='jsb_form_submit_i']"

    # Page object methods/functions
    
    def verifylaunchpage(self):
        try:
            searchbar = self.page.frame_locator("#"+self.id_iframe).locator(selector_or_locator="xpath="+self.xpath_input_searchbar)
            searchbar.wait_for(state='visible')
            if searchbar.is_visible():
                self.rm.addscreenshot("The launchpage is displayed as expected.")
            else:
                self.rm.addscreenshot("The launchpage is NOT displayed.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during verification of launchpage")
            print(e)
            return False
        else:
            return True
        
    def searchforjobid(self, jobid):
        try:
            iframe = self.page.frame_locator("#"+self.id_iframe)
            searchbar = iframe.locator(selector_or_locator="xpath="+self.xpath_input_searchbar)
            searchbutton = iframe.locator(selector_or_locator="xpath="+self.xpath_button_search)
            searchbar.clear()
            searchbar.fill(jobid)
            self.rm.addscreenshot("The searchbar is filled with jobid = "+jobid)
            searchbutton.click()
            self.rm.addscreenshot("The search button is clicked")
        except Exception as e:
            self.rm.addscreenshot("Error occurred during search for job id = "+jobid)
            print(e)
            return False
        else:
            return True
        

