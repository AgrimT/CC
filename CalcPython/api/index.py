from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        html = """
        <html>

        <head>
            <title>Python Calculator</title>

            <style>

                body{
                    font-family: Arial;
                    text-align: center;
                    background: #f2f2f2;
                    padding-top: 100px;
                }

                .box{
                    background: white;
                    width: 350px;
                    margin: auto;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px gray;
                }

                input{
                    width: 80%;
                    padding: 10px;
                    margin: 10px;
                    font-size: 16px;
                }

                button{
                    padding: 10px 15px;
                    margin: 5px;
                    font-size: 15px;
                    cursor: pointer;
                }

            </style>
        </head>

        <body>

            <div class="box">

                <h1>Calculator</h1>

                <input type="number" id="n1" placeholder="First Number">

                <input type="number" id="n2" placeholder="Second Number">

                <br><br>

                <button onclick="calculate('add')">Add</button>

                <button onclick="calculate('sub')">Subtract</button>

                <button onclick="calculate('mul')">Multiply</button>

                <button onclick="calculate('div')">Divide</button>

                <h2 id="result"></h2>

            </div>

            <script>

                function calculate(type){

                    let a = Number(document.getElementById("n1").value);

                    let b = Number(document.getElementById("n2").value);

                    let result = 0;

                    if(type == "add"){
                        result = a + b;
                    }

                    else if(type == "sub"){
                        result = a - b;
                    }

                    else if(type == "mul"){
                        result = a * b;
                    }

                    else if(type == "div"){
                        result = a / b;
                    }

                    document.getElementById("result").innerHTML =
                        "Result = " + result;
                }

            </script>

        </body>

        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(html.encode())
