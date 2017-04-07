import webapp2
import string
import cgi

form = """
<html>
  <head>
    <title>Unit 2 Rot 13</title>
  </head>
  <body>
    <h2>Enter some text to Rot13:</h2>
    <form method='post'>
      <input type='textarea' name='text' value='%s' style='height: 100px; width: 400px;'></textarea>
      <br>
      <input type= 'submit'>
    </form>
  </body>
</html>
    """

lowercase_string = string.ascii_lowercase
uppercase_string = string.ascii_uppercase

lowercase_list = []
uppercase_list = []

for e in lowercase_string:
    lowercase_list.append(e)

for e in uppercase_string:
    uppercase_list.append(e)

def rot13(x):
    if x in lowercase_list:
        return lowercase_list[(lowercase_list.index(x) + 13) % len(lowercase_list)]
    if x in uppercase_list:
        return uppercase_list[(uppercase_list.index(x) + 13) % len(uppercase_list)]
    else:
        return x

def rotstring(x):
    for e in range(0, len(x)):
        x = x[:e] + rot13(x[e]) + x[e+1:]

    return x

def escape_html(s):
    return cgi.escape(s, quote = True)

class MainPage(webapp2.RequestHandler):
    def write_form(self, rot=''):
        self.response.out.write(form % escape_html(rot))

    def get(self):
        self.write_form()

    def post(self):
        self.write_form(rotstring(self.request.get('text')))

app = webapp2.WSGIApplication([ ('/', MainPage)],
                                debug=True)
