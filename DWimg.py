#!/usr/local/bin/python
# -*- coding: utf-8 -*-


import requests
import os
import re
from markdown import markdown
from bs4 import BeautifulSoup

def readTargetFromFile():
	# Read hackmd note URL from file
	# Declare
	targets=[]
	with open('//Users//shuyue.wu//Documents//Hack_Py//DownloadImg//targets.txt') as f:
		line = f.readline()
		while line:
			targets.append(line.strip())
			#print(line, end='')
			line = f.readline()
	f.close()
	#print(targets)
	return targets

def parse(target):
	# Parsing hackmd note by beautifulsoup
	# Declare
	mk = ""
	
	#response = requests.get('https://hackmd.io/@F42tsulnReKfQB3f9gBp7Q/By5xTmPqj')
	response = requests.get(target)
	#print(target)
	soup = BeautifulSoup(response.content, 'html.parser')
	#print(type(soup))

	# Extract Markdown content from HTML
	for a in soup.find_all(id='doc'):
		mk = a.contents
		#print(mk)	
	return mk


def imageExtract(mkContent):
	# Extract Image URL from Markdown Content
	# Declare
	images = []
	mkConvert = markdown(mkContent) # Convert markdown to HTML
	soup = BeautifulSoup(mkConvert, 'html.parser') # Parse HTML content
	for i in soup.find_all('img'):
		images.append(i.attrs['src'])
	#print(images)
	#print(len(images))
	return images

def createDir(dirName):
	# Set up directory Name
	targetDir = dirName
	parent_dir = "//Users//shuyue.wu//Documents//Hack_Py//DownloadImg//"
	path = os.path.join(parent_dir, targetDir)

	# Create directory
	try:
		if not os.path.exists(path):
			print("Directory '%s' not exist!!"% targetDir)
			os.mkdir(path)
			print("Directory '%s' created!!"% targetDir)
	except OSError as err:
		print(err)

def downloadImage(path, imagesURL):
	# Download image from url
	for imageindex in range(len(imagesURL)):
		res = requests.get(str(imagesURL[imageindex]), stream=True)
		fullPath = path+'/'+str(imageindex)
		print(fullPath)
		if res.status_code == 200:
			with open(fullPath, 'wb') as file:
				file.write(res.content)
			#print('Image Successfully Downloaded: ', imageindex)
			#file.close()
		else:
			print('Image Couldn\'t be retrieved!!!')

def main():
	# Declare
	mkDatas = []
	imagesURL = []
	hackmdURL = readTargetFromFile()
	# Extract markdown contents
	for targetURL in hackmdURL:
		#print(targetURL)
		mkDatas.append(parse(targetURL))
		#print(mkDatas)
	#print(mkDatas[0][0])
	#print(mkDatas[1][0])

	# Extract images 
	for index in range(len(mkDatas)):
		# Extract Title from markdown
		# Using Title to set up directory Name
		title = re.findall(r'^#\s(\S*)\n', str(mkDatas[index][0]))[0]
		createDir(title)
		dirPath = os.path.abspath(title)

		# Extract images
		mkDatas[index][0]
		imagesURL = imageExtract(mkDatas[index][0])
		#print(imagesURL)
		downloadImage(dirPath, imagesURL)	

	#mkContent = str(markdownDatas[0][0])
	#print(markdown(markcontent))
	#converted = markdown(markcontent)
	#print(converted)
	'''
	soup2 = BeautifulSoup(converted, 'html.parser')
	datas2=[]
	for i in soup2.find_all('img'):
		#print(i)
		datas2.append(i.attrs['src'])
	'''
	#print(datas2)
	#print(len(datas2))


if __name__ == '__main__':
	main()