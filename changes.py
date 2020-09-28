from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from change_template import Templates as tp
import time

class CreateChange():

    def __init__(self, settings):
        self.userid = settings['userid']
        self.password = settings['password']
        self.ini = settings['ini']
        self.driver = webdriver.Firefox()
        # self.chg_templates = Templates()

    def start_browser(self):
        self.driver.get('https://jefferson.service-now.com/navpage.do')
        time.sleep(1)
        self.driver.maximize_window()

    def login(self):
        self.driver.implicitly_wait(3)
        id_box = self.driver.find_element_by_name('j_username')
        id_box.clear()
        id_box.send_keys(self.userid)

        pass_box = self.driver.find_element_by_name('j_password')
        pass_box.clear()
        pass_box.send_keys(self.password)

        login_button = self.driver.find_element_by_name('_eventId_proceed')
        login_button.click()

        wrong_password = None
        try:
            self.driver.implicitly_wait(2)
            wrong_password = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/section/p')
        except:
            pass

        if wrong_password:
            raise Exception("Wrong password entered")

    def update_login_settings(self, settings):
        self.userid = settings['userid']
        self.password = settings['password']
        self.ini = settings['ini']
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def create_change(self):
        self.driver.implicitly_wait(10)

        create_new_change = self.driver.find_element_by_id("concourse_module_323bb07bc611227a018aea9eb8f3b35e")
        create_new_change.click()

        self.driver.implicitly_wait(3)

        # Must switch to the correct iframe to find the elements
        # see https://stackoverflow.com/questions/44834358/switch-to-an-iframe-through-selenium-and-python for more information
        iframe = self.driver.find_element_by_xpath("//*[@id='gsft_main']")
        self.driver.switch_to.frame(iframe)

        #user name
        self.driver.implicitly_wait(1)
        user_name = self.driver.find_element_by_xpath("//*[@id='sys_display.change_request.assigned_to']")
        user_name = user_name.get_attribute('value')

        #Category
        self.driver.find_element_by_xpath("//*[@id='change_request.category']/option[@value='Epic']").click()

        # #Configuration item
        configuration_item = self.driver.find_element_by_id('sys_display.change_request.cmdb_ci')
        configuration_item.click()
        configuration_item.click()
        configuration_item.send_keys('Master File(s)')
        configuration_item.send_keys(Keys.ENTER)
        configuration_item.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(2)

        #CM Ticket #
        package_id = self.driver.find_element_by_xpath("//*[@id='change_request.u_package_id']")
        package_id.send_keys('T140-')

        #Priority
        self.driver.find_element_by_xpath("//*[@id='change_request.u_priority']/option[@value='3']").click()

        #Type
        self.driver.find_element_by_xpath("//*[@name='change_request.type']/option[@value='Maintenance']").click()

        #Assignment group
        assignment_group = self.driver.find_element_by_name('sys_display.change_request.assignment_group')
        assignment_group.send_keys('Enterprise Business Intelligence')
        assignment_group.send_keys(Keys.ENTER)

        #Title
        title = self.driver.find_element_by_name('change_request.short_description')
        title.send_keys(f'Maintenance Change: {tp.template[self.ini]["title"]}')

        #Affected master files
        unlock_btn = self.driver.find_element_by_xpath("//*[@id='change_request.u_master_file_list_unlock']")
        unlock_btn.click()

        master_files = self.driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_master_file_list']")
        for item in tp.template[self.ini]['ini']:
            master_files.send_keys(item)
            time.sleep(1)
            master_files.click()
            master_files.send_keys(Keys.ENTER)

        lock_btn = self.driver.find_element_by_xpath("//*[@id='change_request.u_master_file_list_lock']")
        lock_btn.click()

        #Reason for change
        rsn_for_chg = self.driver.find_element_by_name('change_request.u_reason_for_change')
        rsn_for_chg.send_keys(f'{tp.template[self.ini]["rsn"]}')

        #Migration Method
        self.driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_migration_method_data_courier']").click()

        #Migrator
        migrator = self.driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_migrator']")
        migrator.send_keys(user_name)
        migrator.send_keys(Keys.ENTER)

        #Destination Environment
        self.driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]").click()

        #TST
        self.driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_tst']").click()

        #AMBTST
        self.driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_ambtst']").click()

        #MST
        self.driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_mst']").click()

        #PRD
        self.driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_prd']").click()

        #Planning Tab
        self.driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/span[4]/span[1]/span[2]").click()

        #Change Plan
        chg_plan = self.driver.find_element_by_xpath("//*[@id='change_request.change_plan']")
        chg_plan.send_keys(tp.template[self.ini]['plan'])

        #Backout plan
        backout_plan = self.driver.find_element_by_xpath("//*[@id='change_request.backout_plan']")
        backout_plan.send_keys(tp.template[self.ini]['backout'])

        #Test Plan
        tst_plan = self.driver.find_element_by_xpath("//*[@id='change_request.test_plan']")
        tst_plan.send_keys(tp.template[self.ini]['test'])

        #Tester
        tester = self.driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_name_of_testing_person']")
        tester.send_keys(self.userid)
        tester.send_keys(Keys.ENTER)

        #End user communication
        end_usr_comm = self.driver.find_element_by_xpath("//*[@id='change_request.u_string_end_user_com_plan']")
        end_usr_comm.send_keys('N/A')
