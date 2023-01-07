from flask import Flask, jsonify, request
import proxy

app = Flask(__name__)

@app.route('/search')
def search():
    html = proxy.make_req_requests(request.args.get("q"), "EN", res_number=40)
    return jsonify({"status": 1, "data": html})