'''This is the file that will be used to judge if a url is safe to go to or not. It will also return important data'''

import json
from traverse import get_root_http, get_root_https

base_msg = '''
Hello. Our bot has found that the link that has been posted, is actually cited to be false.
We have recieved this information from snopes, a reputable fact checking platform.
Some alternatives to find about the {topic} of COVID19 is {source}:
{link}
'''

mixed_msg = '''
Hello we have found that this link might not be as accurate as it seems.
Instead of using these mixed sources, please use official ones like CDC (Center of Disease Control), and WHO (World Health Organization)
WHO: https://www.who.int/emergencies/diseases/novel-coronavirus-2019
CDC: https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html
'''

class Message: # This is the class 
    def __init__(self, base_url, long_url, status, category):
        self.url = long_url
        self.base_url = base_url
        self.status = status
        self.category = category

    def load_message(self): # This function will return reputable alternatives based on the category, along with a message
        if self.status == 'false':
            if self.category == 'origin':
                return base_msg.format( # Returns the base message formatted, done for each category
                    topic = 'spread and origin',
                    source = 'the CDC (Centre of Disease Control)',
                    link = 'https://www.cdc.gov/coronavirus/2019-ncov/prepare/transmission.html'
                )
            elif self.category == 'prevention':
                return base_msg.format(
                    topic = 'prevention and treatement',
                    source = 'WHO (World Health Organization)',
                    link = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public'
                )
            elif self.category == 'international response':
                return base_msg.format(
                    topic = 'international response',
                    source = 'WHO (World Health Organization)',
                    link = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019'
                )
            elif self.category == 'american response':
                return base_msg.format(
                    topic = 'American response',
                    source = 'the CDC (Centre of Disease Control)',
                    link = 'cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fsummary.html#cdc-response'
                )
            elif self.category == 'trump':
                return base_msg.format(
                    topic = 'Trump and COVID19',
                    source = 'the CDC. We want you to look at response done by the professionals',
                    link = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html'
                )
            elif self.category == 'predictions':
                return 'This article is only speculation. If you would like up to date information please check https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/summary.html!'
            elif self.category == 'memes':
                return "It's all fun and games until someone close to you is harmed. Please keep that in mind!"
            elif self.catergory == 'videos':
                return "Please make sure you check the source of this video is reputable. You may be spreading lies without knowing it!"
            elif self.category == 'business':
                return base_msg.format(
                    topic = 'Business and Industries',
                    source = 'WHO (World Health Organization)',
                    link = 'https://www.who.int/emergencies/diseases/novel-coronavirus-2019'
                )
            elif self.category == 'entertainment':
                return 'We have found on snopes that this form of entertainment is spreading lies, please double check the source and stay safe!'
        
        elif self.status == 'mixed':
            return mixed_msg
        

# Load the data from the JSON file
json_file = open('snopes_store.json', 'r+')
data = json.load(json_file)

def check_safe(url: str): # This function will help to determine if the function is safe
    long_url_http = get_root_http(url)
    long_url_https = get_root_https(url)

    if long_url_http in data: # HTTP LINK FOUND IN SNOPES
        return Message(url, long_url_http, data[long_url_http]['status'], data[long_url_http]['category'])
    elif long_url_https in data: # HTTPS LINK FOUND IN SNOPES
        return Message(url, long_url_http, data[long_url_https]['status'], data[long_url_https]['category'])
