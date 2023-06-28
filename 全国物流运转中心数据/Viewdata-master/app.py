from flask import Flask, render_template
import viewdata.tools as tool
from flask import jsonify, json
from flask_cors import CORS

app = Flask(__name__, static_folder='', static_url_path='')
CORS(app, resources='/*')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRNT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template("index3.html")


@app.route("/js/data-1576140623415-kSH4vRQ1.json", methods=['GET'])
def index3_json_get():
    with open(r"D:\Projects\PycharmProjects\可视化大屏\Viewdata-master\statics\js\data-1576140623415-kSH4vRQ1.json", encoding='utf-8') as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)

@app.route("/index3/char1_2")
def task21():
    data = tool.index3_char1_2_data()
    return jsonify({"char1_name":data[0],"char1_value":data[1],"char2_name":data[2],"char2_value":data[3]})

@app.route("/index3/char3")
def task22():
    data = tool.index3_char3_data()
    return jsonify({"province":data[0],"damaged":data[1],"lost":data[2],"rejects":data[3],"not_signed":data[4]})

@app.route("/index3/maps")
def task23():
    data = tool.index3_maps_data()
    return jsonify(data)

@app.route("/index3/chart5")
def task24():
    data = tool.index3_chart5_data()
    return jsonify({"sex_data":data[0],"line_old":data[1],"line_value":data[2],"edu_data":data[3]})

@app.route("/index3/chart6")
def task25():
    data = tool.index3_chart6_data()
    return jsonify({"data1":data[0],"data2":data[1]})

@app.route("/index3/chart8")
def task26():
    data = tool.index3_chart8_data()
    return jsonify(data)

if __name__ == '__main__':
    app.debug = True
    app.run()