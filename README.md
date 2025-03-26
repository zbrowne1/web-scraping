# WEB SCRAPING
This is a python script that scrapes job listing from the website Fake JoB Websites. Additionally it extracts key job details. The extracted data is then structured into a Pandas Data Frame and saved as a CSV File.
I used Python for this project. I also used requests for fetching the webapage datta, Beautiful Soup for the webscraping and Pandas to structure and save the data.

## What is extracted?
The script extracts the following: Job Titles, Company Name, Location (City), Location(State), Date Posted, Day, Month, Day of the week and Year
### Running the scripts
In the command prompt, I had to run the code pip install requests beautifulsoups4 pandas to install the libraries that were required. 
After installing the libraries, I created the script using Jupyter notebook and downloaded the script as a py file. Next, I opened the command prompt and used the cd command to navigate to the folder where the script is located cd C:\Userd\zoniq\Downloads. Next I executed the following command in the command prompt python webscraping.py and then five rows and six columns of the data appeared in the command prompt. I also checked my downloads and noticed that a csv file was automatically generated after running the script. I went ahead and uploaded it on GITHUB
