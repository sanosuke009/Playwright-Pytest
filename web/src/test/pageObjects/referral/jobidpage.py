"This module contains the page object class of the referral launch page"

from web.src.test.baseClass.baseclass import baseclass


class jobidpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    id_iframe = "icims_content_iframe"
    xpath_span_jobid = lambda self, jobid: "//span[contains(text(),'"+jobid+"')]"
    xpath_header_title = "//h1[@class='iCIMS_Header']"
    xpath_span_referbutton = "//span[contains(text(),'Email this job to a friend')]"

    # Page object methods/functions

        
    def emailthejobtoafriend(self, jobid):
        try:
            self.page.wait_for_load_state(state='networkidle')
            iframe = self.page.frame_locator("#"+self.id_iframe)
            jobidspan = iframe.locator(selector_or_locator="xpath="+self.xpath_span_jobid(jobid=jobid))
            jobheader = iframe.locator(selector_or_locator="xpath="+self.xpath_header_title)
            referbutton = iframe.locator(selector_or_locator="xpath="+self.xpath_span_referbutton)
            if jobidspan.is_visible():
                referbutton.click()
                self.rm.addscreenshot("JD page for jobid "+jobid+" is displayed and the title is "
                                      +jobheader.inner_text()+" and Clicked on refer button")
            else:
                self.rm.addscreenshot("JD page for jobid "+jobid+" is NOT displayed")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during displaying search result for job id = "+jobid)
            print(e)
            return False
        else:
            return True