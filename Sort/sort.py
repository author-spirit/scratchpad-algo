elem = [800, 100, 120, 650, 230]
print("Original", elem)


n = len(elem)
for i in range(n):
    hold_index = i
    for j in range(i+1, n):
        print(j)
        if elem[j] < elem[hold_index]:
            hold_index = j

    if i != hold_index:
        elem[i], elem[hold_index] = elem[hold_index], elem[i]

print("Sorted", elem)
