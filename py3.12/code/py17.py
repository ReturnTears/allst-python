# break
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(f"inner loop : {j}")
    print(f"outer loop : {i}")

# continue
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"inner loop : {j}")
    print(f"outer loop : {i}")