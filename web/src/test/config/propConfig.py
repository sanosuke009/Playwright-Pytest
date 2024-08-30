localExecution = True # To check between local and vm/docker execution
reportPath = 'allure-results/'
implicitwait = 5000
explicitwait = 5000
browsername = 'chrome'
headless = False
browserargs = ["--start-maximized"]

user_data_dir = "./web/user_data_dir"
playwright_videos_dir = "./recorded-videos/"
playwright_traces_dir = "./test-results/"


#================Parabank====================
parabanktestdatafilepath = "./web/src/test/testData/parabank/testdata.json"

#================Youtube======================
youtubetestdatafilepath = "./web/src/test/testData/youtube/testdata.json"

#================Referral======================
referraltestdatafilepath = "./web/src/test/testData/referral/testdata.json"