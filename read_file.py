def read_file(path):
    res = []
    with open(path, 'r') as f:
        for line in f:
            linea = line.strip().split(';')
            c = []
            if 'num_cells' in line:
                num = line.split('=')[1]
                res.append(int(num))
            else:
                for l in linea:
                    coordenadas = l.split(',')
                    c.append((int(coordenadas[0]), int(coordenadas[1])))
                res.append(c)
    return res