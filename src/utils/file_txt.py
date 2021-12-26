def read_file(fp):
    with open(fp, 'r') as f:
        data = f.readline()

    infor = data.split('|')
    return infor