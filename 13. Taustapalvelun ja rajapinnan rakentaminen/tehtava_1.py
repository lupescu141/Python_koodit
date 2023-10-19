from flask import Flask, request

app = Flask(__name__)


@app.route('/alkuluku/<numero>')
def alkuluku(numero):

    while True:
        args = request.args
        userinput = numero

        i = int(userinput)
        jaolliset_kerrat = 0

        while i > 0:

            if float(userinput) % i == 0:
                jaolliset_kerrat += 1

            i -= 1

        if jaolliset_kerrat != 2:
            istrue = True
            vastaus = {"Number": userinput,
                       "IsPrime": istrue}

            return vastaus

        else:
            return f"Number:{userinput} isPrime:tue"


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)