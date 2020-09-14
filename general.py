# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 07:39:14 2020

@author: cosmotron
"""

import os

#each crawled site is a separate project
def create_dir(dirct):
     if not os.path.exists(dirct):
         print('Creating proj ' + dirct)
         os.makedirs(dirct)
         
create_dir('flinkhub')

#create queue and crawled files
def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '') 
 
#create a new file       
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
    
#create_data_files('flinkhub', 'https://flinkhub.com/')
    
#add data onto existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')
        
#delete the contents of a file
def delete_file_contents(path):
    with open(path, 'w'):
        pass
    
#read a file and convert to set
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#iterate set and each set item will be new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)
        