import get_details
import json
import os

# update folder and check for any outages
# in bicholim or muslim wada
def outage():
    os.chdir('/home/flash/Programming/Sideline/Android/Outages/script')
    try:
        get_details.update()
    except:
        print('Error, could not update.')
    else:
        check_outage_in(['Bicholim'])

# open today's json as a dictionary
def get_outage_dict():
    filename=get_details.get_filename()
    with open(f'./json/{filename}') as file:
        outage_dict = json.load(file)['outages']
    return outage_dict

#def print_outage_details(details):
#    print(f'Date:\t\t{details["date"]}')
#    print(f'From time:\t{details["from_time"]}')
#    print(f'To time:\t{details["to_time"]}')
#    print(f'Feeders:')
#    for feeder in details['feeders']:
#        print(f'\t\t{feeder}')
#    print(f'Areas:')
#    for area in details['areas']:
#        print(f'\t\t{area}')

# a wrapper for printing any upcoming outages
def print_outage_details(outages):
    if outages:
        print(f"Outage on: ", end="")
        for outage in outages:
            print(outage['date'], end="\t")
        print()
    else:
        print("No outages.")

# check outages in a list of areas provided
def check_outage_in(areas):
    outage_dict=get_outage_dict()
    outages_found=[]
    for outage_details in outage_dict:
        for area in areas:
            if area.upper() in outage_details['feeders']+outage_details['areas']:
                outages_found.append(outage_details)
    print_outage_details(outages_found)

if __name__=='__main__':
    outage()