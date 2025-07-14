import requests
from bs4 import BeautifulSoup
import pyfiglet
import csv

baner = pyfiglet.figlet_format("WEB SCRAPPER")
print(baner)

website_url = "https://infopark.in/companies/job"
try:
    res = requests.get(website_url, verify=False)
    res.raise_for_status()  # Check for any request errors
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.find_all("div", {"class": "row company-list joblist"})
    
    with open("results.csv", "w+", newline='') as file:
        writer = csv.writer(file, dialect="excel")
        writer.writerow(["Title", "Company Name", "Last Date", "Link"])
        
        for job in jobs:
            title_element = job.find("a")
            title = title_element.text if title_element else "Title Not Found"
            link = title_element["href"] if title_element else "Link Not Found"
            
            company_name = job.find("div", {"class": "jobs-comp-name"}).text.strip() \
                if job.find("div", {"class": "jobs-comp-name"}) else "Company Name Not Found"
                
            last_date_element = job.find("div", {"class": "job-date"})
            last_date = last_date_element.text.strip() if last_date_element else "Last Date Not Found"
            
            writer.writerow([title, company_name, last_date, link])
            writer.writerow([title, company_name, last_date, link])

            print("Title:", title)
            print("Company:", company_name)
            print("Last Date:", last_date)
            print("Link:", link)
            print()  # Empty line for separation

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
