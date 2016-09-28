import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f7d8b2d7'.decode('hex')
P2P_PORT = 52399
ADDRESS_VERSION = 40
RPC_PORT = 52398
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'harambecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 13.46*100000000 #gross hack for now
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 90 # s
SYMBOL = 'HMBC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Harambecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Harambecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.harambecoin'), 'harambecoin.conf')
BLOCK_EXPLORER_URL_PREFIX = ''
ADDRESS_EXPLORER_URL_PREFIX = ''
TX_EXPLORER_URL_PREFIX = ''
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
