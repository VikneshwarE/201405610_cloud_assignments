from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel,info
from mininet.util import dumpNodeConnections
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.topo import Topo
def emptyNet() :
        l=[int(i) for i in raw_input().split()]
        X=l[0]
        Y=l[1]
        net=Mininet(controller=Controller,link=TCLink)
        net.addController('c0')
        info('Adding Switches\n')
        S=[]
        for i in range(Y) :
                switchname='S'+str(i)
                S.append(net.addSwitch(switchname))
        k=0
        H=[]
        info('Adding Hosts\n')
	 for i in range(Y) :
                for j in range(X) :
                        if k%2 == 0 :
                                hostname='H'+str(k)
                                ipaddr='10.0.0.'+str(k+1)+'/24'
                                H.append(net.addHost(hostname,ip=ipaddr))        
                        else :
                                hostname='H'+str(k)
                                ipaddr='10.0.1.'+str(k+1)+'/24'
                                H.append(net.addHost(hostname,ip=ipaddr))
                        k=k+1
        k=0
        for i in range(Y) :
                for j in range(X) :
                        if k%2 == 0 :
                                net.addLink(H[k],S[i],bw=2)
                        else :
                                net.addLink(H[k],S[i],bw=1)
                        k=k+1
        for i in range(Y-1) :
                net.addLink(S[i],S[i+1],bw=2)
	 net.start()
        CLI(net)
        net.stop()


if __name__ == '__main__' :
        setLogLevel('info')
        emptyNet()

