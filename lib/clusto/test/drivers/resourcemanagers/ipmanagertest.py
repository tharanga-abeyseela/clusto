
import clusto
from clusto.test import testbase

from clusto.drivers import IPManager, BasicServer, ResourceTypeException

class IPManagerTest(testbase.ClustoTestBase):

    def data(self):

	ip1 = IPManager('a1', gateway='192.168.1.1', netmask='255.255.255.0',
			baseip='192.168.1.0')

	ip2 = IPManager('b1', gateway='10.0.128.1', netmask='255.255.252.0',
			baseip='10.0.128.0')

	s = BasicServer('s1')

    def testBadIPAllocation(self):
	
	ip1, ip2, s1 = map(clusto.getByName, ['a1', 'b1', 's1'])

	self.assertRaises(ResourceTypeException, ip1.allocate, s1, '10.2.3.4')



