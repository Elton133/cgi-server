# print("Content-Type: text/html\n")
# print("<html><body>")
# print("<h1>Hello from CGI!</h1>")
# print("</body></html>")


import cgi

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")

print("<html><body>")
print(f"<h1>Hello, {name}!</h1>")
print(f"<p>Your email is {email}</p>")
print("</body></html>")