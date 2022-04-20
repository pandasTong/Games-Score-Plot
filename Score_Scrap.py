from selenium import webdriver
import numpy as np
import pandas as pd 
import time

# Initiate webdrive
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

# Scrap scores for each year

dlist = {'year': [], 'games': [], 'score': [], 'team': []}
week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for i in range(1969,2022):

	y, g, s, t = [],[],[],[]
	template = "https://www.basketball-reference.com/playoffs/NBA_{}.html"
	url = template.format(i)
	print(url)
	wd = webdriver.Chrome('/Users/t.b/Desktop/webdriver/chromedriver', options = chrome_options)
	wd.get(url)
	wd.maximize_window()
	wd.execute_script("window.scrollTo(0, 400)")
	time.sleep(5)

# Find Element
	a = wd.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div[2]/table/tbody/tr[1]/td[1]/span/strong")
	a.click()
	b = wd.find_element_by_xpath("/html/body/div[2]/div[6]/div[2]/div[2]/table/tbody/tr[2]/td/div/table/tbody")
	c = b.find_elements_by_css_selector('tr td')
	print(len(c))

# Append to Dictionary
	l = []
	for d in c:
		e = d.get_attribute('innerText')
		if e[:3] in week:
			pass
		elif e.startswith('Game'):
			g.append(e)
			g.append(e)
		elif e.isdigit() == True:
			s.append(e)
		else:
			t.append(e)
	y = [i] * int(len(c)/3)
	dlist['year'] += y
	dlist['games'] += g
	dlist['score'] += s
	dlist['team'] += t
	wd.close()

# Convert to DataFrame
final_score = pd.DataFrame(dlist)

# Parsing & Cleaning
final_score['games'] = final_score['games'].apply(lambda x: 'G'+x[-1] if x.startswith('Game') else x)
final_score['team'] = final_score['team'].str.replace('@ ', '')

# Keep team name only
temp = final_score['team'].str.split(' ', expand = True)
temp[2][temp[2].isnull()] = temp[1]
temp[1][temp[1] != 'Trail'] = ''
temp['x'] = temp[1] + temp[2]
final_score['team'] = temp['x']

# Uncomment to Save to CSV
final_score.to_csv('df.csv', index = False)
