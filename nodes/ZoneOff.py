
import polyinterface
LOGGER = polyinterface.LOGGER

class ZoneOffNode(polyinterface.Node):

    def __init__(self, controller, parent_address, address, name):
        LOGGER.debug("ZoneOff:__init__: {} {}".format(address,name))
        super(ZoneOffNode, self).__init__(controller, parent_address, address, name)

    def start(self):
        self.l_debug('start','')
        super(ZoneOffNode, self).start()

    def l_info(self, name, string):
        LOGGER.info("%s:%s:%s: %s" %  (self.id,self.name,name,string))

    def l_error(self, name, string):
        LOGGER.error("%s:%s:%s: %s" % (self.id,self.name,name,string))

    def l_warning(self, name, string):
        LOGGER.warning("%s:%s:%s: %s" % (self.id,self.name,name,string))

    def l_debug(self, name, string):
        LOGGER.debug("%s:%s:%s: %s" % (self.id,self.name,name,string))

    "Hints See: https://github.com/UniversalDevicesInc/hints"
    hint = [1,2,3,4]
    drivers = [
        # physical status
        {'driver': 'ST',  'value': 0, 'uom': 25},
        # logical status
        {'driver': 'GV0', 'value': 0, 'uom': 25},
    ]
    id = 'zoneoff'
    commands = {
    }
