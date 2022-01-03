cargo = [40, 20, 4, 5, 30, 8, 2, 7, 3, 19, 32, 40, 20, 35, 15, 32, 9]
cargo.sort()
cargo.reverse()

print("The cargo list is:", cargo)

boxCopacity = 90
box = []
i = 0

while i < len(cargo) and (boxCopacity - sum(box) >= min(cargo)):
    if (boxCopacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i += 1

print("The collected items sum is:", sum(box))
print("The elements box:", box)