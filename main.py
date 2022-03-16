
def create_list_files():
    list = ['1.txt', '2.txt', '3.txt']
    return list

if __name__ == '__main__':
    list_files = create_list_files()
    # print(list_files)
    quantity = []
    for file in list_files:
        with open(file, encoding='utf-8') as f:
            quantity.append(f.read().count('\n') + 1)
    # print(quantity)
    new_list = list(zip(list_files, quantity))
    # print(new_list)
    new_list = sorted(new_list, key=lambda x: x[1])
    # print(new_list)
    f = open("result.txt", "w")
    f.close()
    for f in new_list:
        with open(f[0], encoding='utf-8') as old_file:
            with open("result.txt", 'a') as new_file:
                new_file.write(f[0] + '\n')
                new_file.write(str(f[1])+'\n')
                new_file.write(old_file.read() + '\n')
