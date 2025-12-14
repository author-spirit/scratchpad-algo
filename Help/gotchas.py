"""
Ref: https://docs.python-guide.org/writing/gotchas/
"""

# BTS, it creates list only once, add used on next call
# To avoid this mark the arr to None and create new list on each run
def mutable_default_args():
    def push(val, arr = []):
        arr.append(val)
        return arr
    
    def push2(val, arr = None):
        if arr is None:
            arr = []

        arr.append(val)
        return arr

    print(push(1))
    print(push(2))
    
    print("After Fix")
    print(push2(1))
    print(push2(2))

mutable_default_args()

# Iterating while mutating, goes infinite
# use [:] or copy
"""
name = ['name', 'age', 'place']
for nm in name:
    print(nm)
    name.append(nm)
"""
name = ['name', 'age']
for nm in name.copy():
    print(nm)
    name.append(nm)
print("Original Modified: ", name)


# Use hashlib for hashing

import hashlib
original_string = 'hello debbie, meet me at north-east'
print(hashlib.blake2b(b'hello', digest_size=16).hexdigest())
print()


# list * n copies references
arr = [[1,2,3]] * 3
arr[0][0] = 1.2
print("Refer: ", arr)
arr = [[1,2,3] for _ in range(3)]
arr[0][0] = 1.2
print(arr)

# Shallow copy, if any modification to original will updates in copied version too
# use deepcopy
dup = arr.copy()
arr[0][0] = 2.5
print(dup) # modifies the duplicate too

import copy
dupz = copy.deepcopy(arr)
arr[0][0] = 0.7
print(dupz) # 0.7 shouldn't apply for dupz, its now 2.5


import decimal
print(0.1 + 0.2 == 0.3, decimal.Decimal(0.1 + 0.2), decimal.Decimal(0.3))
