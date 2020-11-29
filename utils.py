import logging
import shutil
import datetime

def init_logger(name, output_path):
    name = name.replace(".", "-")     
    a_logger = logging.getLogger()
    a_logger.setLevel(logging.DEBUG)
    output_file_handler = logging.FileHandler(output_path + str(name) +".log")
    a_logger.addHandler(output_file_handler)
    return a_logger, output_file_handler

def write_logger(logger, log):
    logger.debug(str(log).replace("'", r'"'))

def flush_logger(logger, output_handler):
    logger.removeHandler(output_handler)

def file_move(orig_path, tar_path):
    shutil.copy(orig_path, tar_path)   

def get_yoil(year, month, day):
    return datetime.datetime(year, month, day).weekday()

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_uclidean_distance(src, tar):
    src[1], src[2], tar[1], tar[2] = float(src[1]), float(src[2]), float(tar[1]), float(tar[2])
    diff = ((tar[1] - src[1])**2 + (tar[2] - src[2])**2)**(1/2)
    return diff

