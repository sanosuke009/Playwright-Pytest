"This module contains the page object class of the referral launch page"

from web.src.test.baseClass.baseclass import baseclass


class referralformpage:

    def __init__(self, base:baseclass):
        self.page = base.page
        self.rm = base.rm

    # Page object locators
    id_iframe = "icims_content_iframe"
    xpath_input_title = lambda self, title: "//label[text()='"+title+"']/parent::div/following-sibling::div/input"
    xpath_textarea_messagetocandidate = "//textarea[@id='PortalProfileFields.ReferrerCommentsToReferral']"
    xpath_button_submit = "//input[@type='submit']"
    xpath_div_success = "//div[contains(text(),'Thank you for emailing your friend!')]"

    # Page object methods/functions

        
    def refer(self, _referrername, _referreremail, _firstname, _lastname, _email, _message):
        try:
            xpath_input_referrerfullname = self.xpath_input_title("Your Full Name")
            xpath_input_referreremail = self.xpath_input_title("Your Email")
            xpath_input_firstname = self.xpath_input_title("First Name")
            xpath_input_lastname = self.xpath_input_title("Last Name")
            xpath_input_email = self.xpath_input_title("Email")
            self.page.wait_for_load_state(state='networkidle')
            iframe = self.page.frame_locator("#"+self.id_iframe)
            referrerfullname = iframe.locator(selector_or_locator="xpath="+xpath_input_referrerfullname)
            referreremail = iframe.locator(selector_or_locator="xpath="+xpath_input_referreremail)
            firstname = iframe.locator(selector_or_locator="xpath="+xpath_input_firstname)
            lastname = iframe.locator(selector_or_locator="xpath="+xpath_input_lastname)
            email = iframe.locator(selector_or_locator="xpath="+xpath_input_email)
            messagetocandidate = iframe.locator(selector_or_locator="xpath="+self.xpath_textarea_messagetocandidate)
            referbutton = iframe.locator(selector_or_locator="xpath="+self.xpath_button_submit)
            if referrerfullname.is_visible():
                referrerfullname.fill(_referrername)
                referreremail.fill(_referreremail)
                firstname.fill(_firstname)
                lastname.fill(_lastname)
                email.fill(_email)
                messagetocandidate.fill(_message)
                self.rm.addscreenshot("The form is filled with these data: "+_referrername+" "+_referreremail+" "+
                                      _firstname+" "+_lastname+" "+_email+" "+_message)
                referbutton.click()
                self.page.wait_for_load_state(state='networkidle')
                successmessage = iframe.locator(selector_or_locator="xpath="+self.xpath_div_success)
                successmessage.wait_for()
                if successmessage.is_visible():
                    self.rm.addscreenshot("Referral successful!")
                else:
                    self.rm.addscreenshot("Referral NOT successful!")
                    return False
            else:
                self.rm.addscreenshot("Refer page is NOT displayed")
                return False
        except Exception as e:
            self.rm.addscreenshot("Error occurred during final refer page")
            print(e)
            return False
        else:
            return True