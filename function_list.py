

import idc
import idaapi 
import idautils

#print("Hello")

# Could log to an external log file 

print("FUNCTIONS:")
count = 0
for ea in idautils.Functions():
    count+=1
    #print("{}, {}".format(ea, idc.get_func_name(ea)))
    print(f"FUNCTION, {hex(ea)}, {idc.get_func_name(ea)}")
print("FUNCTIONS count :" + str(count))

qexit(0)
