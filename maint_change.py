from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from config import DefaultConfig
import time

CONFIG = DefaultConfig()
driver = webdriver.Firefox()

driver.get('https://jefferson.service-now.com/navpage.do')
time.sleep(3)

driver.maximize_window()

id_box = driver.find_element_by_name('j_username')
id_box.send_keys('mlm042')

pass_box = driver.find_element_by_name('j_password')
pass_box.send_keys(CONFIG.SECRET)

login_button = driver.find_element_by_name('_eventId_proceed')
login_button.click()

# time.sleep(10)
driver.implicitly_wait(10)

create_new_change = driver.find_element_by_id("concourse_module_92740c471b78b0905b25db91dd4bcb2b")
create_new_change.click()

# time.sleep(3)
driver.implicitly_wait(3)

# Must switch to the correct iframe to find the elements
# see https://stackoverflow.com/questions/44834358/switch-to-an-iframe-through-selenium-and-python for more information
iframe = driver.find_element_by_xpath("//*[@id='gsft_main']")
driver.switch_to.frame(iframe)

#Category
driver.find_element_by_xpath("//*[@id='change_request.category']/option[@value='Epic']").click()

# #Configuration item
configuration_item = driver.find_element_by_id('sys_display.change_request.cmdb_ci')
configuration_item.send_keys('Master File(s)')
configuration_item.send_keys(Keys.ENTER)
configuration_item.send_keys(Keys.ENTER)
time.sleep(3)

driver.implicitly_wait(2)

#CM Ticket #
package_id = driver.find_element_by_xpath("//*[@id='change_request.u_package_id']")
package_id.send_keys('T140-')

#Priority
driver.find_element_by_xpath("//*[@id='change_request.u_priority']/option[@value='3']").click()

#Type
driver.find_element_by_xpath("//*[@name='change_request.type']/option[@value='Maintenance']").click()

#Assignment group
assignment_group = driver.find_element_by_name('sys_display.change_request.assignment_group')
assignment_group.send_keys('Enterprise Business Intelligence')
assignment_group.send_keys(Keys.ENTER)

#Title
title = driver.find_element_by_name('change_request.short_description')
title.send_keys('Maintenance Change: Update Grouper')

#Affected master files
unlock_btn = driver.find_element_by_xpath("//*[@id='change_request.u_master_file_list_unlock']")
unlock_btn.click()

master_files = driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_master_file_list']")
master_files.send_keys('VCG')
master_files.send_keys(Keys.ENTER)

lock_btn = driver.find_element_by_xpath("//*[@id='change_request.u_master_file_list_lock']")
lock_btn.click()

#Reason for change
rsn_for_chg = driver.find_element_by_name('change_request.u_reason_for_change')
rsn_for_chg.send_keys('***')

#Migration Method
driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_migration_method_data_courier']").click()

#Migrator
migrator = driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_migrator']")
migrator.send_keys('Matthew Moore')
migrator.send_keys(Keys.ENTER)

#Destination Environment
driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/span[2]/span[1]/span[2]").click()

#TST
driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_tst']").click()

#AMBTST
driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_ambtst']").click()

#MST
driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_mst']").click()

#PRD
driver.find_element_by_xpath("//*[@id='label.ni.change_request.u_destination_prd']").click()

#Planning Tab
driver.find_element_by_xpath("/html/body/div[2]/form/div[1]/span[4]/span[1]/span[2]").click()

#Change Plan
chg_plan = driver.find_element_by_xpath("//*[@id='change_request.change_plan']")
chg_plan.send_keys('Update the grouper')

#Backout plan
backout_plan = driver.find_element_by_xpath("//*[@id='change_request.backout_plan']")
backout_plan.send_keys('Undo the change')

#Test Plan
tst_plan = driver.find_element_by_xpath("//*[@id='change_request.test_plan']")
tst_plan.send_keys('Verify grouper has correct records')

#Tester
tester = driver.find_element_by_xpath("//*[@id='sys_display.change_request.u_name_of_testing_person']")
tester.send_keys('Matthew Moore')
tester.send_keys(Keys.ENTER)

#End user communication
end_usr_comm = driver.find_element_by_xpath("//*[@id='change_request.u_string_end_user_com_plan']")
end_usr_comm.send_keys('N/A')
