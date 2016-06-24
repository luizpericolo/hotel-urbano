import sys
import xmltodict
import requests

cd_url = "http://www.w3schools.com/xml/cd_catalog.xml"

def get_cd_list():
    response = requests.get(cd_url)
    response_dict = xmltodict.parse(response.text)
    return [dict(cd) for cd in response_dict.get("CATALOG", {}).get("CD", [])]

def get_cd_attribute(name):
    cd_list = get_cd_list()

    return [cd.get(name, "") for cd in cd_list]

if __name__ == "__main__":
    _, attribute = sys.argv
    cd_titles = get_cd_attribute(attribute.upper())
    for cd_title in cd_titles:
        print(cd_title)
