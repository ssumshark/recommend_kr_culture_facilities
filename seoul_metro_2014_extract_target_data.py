import os
import natsort
import datetime
import sys
import utils
import time

def main(input_path, output_path):
    os.makedirs(output_path, exist_ok=True)
    # Init Days
    MON = 0; TUE = 1; WED = 2; THU = 3; FRI = 4; SAT = 5; SUN = 6
    START_TIME = ['06', '07', '08', '09', '10']

    for num, log in enumerate(input_path):
        st_t = time.time()
        date = log[log.find('_')+1:].split('.')[0]
        year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
        yoil = utils.get_yoil(year, month, day)
        if (yoil == SAT or yoil == SUN) and args.weekend:                                          
            file_move(log, TAR_PATH)
        elif yoil in [MON, TUE, WED, THU, FRI] and args.weekday:
            file_move(log, TAR_PATH)
        elif args.except_startTime:
            log_info = open(log, 'r', encoding='utf-8')
            weekend_lines = log_info.read().splitlines()    
            a_logger, output_handler = utils.init_logger(log.split('/')[2], output_path)           
            for weekend in weekend_lines:
                time = weekend.split(',')[0].split('-')[2].split(':')[0][3:]
                if time in START_TIME: continue
                utils.write_logger(a_logger, log=weekend)
            utils.flush_logger(a_logger, output_handler)
        else:
            print('select what you want in arguments!'); assert False
        print('txt to log file -> ({}/{})'.format(num, len(input_path), time.time() - st_t), end='\r')
       
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extract weekend or weekday, or data except starttime for 2014 Seoul Metro Data')
    parser.add_argument('--input', required=True, type=str, help='enter the input path')
    parser.add_argument('--output', required=True, type=str, help='enter the output path')
    parser.add_argument("--weekend", action="store_true", help='copy only weekend data in all data if you want')
    parser.add_argument("--weekday", action="store_true", help='copy only weekday data in all data if you want')
    parser.add_argument("--except_startTime", action="store_true", help='subtrat start time in data if you want')
    args = parser.parse_args()
    sorted_input = natsort.natsorted([os.path.join(args.input, x) for x in os.listdir(args.input)])
    main(sorted_input, args.output)       
