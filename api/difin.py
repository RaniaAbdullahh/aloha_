from http.server import BaseHTTPRequestHandler
from urllib import parse

import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
       
        url_components = parse.urlsplit(s)
       
        query_string_lst =parse.parse_qs(url_components.query)
        if 'word' in query_string_lst:
            print(11111)
            word = query_string_lst["word"][0]
            print(2222,word)
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            r = requests.get(url + word)
            response = r.json()
            print(response)
            all_dif=[]
            for words in response:
                definision = words['meanings'][0]['definitions'][0]['definition']
                all_dif.append(definision)


        message =str(all_dif)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return  
