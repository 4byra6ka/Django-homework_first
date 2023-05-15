from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_post(self):
        """ Метод для обработки входящих POST-запросов """
        c_len = int(self.headers.get('Content-Length'))
        client_data = self.rfile.read(c_len)
        client_data = client_data.decode()
        print(client_data)
        self.send_response(201)
        self.send_header("Content-type", "application/text")
        self.end_headers()
        self.wfile.write(bytes("Запрос обработан", "utf-8"))

    def do_get(self):
        """ Метод для обработки входящих GET-запросов """
        text = 'Hello, World wide web!'
        self.send_response(200)
        self.send_header("Content-type", "application/text")
        self.end_headers()
        self.wfile.write(bytes(text, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
