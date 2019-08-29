from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import config
import time
import ele
import logging
logging.basicConfig(level=logging.INFO)
driver = webdriver.Firefox()
driver.get(config.http_url+'info.html')
assert config.FW_version in driver.find_element_by_xpath(ele.e_fw_version).text
assert config.build_name in driver.find_element_by_xpath(ele.e_build_name).text
driver.get(config.http_url+'wancfg.cmd?action=view')
element = driver.find_element_by_xpath('/html/body/blockquote/form/center/table/tbody/tr[2]/td[1]').text
assert element == 'ppp0'
driver.get(config.http_url+'info.html')
assert config.CPE_MAC_Info in driver.find_element_by_xpath(ele.e_cpe_mac).text
driver.get(config.http_url+'dhcpinfo.html')
assert config.LAN1_MAC in driver.find_element_by_xpath(ele.e_dhcp_table).text
logging.warning('finding element '+ele.e_dhcp_table)
assert config.LAN1_IP in driver.find_element_by_xpath(ele.e_dhcp_table).text
logging.info('found element'+ele.e_dhcp_table)
driver.get(config.http_url+'lancfg2.html')
elem = driver.find_element_by_xpath('//html/body/blockquote/form/table/tbody/tr[2]/td[2]/input').clear().send_keys(config.lan_interfaceip)
elem.send_keys(config.lan_interfaceip)
elem = driver.find_element_by_xpath("//html/body/blockquote/form/center/p/input").click()
driver.quit()
