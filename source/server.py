#server.py
###############################################################################
# Serves up cpu, memory and disk usage on a webpage
#
# author: eric.hoxworth@gmail.com
###############################################################################

import os
import bottle
import psutil
from bottle import route, run, request, abort, redirect, Response, template
import platform
from datetime import datetime


@route('/', method="GET")
def main():

    __format = "pretty"

    if 'format' in request.query.keys() and request.query['format'] in ['json']:
        __format = request.query['format'];

    deets = getDetails()
    
    output = None

    if __format=="pretty":
        # load template
        output = template("pretty.tpl",deets=deets)

    if __format=="json":
        # already in json, just send it
        output = deets


    # Other formatters can place here
    return output


def getDetails():

    # return these details
    deets = {"cpu_usage":None,"memory_usage":None,"disk_usage":None,"os_version":platform.platform()}

    deets['cpu_usage'] = psutil.cpu_percent(interval=None)
    deets['memory_usage'] = psutil.virtual_memory().percent
    deets['disk_usage'] = psutil.disk_usage('/').percent

    ####
    # Bonus data:
    ####

    # CPU
    deets['cpu_details'] = {'details':[]}
    cpu_details = psutil.cpu_percent(interval=None, percpu=True)
    deets['cpu_details']['count'] = len(cpu_details)
    for i in range(0,len(cpu_details)):
        deets['cpu_details']['details'].append({'name':i,'cpu_usage':cpu_details[i]})

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

    deets['hostname'] = platform.node()
    deets['boottime'] = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    
    return deets    


# This must be added in order to do correct path lookups for the views
import os
from bottle import default_app
application=default_app()

