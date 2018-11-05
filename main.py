from setup import Setup
from modules.servidor import servidor

if __name__ == "__main__":
    print "Starting the configuration"
    Config = Setup()
    print "Trying to run server..."
    host = Config.host
    port = Config.port
    del Config
    print "Se ejecuto el servidor en: %s:%s" % (host, port)
    servidor(host, port)