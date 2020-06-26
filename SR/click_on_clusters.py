import time

from Data.parameters import Data


class Clusters():
    def __init__(self, driver):
        self.driver = driver

    def check_markers_on_clusters_map(self):
        self.driver.find_element_by_id(Data.sr_cluster_btn).click()
        time.sleep(15)
        dots = self.driver.find_elements_by_class_name(Data.dots)
        return dots