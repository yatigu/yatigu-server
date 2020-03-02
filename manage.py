from settings.settings import manager, app, HOST_ADDR, PORT_NUM, MODE
from waitress import serve
from paste.translogger import TransLogger

if __name__ == '__main__':
    if MODE == 'DEV':
            manager.run()
    elif MODE == 'RUN':
            serve(TransLogger(app, setup_console_handler=True),
                  host=HOST_ADDR, port=PORT_NUM)


