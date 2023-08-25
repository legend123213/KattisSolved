data = [i for i in input().split()]
key = [i for i in input().split()]
keyPointer = [0]*len(key)
pointer = 0
for j in range(len(key)):
    for i in range(pointer, len(key)-2):
        print("key:{},pointer:{}".format(key[pointer], key[i+1]))
        if key[pointer] == key[i+1]:
            keyPointer[i+1] = pointer+1
    pointer += 1

key.insert(0, 0)
keyPointer.insert(0, 0)
output = {"answer": 0, "indexes": []}
pointer = 0
for i in range(len(data)+1):
    if pointer < len(key)-1:
        if key[pointer+1] == data[i]:
            pointer += 1
        else:
            pointer = keyPointer[pointer]
    elif pointer >= len(key)-1:
        output["answer"] += 1
        output['indexes'].append([i-len(key)+1, i])
        pointer = 0
    print("index: {} , pointer:{}".format(i, pointer))
