#-*- coding: utf-8 -*-
import uuid
def get__mac_address():
    mac=uuid.UUID(int = uuid.getnode ()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
print get__mac_address()