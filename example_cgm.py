from brian2 import *
from brian2lems.lemsexport import all_devices

set_device('lemsdevice')

n = 100
duration = 1*second
tau = 10*ms
Ek = 12
El = 30*mV
eqs = '''
dv/dt = (v0 - v) / tau : volt (unless refractory)
v0 : volt
'''
group = NeuronGroup(n, eqs, threshold='v > 10*mV', reset='v = 0*mV',
                    refractory=5*ms, method='linear')
group.v = 0*mV
group.v0 = '20*mV * i / (N-1)'

monitor = SpikeMonitor(group, record=[3,33])

run(duration/2)

device.build("ifcgmtest.xml")
