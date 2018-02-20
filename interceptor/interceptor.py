import StringIO
import email
import socket

import pride.components.network


class Connecting_Socket(pride.components.network.Tcp_Client):
    
    defaults = {"request_data" : ''}
    required_attributes = ("request_data", )
    
    def on_connect(self):
        super(Connecting_Socket, self).on_connect()
        self.send(self.request_data)
        #self.alert("Sent:\n{}".format(self.request_data))
        self.alert("Connected as {}".format(self.sockname))
        
    def recv(self):
        data = super(Connecting_Socket, self).recv()
        #self.alert("Received:\n{}".format(data))
        self.delete()
        
        
class Interceptor_Proxy_Socket(pride.components.network.Tcp_Socket):
    
    defaults = {"outgoing_connection" : Connecting_Socket}
    
    def recv(self):        
      #  assert self.sockname != ("127.0.0.1", 8080)
        assert self.sockname != self.parent.sockname
        raw_data = super(Interceptor_Proxy_Socket, self).recv()
        request_line, header_data = raw_data.split('\r\n', 1)
        _stringio = StringIO.StringIO(header_data)
        headers = email.message_from_file(_stringio)
        try:
            host, port = headers["Host"].split(':', 1)
        except ValueError:
            print "ValueError", headers["Host"]
            host = headers["Host"]
            port = 80
        ip = socket.gethostbyname(host)        
        assert ip != "127.0.0.1"
        assert ip != "localhost"
        connection = self.create(self.outgoing_connection, ip=ip, port=int(port), request_data=raw_data)
                
    
class Interceptor_Proxy_Server(pride.components.network.Server):
    
    defaults = {"port" : 8080, "Tcp_Socket_type" : Interceptor_Proxy_Socket}
    
    def delete(self):
        self.alert("Deleting")
        super(Interceptor_Proxy_Server, self).delete()
        
        
def unit_test():
    print "Creating server..."
    server = pride.objects["/Python"].create(Interceptor_Proxy_Server)
    server.alert("Server created")
    
if __name__ == "__main__":
    unit_test()
    