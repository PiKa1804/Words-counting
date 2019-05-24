from flask import Flask, render_template, request
import urllib.robotparser
import Function

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/',methods = ['POST'])
def result():
    text = request.form['text']
    URL_BASE='http://'+text
    result=dict()

    try: 
            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(urllib.parse.urljoin(URL_BASE, '/robots.txt'))
            parser.read()
            url2 = urllib.parse.urljoin(URL_BASE, '/')
            if parser.can_fetch('*', url2)==True:
                print("Ok")
                result=Function.Execute(URL_BASE)
                if result=={}:
                    return render_template('start.html',tekst=result,header='There are NO results for '+text)
            
            else:
                print("Robots.txt")
            return render_template('start.html',tekst=result,header='These are results for '+text)
    except Exception as e:
            print("Can't connect")
            return render_template('start.html',tekst={},header='Can\'t connect with '+text)
    
 
@app.errorhandler(404)   
def not_found_error(error):
    return render_template('404.html'),404


if __name__ == '__main__':
    app.run() 
