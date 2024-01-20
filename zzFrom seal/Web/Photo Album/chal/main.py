
from flask import Flask, render_template, request, send_file
import io
app = Flask(__name__, template_folder='templates')
 
 
@app.route('/view', methods=['GET'])
def view():
    file=request.args.get('file')
    if file:
        with open(f'pics/{file}','rb') as f:
            return send_file(
                    io.BytesIO(f.read()),
                    mimetype='image/jpeg',
                    as_attachment=True,
                    download_name=f'{file}')
        return 'No file data!'
    else:
        return 'No file param!'
 
 
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

 
if __name__ == '__main__':
    app.run()
