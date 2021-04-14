import os
import pages
import server



pages.install()
server.run(int(os.environ.get("PORT",0)))
