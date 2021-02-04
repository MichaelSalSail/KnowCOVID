from newsapi.newsapi_client import NewsApiClient
from creds import NEWS_API_KEY
import string
import sys
from datetime import datetime
from collections import *

newsapi = NewsApiClient(api_key=NEWS_API_KEY)

all_domains=['vox.com','bbc.com','www.sciencenews.org','buzzfeednews.com',
             'www.theguardian.com/us', 'nbcnews.com', 'apnews.com', 'npr.org']
# switched out sciencenews for news.nationalgeographic.com
# switched out theguardian for abcnews.go.com
# switched nationalgeographic to www.sciencedaily.com
# switched abcnews to reuters
# Still not working properly
# Default link will always be used: www.sciencenews.org
# Default link will always be used: www.theguardian.com/us
fd = open("Looking-for-good.txt", "w+")
today_date = datetime.today().strftime('%Y-%m-%d')

for k in all_domains:
    data = newsapi.get_everything(q='coronavirus',
                                  domains=k,
                                  to=today_date,
                                  language='en',
                                  sort_by='publishedAt',
                                  page=2)
    # data = newsapi.get_sources()
    # category='general', language='en', country='us'

    # sources
    for x, y in enumerate(data["articles"]):
        fd.write(y["url"] + "\n" )

fd.close()
print("All relevant articles on the internet were found.")