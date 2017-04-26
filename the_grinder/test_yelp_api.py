from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest

test1 = Test(1, "Request resource")
request1 = HTTPRequest()
test1.record(request1)
 
class TestRunner:
    def __call__(self):
        # result = request1.GET("http://localhost:7001/")
 
        # result is a HTTPClient.HTTPResult. We get the message body
        # using the getText() method.
        # writeToFile(result.text)
        print("HELLO WORLD")

def setup_creds():
	with io.open('config_secret.json') as cred:
		creds = json.load(cred)
		return creds


creds = setup_creds()
auth = OAuth1(creds['consumer_key'], creds['consumer_secret'], creds['token'], creds['token_secret'])
 
# Utility method that writes the given string to a uniquely named file.
# def writeToFile(text):
#     filename = "%s-page-%d.html" % (grinder.processName, grinder.runNumber)
 
#     file = open(filename, "w")
#     print >> file, text
#     file.close()