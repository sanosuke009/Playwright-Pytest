from web.src.test.baseClass.baseclass import baseclass
from web.src.test.config.propConfig import referraltestdatafilepath
import pytest

from web.src.test.pageObjects.referral.jobidpage import jobidpage
from web.src.test.pageObjects.referral.jobsearchresultpage import jobsearchresultpage
from web.src.test.pageObjects.referral.ref_launchpage import ref_launchpage


@pytest.fixture(scope="function", autouse=True)
def before_each(base:baseclass):
    base.settestdatamanager(referraltestdatafilepath)
    yield base

@pytest.mark.parametrize(
    "keyword",
    ["Refer"],
)
def test_referral(base:baseclass, keyword):
    testdata = base.tm.gets(keyword)
    base.page.goto(testdata.get("url"))
    launchpageobj = ref_launchpage(base)
    assert launchpageobj.verifylaunchpage() == True
    assert launchpageobj.searchforjobid(testdata.get("jobid")) == True
    resultpageobj = jobsearchresultpage(base)
    assert resultpageobj.verifyresult(testdata.get("jobid")) == True
    jobidpageobj = jobidpage(base)
    assert jobidpageobj.emailthejobtoafriend(testdata.get("jobid")) == True
