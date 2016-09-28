from p2pool.bitcoin import networks

PARENT = networks.nets['harambecoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '8f174d986b027d27'.decode('hex')
P2P_PORT = 54000
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 53000
BOOTSTRAP_ADDRS = 'catillack.com'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-hmbc'
VERSION_CHECK = lambda v: None if 100001 <= v else 'Harambecoin version too old. Upgrade to 1.0.0.2 newer!'
VERSION_WARNING = lambda v: None
