import logging
import os
import sys
import argparse
import time
import utils


def main(input_file, output_path):
    os.makedirs(output_path, exist_ok=True)
    txt_file = input_file
    f = open(txt_file, 'r', encoding='utf-8')
    txt_info = f.readlines()
    txt_info = txt_info[1:] # remove first descriptions line
    start_data, end_data = txt_info[:int(len(txt_info)/2)], txt_info[int(len(txt_info)/2):]

    # find month start step
    start_month_idx = []
    for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
        for idx, end_data_line in enumerate(end_data):
            month = int(end_data[idx].replace('\n', '').split('\t')[0].split('.')[1])
            if month == i:
                start_month_idx.append(idx)
                break
     
    assert len(start_data) == len(end_data) # check whether two data length is same.

    for idx in (range(len(start_data))):
        st_t = time.time()
        flag = True
        start_split_data = start_data[idx].replace('\n', '').split('\t')
        # if prev data and next data is different, generate other log file.
        if idx != 0 and start_data[idx - 1].replace('\n', '').split('\t')[0] != start_split_data[0]:
            a_logger, output_file_handler = utils.init_logger(name=start_split_data[0], output_path=output_path)
        elif idx == 0:
            a_logger, output_file_handler = utils.init_logger(name=start_split_data[0], output_path=output_path)

        # Search End Data more Fastly by loading index start checkpoints
        start_data_month = int(start_data[idx].replace('\n', '').split('\t')[0].split('.')[1]) - 1
        for end_data_ckpt_idx in end_data[start_month_idx[start_data_month]:]:
            end_split_data = end_data_ckpt_idx.replace('\n', '').split('\t')
            if end_split_data[0] == start_split_data[0] and end_split_data[1] == start_split_data[1]:
                target_end_data = end_split_data
                flag = False
                break
        if flag: assert False, 'data is mismatching between start data and end data !'
        assert start_split_data[0] == end_split_data[0] and start_split_data[1] == end_split_data[1], 'two data is not the same!'
        
        # Split Day to Hour
        for i in range(4,len(start_split_data)):
            if i != len(start_split_data) - 1:
                day = start_split_data[0].replace(".", "-") + "T" + str(i+1).zfill(2) + ":00.000Z"
            else:
                day = start_split_data[0].replace(".", "-") + "T" + "00:00.000Z"
            # using field 
            line_num = '-'
            line_num_en = '-'
            station_name = start_split_data[2][:start_split_data[2].find('(')]
            people_in = int(start_split_data[i].replace(',', ''))
            people_out = int(target_end_data[i].replace(',',''))

            # Change data to output format
            output_format = {"time_slot":day, "line_num":line_num, "line_num_en":line_num_en, "station_name":station_name, "people_in":people_in, "people_out":people_out}
            utils.write_logger(a_logger, log=str(output_format).replace("'", r'"'))

        # flush logging and make new one    
        if idx !=0 and start_data[idx + 1].replace('\n', '').split('\t')[0] != start_split_data[0]:
            utils.flush_logger(a_logger, output_file_handler)

        print('[Seoul Metro Txt to Log file] ({}/{}), time : {:.4f} sec'.format(idx, len(start_data), time.time() - st_t), end='\r')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Text File to Log file for 2014 Seoul Metro Data')
    parser.add_argument('--input', required=True, type=str, help='enter the input path')
    parser.add_argument('--output', required=True, type=str, help='enter the output path')
    args = parser.parse_args()
    main(args.input, args.output)
