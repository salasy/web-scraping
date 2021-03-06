import whois
import csv
from time import sleep
import re
from pandas import DataFrame

domains = open('domains.csv', 'r').read().split()
domain_list = []
email_list = []
for domain in domains:
    try:
        url = whois.whois(domain)
        url = url.text    
        htmltext = str(url)
        htmltext = htmltext.split('\n')
        for line in htmltext:
            if re.findall('Registrant Email', line):
                email = line
                email = re.findall('[^:\s]+@\S+', email)
                domain_list.append(domain); sleep(1)
                email_list.append(email[0]); sleep(1)
    except:
        domain_list.append(domain); sleep(1)
        email_list.append('No match'); sleep(1)

# write to csv
with open('whois.csv', 'w') as f:                        
    data = zip(domain_list, email_list)    
    wtr = csv.writer(f)                                                   
    wtr.writerows(data)

# write to excel
dataframe = DataFrame({'URL': domain_list, 'Email': email_list})
dataframe.to_excel('whois.xlsx', sheet_name='data', index = False)

