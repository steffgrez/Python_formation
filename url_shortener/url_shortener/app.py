from wsgiref import simple_server

import falcon

db = {}

class ShortLinkGenerator(object):
    def on_get(self, request, response):
        print("coucou")
        response.status = falcon.HTTP_200
        response.content_type = 'text/html'
        response.body = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Welcome to our URL shortener!</title>
    </head>

    <style>
        body { background-color: whitesmoke; }
        h1   { color: black; left: 0; line-height: 200px; margin-top: -100px;
               position: absolute; text-align: center; top: 50%; width: 100%; }
    </style>

    <body>
        <h1>Welcome to our URL shortener!</h1>
    </body>
</html>
        """


application = falcon.API()
application.add_route('/short_link', ShortLinkGenerator())


if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, application)
    httpd.serve_forever()