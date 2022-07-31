import sys
from gitp.gitp import Gitp

program = Gitp()
program.run(sys.argv[0], sys.argv[1:])
