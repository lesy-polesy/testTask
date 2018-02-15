import json
import settings as s
from bottle import route, run, template, get, post, static_file
from bottle import response, request, error, install
from bottle_sqlite import SQLitePlugin

sqlite = SQLitePlugin(dbfile=s.mydb_name)
install(sqlite)

@route('/test')
def test():
    return static_file('test.html',root=s.myviews_path)

@get('/api/<id>')
def data(id,db):
    result = db.execute("SELECT apid,fname,lname,createdtime FROM dataset WHERE apid = ? AND createdtime > datetime(\'now\', \'-1 hour\',\'localtime\')", (id,)).fetchall()
    if result:
        return template(('%s/make_table' % s.myviews_path), id=str(id), rows=result)
    return ('<h3>За последний час по id = ' + str(id) + ' данных нет</h3>')

@post('/api/<id>')
def setData(id,db):
    firstname = request.json['first_name']
    lastname = request.json['last_name']
    if(firstname == "" or lastname == ""):
        response.status = 400  # ошибка
        response.content_type = 'application/json'
        return json.dumps({'error': 'Неполные данные ' + str(id)})
    else:
        db.execute('INSERT INTO dataset(apid,fname,lname) VALUES(?,?,?)',(id,firstname,lastname))
    response.status=200
    return json.dumps({'ok':'вроде проскочили'})


@error(500)
def error500(error):
    return json.dumps({"error":'<p>Internal server error:</p>'+str(error.exception)})

run(host=s.myhost, port=s.myport, debug=True)
