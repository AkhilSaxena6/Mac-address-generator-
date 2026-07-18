import random

def macadd():
    mac_add = ""
    charset = "1234567890ABCDEF"
    for i in range(1,13):
        mac_add = mac_add + random.choice(charset)
        
        if (i%2==0 and i!=12):
            mac_add = mac_add + ":"
      
        if i==12:
            print(mac_add)
        else:
            pass
            
macadd()