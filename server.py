import os

import tornado.ioloop
import tornado.web
import tornado.autoreload


class MainHandler(tornado.web.RequestHandler):
    def prepare(self):
        print("Preparing!!")

    def get(self):
        self.write("Hello, world")

    def on_finish(self):
        print("Finished!")


application = tornado.web.Application([
    (r"/", MainHandler),
])


def setup_dev_server():
    this_dir = os.path.dirname(os.path.realpath(__file__))

    tornado.autoreload.start()
    for dir, _, files in os.walk(this_dir):
        [tornado.autoreload.watch(dir + '/' + f)
         for f in files if not f.startswith('.')]


if __name__ == "__main__":
    if os.environ.get('C10K_ENV') == 'develop':
        print('Running dev server!')
        setup_dev_server()

    port = 5000
    application.listen(port)
    print(f'Listening on port {port}!')
    tornado.ioloop.IOLoop.instance().start()
