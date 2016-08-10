#!/usr/bin/python2.7

import re
import sys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
import datetime
import os
from pyvirtualdisplay import Display
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
import pdb

#instantiate virtual display
display = Display(visible=0, size=(800, 600))
display.start()

#function to remove Non-Ascii Characters(Specifically BOM)
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

#initialize selenium python we driver
browser = webdriver.Firefox() # Get local session of firefox


log = open('logs/generate.txt','a')

#Start Mirror Site Generation for Deutsche Bank  Jobs
log.write("\nStart Mirror Site Generation for Deutsche Bank \n")
curr_timestamp = datetime.datetime.now()
log.write("Mirror Site Generated On: "+str(curr_timestamp)+"\n")

browser.get("https://www.db.com/careers/en/prof/role-search/job_search_results.html#")
time.sleep(10)
print"open"

#HTML FILE STRUCTURE

DeutscheBank = open('var/DeutscheBank.html','w')
DeutscheBankstarthtmlcode = "<html>\n<head>\n</head>\n<body>\n<h1> Deutsche Bank Jobs</h1>\n<table><tbody>"
DeutscheBankendhtmlcode = "</tbody>\n</table>\n</body>\n</html>"

DeutscheBank.write(DeutscheBankstarthtmlcode)

jobcount = 0
jobArray = []
try:
	# for i in range (0,100):
		# try:

			# loadmorepage = browser.find_element_by_xpath("//a[@class='custom-button action-btn showmore hr-type-a']")
			# print"found more button"
			# loadmorepage.click()
			# time.sleep(8)
			# browser.save_screenshot('screenie.png')
			# # try:
				# # Stop = browser.find_element_by_xpath("//tr[@style='display: none;' and @class='load-more']")
				# # print "Found display none"
				# # break
			# # except NoSuchElementException:
				# # pass
				# # print "pass"
		# except NoSuchElementException:
			# log.write("Element Not Found\n")
	try:

		joblinks = browser.find_elements_by_xpath("//a[@class='custom-button grey-orange findOutMore']")
		numJobs = len(joblinks)
		print numJobs

		for link in joblinks:
			jobid = link.get_attribute('data-jobid')
			href1 = "https://www.db.com/careers/en/prof/role-search/job_search_results.html#JobOpeningId="
			job=href1+jobid
			print job
			jobArray.append(job)
	except NoSuchElementException as e:
		log.write("Element Not Found: " + e.msg + "\n")

	# Create array of job links and original html of its row in the results table since date posted is not on detail page url
	for job in jobArray:

		browser.get(job)
		time.sleep(8)
		detailUrl = job
		Desc = browser.find_element_by_xpath("//div[@id='db-jobad']").get_attribute("innerHTML")
		browser.save_screenshot('Des.png')
		print(Desc)
		output = "<tr><td>" + Desc + "</td><td><a href='" + detailUrl + "'>" + detailUrl + "</a></td></tr>\n"
		output = removeNonAscii(output)
		DeutscheBank.write(output)

		jobcount = jobcount + 1



except NoSuchElementException:
	log.write("Element Not Found\n")

print(jobcount)
DeutscheBank.write(DeutscheBankendhtmlcode)
DeutscheBank.write("<h2>Total Jobs Extracted: "+str(jobcount)+"</h2>\n")
DeutscheBank.close()
browser.close()
display.stop()
log.close()
