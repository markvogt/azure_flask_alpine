from flask import Flask
import os
import ldap
import ldap.modlist as modlist
app = Flask(__name__)

@app.route("/")
def hello():
    output = "hello world MV! <br/>"
    for param in os.environ.keys():
        output+="%20s %s <br/>" % (param,os.environ[param])
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
