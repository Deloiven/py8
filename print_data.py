from import_proces import data_access_read, data_access_write


def print_data():
    data = data_access_read()
   

    for i in range(len(data)):
        for j in data[i]:
            print ('{0:20}'.format(j), end='|')
        print()


if __name__ == '__main__':
    data_access_write ([['id', 'full_name', 'date_birth', 'telephone'], ['5', '6', '7', '8'], ['6', 'Bosh', '11.09.1235', '+78009007080']])
    print_data()