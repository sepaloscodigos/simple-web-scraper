# to import requests and bs4, need to set up a virtual environment. Do this by putting
# (python3 -m venv venv) and then (source venv/bin/activate) and then (python -m pip install requests)
# and finally (python -m pip install beautifulsoup4)
import requests
from bs4 import BeautifulSoup

# gets the desired url
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# finds all the job postings
job_elements = results.find_all("div", class_="card-content")

# prints all the job titles, companies, and locations
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")

# finds only the jobs that include "python" (and it makes the text lowercase before checking)
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())

# finds the html code for only the python jobs
python_job_elements = [h2_element.parent.parent.parent for h2_element in python_jobs]

# prints the job title, company, and location for only the python jobs as well as the links to apply
# for each job
for job in python_job_elements:
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")
    # print the job title, company offering the job, and the job location
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    # since each job has 2 links, and we only want the second one, this assigns the second
    # link in the list to the variable "link"
    link = job.find_all("a")[1]["href"]
    print(link)
    print()
    



