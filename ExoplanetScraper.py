#------------------------------ExoplanetScraper.py-----------------------#
"""
Importing modules:
-BeautifulSoup :- bs4
-webdriver :- selenium
-Service :- selenium.webdriver.chrome.service.chrome
-ChromeDriverManager :- webdriver_manager.chrome
-csv
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

#Providing the url
url="https://en.wikipedia.org/wiki/List_of_exoplanets_discovered_in_2016"

#Initiating the driver for Chrome and opening the url stipulated above
browser=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(url)

#Creating the web scraper 
bs=BeautifulSoup(browser.page_source,"html.parser")

#Locating all "table" tag
table_tags=bs.find("table")

#Defining the list to store the data temporarily
final_list=[]

#Running a for loop over all the "tr" tags in the "table" tag
for tr_tag in table_tags.find_all("tr"):
    exoplanet_list=[]

    #Running a for loop over all the "td" tags in a "tr" tag and append them to lists
    for td_tag in tr_tag:

        exoplanet_list.append(td_tag.text)
        
    final_list.append(exoplanet_list)

#Defining the list to store the refiend data
new_final_list=[]

#Running a for loop over the list to extract its elements
for planet_info in final_list:
    new_final_list_element=[]

    #Running a for loop over each element of the list 
    for point in planet_info:

       #Verifying whether the elements have "\n" in their values or not
       #Case-1 ~Replacing "\n" 
       if "\n" in point:
           new_point=point.replace("\n","")
           new_final_list_element.append(new_point)
       #Case-2 ~Nothing    
       else: 
           new_final_list_element.append(point) 

    new_final_list.append(new_final_list_element)             

#Running a for loop over the refiend list to refine it further
for refined_planet_info in new_final_list:

    #Running a for loop over each element of the refined list
    for refined_point_index,refined_point in enumerate(refined_planet_info):

        #Verifying whether the elements have empty strings as their values or not
        #Case-1 ~Removing the empty strings
        if refined_point==""  :
            refined_planet_info.remove(refined_point)

#Defining the final list for writing all the data into a csv file
write_list=[]

#Running a for over the refined list
for element in new_final_list:
    write_list_element=[]

    #Running a for loop over each element of the refined list
    for value_index,value in enumerate(element):

        #Verifying whether the indexes of the elements are desirable or not
        #Case-1 ~The elements are appended into a new list
        if value_index==0 or value_index==1 or value_index==2 or value_index==7:
            write_list_element.append(value)

    write_list.append(write_list_element)        
    
#Providing an input for the user to decide a file name
file_input=input("Please provide the file name:")

#Verifying whether file name given by user has "." in or not
#Case-1 ~"." is removed by splitting the file name with regard to it
if "." in file_input:
    file_name,file_extension=file_input.split(".")
    file_input=file_name

#Creating a csv file with the name set according to the user's input
with open("{}.csv".format(file_input),"w") as s:
    
    #Initiating the writer and using it to write into the file
    writer=csv.writer(s)
    writer.writerows(write_list)

#Printing the ending message
print("Thank you for using ExoplanetScraper.py!")    
#------------------------------ExoplanetScraper.py-----------------------#