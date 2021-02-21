# power_outages
My mom forgot about today's power outrage so I automated it. I'm too lazy to check the website.
## Description
It scrapes the data from Goa Electricity Department website once a day, checks for any planned power outages in my area and shows it in my status bar. I wrote it over an afternoon, so the code may be unclean.

## Requirements
- BeautifulSoup4
- Requests
- Py3Status and i3 (If you want to put it in your status bar)

## Usage
- Clone the repo
- Add your location in `outage.py`. It would be more accurate if you add your ward/colony instead of city/town.
- Run `outage.py` in python
- If you use py3status, check their documentation for how to add custom modules. You can either copy `outage_py3status.py` to their modules folder or include the path to this repo in your pc. It just pipes the output of `outage.py` to status bar instead of stdout.
