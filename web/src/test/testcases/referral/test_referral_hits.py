from web.src.test.baseClass.baseclass import baseclass
from web.src.test.config.propConfig import referraltestdatafilepath
import pytest

from web.src.test.pageObjects.referral.jobidpage import jobidpage
from web.src.test.pageObjects.referral.jobsearchresultpage import jobsearchresultpage
from web.src.test.pageObjects.referral.ref_launchpage import ref_launchpage
from web.src.test.pageObjects.referral.referralformpage import referralformpage

import gspread
from oauth2client.service_account import ServiceAccountCredentials


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(referraltestdatafilepath)
    yield base

""" @pytest.mark.parametrize(
    "keyword",
    ["Refer"],
) """
""" def method_test_referral(base:baseclass, keyword):
    testdata = base.tm.gets(keyword)
    base.page.goto(testdata.get("url"))
    launchpageobj = ref_launchpage(base)
    assert launchpageobj.verifylaunchpage() == True
    assert launchpageobj.searchforjobid(testdata.get("jobid")) == True
    resultpageobj = jobsearchresultpage(base)
    assert resultpageobj.verifyresult(testdata.get("jobid")) == True
    jobidpageobj = jobidpage(base)
    assert jobidpageobj.emailthejobtoafriend(testdata.get("jobid")) == True
    referralformpageobj = referralformpage(base)
    assert referralformpageobj.refer(
        testdata.get("referrerfullname"),
        testdata.get("referreremail"),
        testdata.get("firstname"),
        testdata.get("lastname"),
        testdata.get("email"),
        testdata.get("messagetocandidate")) == True """
    

def method_test_referral(base:baseclass, keyword, firstname, lastname, emailid, jobid):
    testdata = base.tm.gets(keyword)
    base.page.goto(testdata.get("url"))
    launchpageobj = ref_launchpage(base)
    assert launchpageobj.verifylaunchpage() == True
    assert launchpageobj.searchforjobid(jobid) == True
    resultpageobj = jobsearchresultpage(base)
    assert resultpageobj.verifyresult(jobid) == True
    jobidpageobj = jobidpage(base)
    assert jobidpageobj.emailthejobtoafriend(jobid) == True
    referralformpageobj = referralformpage(base)
    referrerfullname = testdata.get("referrerfullname")
    referreremail = testdata.get("referreremail")
    messagetocandidate = testdata.get("messagetocandidate")
    firstname = firstname
    lastname = lastname
    emailid = emailid
    jobid = jobid
    print("referrerfullname "+referrerfullname)
    print("referreremail "+referreremail)
    print("messagetocandidate "+messagetocandidate)
    print("firstname "+firstname)
    print("lastname "+lastname)
    print("emailid "+emailid)
    print("jobid "+jobid)
    referralformpageobj.refer(referrerfullname, referreremail, firstname, lastname, emailid, messagetocandidate)
    


@pytest.mark.parametrize(
    "keyword",
    ["Refer"],
)
def test_referral_poc(base:baseclass, keyword):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('', scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open('Referral Form Hyland')
    worksheet = spreadsheet.sheet1
    data = worksheet.get_all_values()
    for row in data[1:]:
            firstname = row[1]
            lastname = row[2]
            emailid = row[3]
            jobid = row[4]
            jobid = jobid.split()[0]
            method_test_referral(base, keyword, firstname, lastname, emailid, jobid)
    base.page.__exit__
            

