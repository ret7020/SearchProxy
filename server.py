from flask import Flask, request, jsonify
import proxy

class ProxyAPI:
    def __init__(self, name, host='0.0.0.0', port='8080'):
        self.app = Flask(name)
        self.host = host
        self.port = port
    
        @self.app.route('/')
        def __index():
            return self.index()
        
        @self.app.route('/search')
        def __search():
            return self.seacrh()
    
    def index(self):
        return "Search Proxy for Noogle serch engine!"

    def seacrh(self):
        return jsonify({"status": True, "data": proxy.make_req_requests(request.args.get("q"), "EN", 40)})

    
    def run(self):
        self.app.run(host=self.host, port=self.port)

if __name__ == "__main__":
    web = ProxyAPI(__name__)
    web.run()
