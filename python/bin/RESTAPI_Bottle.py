import bottle

app = bottle.Bottle()


# API - 1 -> IP
# api1 = http://127.0.0.1:8080/ip
@app.route('/ip', method='GET')
def api_ip():
    import sqlite3
    con = sqlite3.connect('myDB.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT IP FROM LOGDATA")
    result = cur.fetchall()
    # return str(result)
    result = [i[0] for i in result]
    D = {k: v for k, v in enumerate(result)}
    return D


# API2 - http://127.0.0.1:8080/emp
@app.route('/emp', method='post')
def empDetails():
    details = bottle.request.params
    details = dict(details)
    return details


@app.route('/json')
def fromJson():
    F = open('myData.json', 'w')
    D = {"course": "python", "loc": "blr"}
    import json
    json.dump(D, F)
    F.close()
    F = open('myData.json')
    r = json.load(F)
    F.close()
    return r


app.run(host='127.0.0.1', port=8080)
