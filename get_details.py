import requests
from bs4 import BeautifulSoup
import json
import datetime as dt
import os 
from pathlib import Path

# function to get filer name for json 
# format: outages_date.json 
# where date is today's date
def get_filename():
    today = dt.date.today().strftime("%d-%m-%Y")
    filename = f"outages_{today}.json"
    return filename

# function to check if the data was updated today
# if a json file containing today's date exists
# it was already updated.
def check_update_today(filename):
    jsons = [file for file in os.listdir('./json')]
    if filename in jsons:
        return True
    else:
        return False

def get_soup_from_url(url="https://www.goaelectricity.gov.in/Goa_power_outage.aspx"):
    r = requests.get(url)
    if r.status_code != 200:
        return False
    soup = BeautifulSoup(r.content,features="lxml")
    return soup

#get the power outage table from soup
def get_outage_table(soup):
    return soup.find(id="GV_power_outage")

# parse the table and jsonify it
def jsonify_table(outage_table_soup, filename):
    table_rows=outage_table_soup.find_all('tr')
    outage_dict={'outages':[]}
    JSON = Path('./json')

    for table_row in table_rows:
        cells = table_row.find_all('td')
        if len(cells)==6:
            index = cells[0].span.text
            date = cells[1].span.text
            feeders = [feeder.strip() for feeder in cells[2].span.text.split(',')]
            areas = [area.strip() for area in cells[3].span.text.split(',')]
            from_time = cells[4].span.text
            to_time = cells[5].span.text
            data = {
                'index': index,
                'date': date,
                'feeders': feeders,
                'areas': areas,
                'from_time': from_time,
                'to_time': to_time
            }
            outage_dict['outages'].append(data)

    with open(JSON/filename,'w') as file:
        outage_json = json.dump(outage_dict, file, indent=4)

# if data wasn't updated today, update it.
def update():
    filename = get_filename()
    if not check_update_today(filename):
        soup = get_soup_from_url()
        outage_table_soup = get_outage_table(soup)
        jsonify_table(outage_table_soup,filename)

if __name__=="__main__":
    update()