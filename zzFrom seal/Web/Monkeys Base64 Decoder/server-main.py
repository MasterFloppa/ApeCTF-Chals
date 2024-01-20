from flask import Flask, render_template, render_template_string, request
import base64
app = Flask(__name__, template_folder='templates')
app.secret_key='ApeCTF{sst1_t1m3_w00h00}'

@app.route('/', methods=['GET'])
def main():
    b64=request.args.get('b64')
    if b64:
        try:
            data = base64.b64decode(b64).decode()
        except Exception as e:
            print(e)
            data = "Invalid base64 data!"
        return render_template_string(data)
    else:
        return render_template('index.html')

 
if __name__ == '__main__':
    app.run()
