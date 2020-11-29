f = open('station_coord.txt', 'r', encoding='utf-8')
fw = open('refined_station_coord.txt', 'w', encoding='utf-8')
lines = f.readlines()
coords = []
name = []
al = []
for l in lines:
    l = l.split(',')
    station_name = l[3][l[3].find(':')+1:]
    station_x = l[9][l[9].find('lat')+5:]
    station_y = l[10][l[10].find('lon')+5:].strip('}{')
    al.append([station_name, station_x, station_y])
    name.append(station_name)
    coords.append([station_x,station_y])
al = list(set([tuple(set(item)) for item in al]))
for a in al:
    a = sorted(list(a))
    fw.write(a[0][1:len(a[0])-1] + ',' + a[2] + ',' + a[1] + '\n')
fw.close()
