#server.py
###############################################################################
# Serves up cpu, memory and disk usage on a webpage
#
# author: eric.hoxworth@gmail.com
###############################################################################

import os
import bottle
import psutil
from bottle import route, run, request, abort, redirect, Response
from sys import platform

@route('/')
def main():

    # return these details
    deets = {"cpu_usage":None,"memory_usage":None,"disk_usage":None,"os_version":platform}

    deets['cpu_usage'] = psutil.cpu_percent(interval=None)
    deets['memory_usage'] = psutil.virtual_memory().percent
    deets['disk_usage'] = psutil.disk_usage('/').percent


    ####
    # Bonus data:
    ####

    # CPU
    deets['cpu_details'] = {'count':-1,'details':psutil.cpu_percent(interval=None, percpu=True)}
    deets['cpu_details']['count'] = len(deets['cpu_details']['details'])

    # Memory
    deets['memory_details'] = {}
    deets['memory_details']['virtual'] = {
        'percent':psutil.virtual_memory().percent,
        'total':psutil.virtual_memory().total
        }
    deets['memory_details']['swap'] = {
        'percent':psutil.swap_memory().percent,
        'total':psutil.swap_memory().total
        }

    # Disk
    deets['disk_details'] = {}
    deets['disk_details']['partition_count'] = len(psutil.disk_partitions())
    deets['disk_details']['partition_count'] = len(psutil.disk_partitions())
    deets['disk_details']['partitions'] = []
    for partition in psutil.disk_partitions():
        deets['disk_details']['partitions'].append({
            'device':partition.device,
            'mountpoint':partition.mountpoint,
            'percent':psutil.disk_usage(partition.mountpoint).percent,
            'total':psutil.disk_usage(partition.mountpoint).total,
            })
    deets['disk_details']['iostats'] = {}
    sdiskio = psutil.disk_io_counters()
    for k in ['read_count','write_count','read_bytes','write_bytes','read_time','write_time']:
        deets['disk_details']['iostats'][k] = getattr(sdiskio,k)


    return deets    

# This must be added in order to do correct path lookups for the views
import os
from bottle import default_app
application=default_app()

