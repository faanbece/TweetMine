from tweepy import StreamListener
import json, time, sys

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer'):
        self.api = api or API()
        self.counter = 0
        self.fprefix = fprefix
        self.output  = open(fprefix + ' - '
                            + time.strftime('%Y_%m_%d %H:%M:%S') + '.data', 'a')
        #self.output  = open(fprefix, 'a')
        #self.delout  = open('delete.txt', 'a+')

    def on_data(self, data):
        print "Data : " + str(data)
        if  'in_reply_to_status' in data:
            self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print warning['message']
            return false

    def on_status(self, status):
        print "Status : " + str(data)
        self.output.write(status + "\n")

        self.counter += 1

        if self.counter >= 20000:
            self.output.close()
            self.output = open(self.fprefix + ' - '
                                + time.strftime('%Y_%m_%d %H:%M:%S') + '.data', 'a')
            self.counter = 0

        return

    def on_delete(self, status_id, user_id):
        #self.delout.write( str(status_id) + "\n")
        print ""
        return

    def on_limit(self, track):
        sys.stderr.write(track + "\n")
        return

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return
