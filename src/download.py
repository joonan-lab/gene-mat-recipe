#!/usr/bin/env python3
"""
This script is for downloading data essential to make a gene matrix.
"""

import os
import yaml

# Path settings
project_dir = os.path.dirname(os.path.abspath('.'))
conf_dir = os.path.join(project_dir, 'conf')
filepath_conf_path = os.path.join(conf_dir, 'filepaths.yaml')
fileurl_conf_path = os.path.join(conf_dir, 'fileurls.yaml')

with open(filepath_conf_path) as filepath_conf_file:
    filepath_conf = yaml.safe_load(filepath_conf_file)

with open(fileurl_conf_path) as fileurl_conf_file:
    fileurl_conf = yaml.safe_load(fileurl_conf_file)

data_dir = os.path.join(project_dir, filepath_conf['DATA_DIR'])
os.makedirs(data_dir)  # Raise FileExistsError if this directory already exists.

# Download data
for data_key in fileurl_conf:
    data_dest_path = os.path.join(project_dir, filepath_conf[data_key])
    cmd = f'wget -O {data_dest_path} {fileurl_conf[data_key]}'
    print(cmd)
    os.system(cmd)
