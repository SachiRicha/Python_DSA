num = int(input("Enter any number: "))
print("Enter any choice: 1. ON the bit  2. OFF the bit  3. Toggle the bit")
ch = int(input("Enter any choice: "))
bitToBeManipulatedIs = int(input("Enter the bit you want to manipulate: "))
bitMask = 1<<bitToBeManipulatedIs-1
if ch == 1:
    print(f"After ON the {bitToBeManipulatedIs} bit: ",num | bitMask)
elif ch == 2:
    print(f"After OFF the {bitToBeManipulatedIs} bit: ",num & ~(bitMask))
elif ch == 3:
    print(f"After toggling the {bitToBeManipulatedIs} bit: ",num ^ bitMask)


