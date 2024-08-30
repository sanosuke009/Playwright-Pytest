"This module contains the page object class of the referral launch page"

from web.src.test.baseClass.baseclass import baseclass


class jobsearchresultpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    id_iframe = "icims_content_iframe"
    xpath_input_searchbar = "//input[@id='jsb_f_keywords_i']"
    xpath_button_search = "//input[@id='jsb_form_submit_i']"
    xpath_div_errormessage = "//div[@class='iCIMS_Message iCIMS_ErrorMessage iCIMS_GenericMessage']"
    xpath_div_jobtable = "//div[@class='container-fluid iCIMS_JobsTable']"
    xpath_header_jobrow = xpath_div_jobtable+"/descendant::h3"

    # Page object methods/functions

        
    def verifyresult(self, jobid):
        try:
            self.page.wait_for_load_state(state='networkidle')
            iframe = self.page.frame_locator("#"+self.id_iframe)
            errormsg = iframe.locator(selector_or_locator="xpath="+self.xpath_div_errormessage)
            joblink = iframe.locator(selector_or_locator="xpath="+self.xpath_header_jobrow)
            #joblink.wait_for(state='visible')
            if joblink.is_visible():
                self.rm.addscreenshot("Result for job id "+jobid+" is displayed")
                joblink.click()
                self.rm.addscreenshot("Clicked on "+jobid)
            elif errormsg.is_visible():
                self.rm.addscreenshot("Result for job id "+jobid+" is NOT displayed.")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during displaying search result for job id = "+jobid)
            print(e)
            return False
        else:
            return True
        


        

