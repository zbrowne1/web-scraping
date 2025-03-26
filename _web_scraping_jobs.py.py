#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

#URL of the website to scrape
URL= "https://realpython.github.io/fake-jobs/"
try:
    # Send a GET request to fetch the webpage content
    response = requests.get(URL)
    response.raise_for_status() #erro for bad repsonses
    
    #Parse HTML content
    soup = BeautifulSoup(response.text,"html.parser")
 
    # Extract job postings
    job_listings = soup.find_all ("div", class_="card-content")

    # Lists to store job data
    jobs_data = []

    # Loop through each job listing and extract the required information
    for job in job_listings:
        title = job.find("h2", class_="title is-5").text.strip()
        company = job.find("h3", class_="subtitle is-6 company").text.strip()
        location = job.find("p", class_="location").text.strip()
        date_posted_str= job.find("time").text.strip()

        #Convert date string to datetime object
        date_posted = datetime.strptime(date_posted_str,"%Y-%m-%d")
        day_of_week = date_posted.strftime("%A")
        day_and_month = date_posted.strftime ("%d %B")
        year = date_posted.year
        #Split location into city and state
        location_parts= location.split(",")
        city = location_parts[0]
        state = location_parts[1] if len (location_parts) > 1 else "Unknown"

        # Append job data to the list
        jobs_data.append({
           "Job Title": title,
           "Company Name": company,
           "Location (City)": city,
           "Location (State)": state,
           "Date Posted (Day, Month, Day of Week)" : f"{day_of_week}, {day_and_month}",
           "Date Posted (Year)" : year
        })

    #Convert list to Pandas DataFrame
    df = pd.DataFrame(jobs_data)
    
    # Define path for CSV file
    csv_file = "realpython_jobs.csv"
    
    # Save to CSV file
    df.to_csv(csv_file, index=False)
    
    # Display rows a few 
    print (df.head())
except requests. exceptions.RequestException as e:
    print (f" Errors] fetching data: {e}")



  


# In[ ]:




