import requests
from bs4 import BeautifulSoup
import re

def get_social_links(soup):
    social_links = []
    social_tags = soup.find_all(href=re.compile(r"(facebook|linkedin|twitter)"))
    for tag in social_tags:
        social_links.append(tag["href"])
    return social_links

def get_emails(soup):
    emails= []
    email_tags = soup.find_all(href=re.compile(r"(mail)"))
    for tag in email_tags:
        emails.append(tag["href"])
    return emails

def get_contacts(soup):
    phone_Numbers = []
    phone_tags= soup.find_all(href=re.compile(r'(mob|tel|mobile|telephone)'))
    for tag in phone_tags:
        phone_Numbers.append(tag["href"])
    return phone_Numbers


# Get user input for the website URL
website_url = input("Enter the website URL: ")

# Fetch the HTML content of the website
response = requests.get(website_url)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract social links
social_links = get_social_links(soup)
print("Social links:")
for link in social_links:
    print(link)

# Extract emails
emails = get_emails(soup)
print("\nEmails:")
for email in emails:
    i=0
    while email[i]!=":":
        i+=1
    print(email[i+1:])

# Extract contacts
contacts = get_contacts(soup)
print("\nContact:")
for contact in contacts:
    i=0
    while contact[i]!="+" and not contact[i].isdigit():
        i+=1
    print(contact[i:])
