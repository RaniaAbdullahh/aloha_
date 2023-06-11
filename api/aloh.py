from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        print(111,s)
        url_components = parse.urlsplit(s)
        print(222,url_components)
        query_string_lst =parse.parse_qs(url_components.query)
        print(3333,query_string_lst)

        name = query_string_lst.get('name',False)
        if name :
            message = f'welcome {name[0]}'
        else:
            message = f'welcome stranger'

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        


            