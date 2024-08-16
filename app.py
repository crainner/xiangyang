from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# 定义数据库路径
DB_PATH = 'directories.db'

# 定义搜索页面的模板
HTML_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Directory Search</title>
  </head>
  <body>
    <h1>Directory Search</h1>
    <form method="get" action="/">
      <input type="text" name="query" placeholder="Search..." required>
      <button type="submit">Search</button>
    </form>
    <ul>
      {% for result in results %}
        <li>{{ result }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
'''

@app.route('/')
def index():
    query = request.args.get('query', '')
    results = []

    if query:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('SELECT directory FROM directories WHERE directory LIKE ?', (f'%{query}%',))
        results = [row[0] for row in cursor.fetchall()]
        conn.close()

    return render_template_string(HTML_TEMPLATE, results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
