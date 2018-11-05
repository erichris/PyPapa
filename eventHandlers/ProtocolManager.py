from eventHandlers.SubProtocol0 import subProtocolHandler0
from eventHandlers.SubProtocol1 import subProtocolHandler1
from eventHandlers.SubProtocol2 import subProtocolHandler2
from eventHandlers.SubProtocol3 import subProtocolHandler3
from eventHandlers.SubProtocol4 import subProtocolHandler4
from eventHandlers.SubProtocol5 import subProtocolHandler5
from eventHandlers.SubProtocol6 import subProtocolHandler6
from eventHandlers.SubProtocol7 import subProtocolHandler7
from eventHandlers.SubProtocol8 import subProtocolHandler8
from eventHandlers.SubProtocol9 import subProtocolHandler9
from eventHandlers.SubProtocol10 import subProtocolHandler10
from eventHandlers.SubProtocol11 import subProtocolHandler11

def protocolHandler(Config, package):
    if(package['Protocol'] == '0'): #Login/Register
        return subProtocolHandler0(Config, package);
    elif(package['Protocol'] == '1'): #Data
        return subProtocolHandler1(Config, package);
    elif(package['Protocol'] == '2'): #Comida
        return subProtocolHandler2(Config, package);
    elif(package['Protocol'] == '3'): #Desayunos
        return subProtocolHandler3(Config, package);
    elif(package['Protocol'] == '4'): #Pedidos
        return subProtocolHandler4(Config, package);
    elif(package['Protocol'] == '5'): #Pedidos
        return subProtocolHandler5(Config, package);
    elif(package['Protocol'] == '6'): #Pedidos
        return subProtocolHandler6(Config, package);
    elif(package['Protocol'] == '7'): #OrdenarChecar
        return subProtocolHandler7(Config, package);
    elif(package['Protocol'] == '8'): #Map
        return subProtocolHandler8(Config, package);
    elif(package['Protocol'] == '9'): #Map
        return subProtocolHandler9(Config, package);
    elif(package['Protocol'] == '10'): #Map
        return subProtocolHandler10(Config, package);
    elif(package['Protocol'] == '11'): #Map
        return subProtocolHandler11(Config, package);