import os
import time

from Data.parameters import Data
from filenames import file_extention
from get_dir import pwd
from reuse_func import GetData


class DistrictwiseCsv():

    def __init__(self, driver):
        self.driver = driver

    def click_download_icon(self):
        cal = GetData()
        self.fname = file_extention()
        cal.click_on_state(self.driver)
        cal.page_loading(self.driver)
        self.driver.find_element_by_id(Data.Download).click()
        time.sleep(3)
        p = pwd()
        self.filename = p.get_download_dir() + "/" + self.fname.pat_district()
        if os.path.isfile(self.filename) != True:
           return "File Not Downloaded"
        if os.path.isfile(self.filename) == True:
            os.remove(self.filename)


