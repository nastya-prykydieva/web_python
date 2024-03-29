import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()

surname = form.getfirst("surname", "–")
name = form.getfirst("name", "–")
group = form.getfirst("group", "–")

surname = html.escape(surname)
name = html.escape(name)
group = html.escape(group)

done = form.getvalue("done", "–")

disciplines = ["Вебпрограмування мовою Python", "Економіка програмного забезпечення",
               "Комп'ютерна графіка", "Основи штучного інтелекту", "Машинне навчання"]
selected = []

for discipline in disciplines:
    if discipline in form:
        selected.append(discipline)

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
if "count" in cookie:
    count = int(cookie["count"].value) + 1
else:
    count = 1

print(f"Set-cookie: count={count};")
print("Content-type:text/html\r\n\r\n")

template_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обробка форми</title>
</head>
<body>
    <h3>Ваші відповіді</h3>
    Прізвище: {surname}<br><br>
    Ім'я: {name}<br><br>
    Група: {group}<br><br>
    Чи завершений Ваш вибір навчальних дисциплін? {done}<br><br>
    Обрані Вами дисципліни:<br> – {"<br> – ".join(selected)}<br><br>
    Кількість заповнених форм: {count}<br><br>
</body>
</html>
"""
print(template_html)
