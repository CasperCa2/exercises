# Write your code here
import re

def scrape_email_addresses(string):
    return re.findall("[a-z0-9A-Z.]+@[a-z0-9A-Z.]+", string)
