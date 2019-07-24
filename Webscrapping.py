from selenium import webdriver
import selenium.webdriver.common.keys  as Keys
from time import sleep
class twitter_dy:
	def __init__(self,usermail,password):
		self.usermail=usermail
		self.password=password
		self.bot=webdriver.Firefox()
	def login(self):
 		bot=self.bot
 		avis_url='https://mail.avisbudget.com/OWA/auth/logon.aspx?replaceCurrent=1&url=https%3a%2f%2fmail.avisbudget.com%2fowa%2f%23authRedirect%3dtrue'
 		bot.get(avis_url)
 		sleep(5)
 		usrnm_fld_loc=bot.find_element_by_name('username')
 		pwd_fld_loc=bot.find_element_by_name('password')
 		usrnm_fld_loc.clear()
 		pwd_fld_loc.clear()
 		usrnm_fld_loc.send_keys(self.usermail)
 		pwd_fld_loc.send_keys(self.password)
 		sleep(1)
 		pwd_fld_loc.send_keys(Keys.RETURN)



dy=twitter_dy('*Replace this username*','*Replace this password*')
dy.login()
