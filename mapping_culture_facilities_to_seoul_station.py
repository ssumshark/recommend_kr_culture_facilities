import json
import logging
import os
import sys
import utils

def main(culture_json, station_geo_txt, output):
    with open(culture_json, "r") as st_json:
        culture = json.load(st_json)
    raw_culture_data = culture['DATA']
    culture_all_data = []
    codes = []
    for line in raw_culture_data:
        x = line['x_coord']
        y = line['y_coord']
        code = line['codename']
        codes.append(code)
        culture_all_data.append([code, x, y])
    codes = list(set(codes)) # remove redundant field

    station_coord = open(station_geo_txt, 'r', encoding='utf-8')
    station_info = station_coord.readlines()
    refined_station = []
    stations = []
    for s in station_info:
        s_parse = s.strip('\n').split(',')
        stations.append(s_parse[0])
        refined_station.append(s_parse)
    station_all_distance = []
    stations = list(set(stations)) # remove redudant station
    output_dict = {x : {y : 0 for y in codes} for x in stations}
    for a in culture_all_data:
        a[1], a[2] = a[1].replace(' ', ''), a[2].replace(' ','')
        for r in refined_station:
            if utils.isFloat(a[1]) and utils.isFloat(a[2]) and utils.isFloat(r[1]) and utils.isFloat(r[2]):
                distance = utils.get_uclidean_distance(src=a, tar=r)
                station_all_distance.append([r[0], a[0], distance])
        valid = [d for d in station_all_distance if len(d) == 3 and utils.isFloat(d[2])] # prune invalid data
        if len(valid) == 0: continue
        sorted_valid_data = sorted(valid_data, key=lambda l:l[2], reverse=False)[0]
        output_dict[sorted_valid_data[0]][sorted_valid_data[1]] += 1
        station_all_distance = []

    a_logger, b = utils.init_logger('station_add_culture_facilities', output_path)           
    for station in ouput_dict:
        station_coord = [[r[1], r[2]] for r in refined_station if r[0] == station] # mapping station name to station geo
        assert len(station_coord) == 1 or len(station_coord) == 0
        v = final_dict[station]
        total = v['도서관'] + v['박물관/기념관'] + v['문화원'] +  v['미술관'] + v['공연장'] + v['문화예술회관'] + v['기타']
        output_format = {"station_name":station, "library":v['도서관'], "museum":v['박물관/기념관'], "culture_center":v['문화원'], "art_gallery":v['미술관'], "stadium":v['공연장'], 'arts_center':v['문화예술회관'], 'etc':v['기타'], 'total_sum':total, 'station_geo': {"lat":station_coord[0][0],"lon":station_coord[0][1]}}
        utils.write_logger(a_lgger, output_format)
        station_coord = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Seoul Metro for the number of curture facilities from 2020 Seoul Culture Data')
    parser.add_argument('--culture_json', required=True, type=str, help='raw culture facilities data path')
    parser.add_argument('--station_geo_txt', required=True, type=str, help='station geo txt data path')
    parser.add_argument('--output', required=True, type=str, help='enter the output path')
    args = parser.parse_args()
    main(args.culture_json, args.station_geo_txt, args.output)       
