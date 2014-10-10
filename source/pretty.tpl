%#template to pretty print the server details#%

<html>
    <head>
        <title>{{deets['hostname']}} - SchoolZilla Server Details</title>
        <!-- bootstrap begin -->
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

        <!-- Optional theme -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">

        <!-- Latest compiled and minified JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
        <!-- bootstrap end -->
        

    </head>
    <body>
        <div class="container">
            <h2>Details for {{deets['hostname']}}</h2>
            <div>
                <h3>General</h3>                
                <div>OS Version: {{ deets['os_version'] }}</div>
                <div>Boot time: {{deets['boottime']}}</div>
            </div>

            <!--CPU-->
            <div>
                <h3>CPU</h3>
                <div>
                    Overall CPU Usage: 
                    <span class="label label-{{!'success' if deets['cpu_usage'] <10 else 'warning' if deets['cpu_usage'] <50 else 'error'}}">{{deets['cpu_usage']}}%</span>
                </div>
                <div>
                    CPU Count: {{deets['cpu_details']['count']}}
                </div>
                % for cpu_detail in deets['cpu_details']['details']:
                <div>
                    CPU #{{cpu_detail['name']}}: 
                    <span class="label label-{{!'success' if cpu_detail['cpu_usage'] <10 else 'warning' if cpu_detail['cpu_usage'] <50 else 'error'}}">{{cpu_detail['cpu_usage']}}%</span>
                </div>
                %end

            </div>

            <!--Memory-->
            <div>
                <h3>Memory</h3>
                <div>
                    Overall Memory Usage: 
                    <span class="label label-{{!'success' if deets['memory_usage'] <25 else 'warning' if deets['memory_usage'] <50 else 'error'}}">{{deets['memory_usage']}}%</span>
                </div>
                <div>
                    Virtual memory (total KB/% used): {{deets['memory_details']['virtual']['total']}} / {{deets['memory_details']['virtual']['percent']}}%
                </div>
                <div>
                    Swap memory (total KB/% used): {{deets['memory_details']['swap']['total']}} / {{deets['memory_details']['swap']['percent']}}%
                </div>
            </div>        

            <!--Disk-->
            <div>
                <h3>Disk</h3>
                <div>
                    Overall Disk Usage: 
                    <span class="label label-{{!'success' if deets['disk_usage'] <25 else 'warning' if deets['disk_usage'] <50 else 'error'}}">{{deets['disk_usage']}}%</span>
                </div>
                <div>Partition count: {{deets['disk_details']['partition_count']}}</div>
                <div>read_bytes: {{deets['disk_details']['iostats']['read_bytes']}}</div>
                <div>read_count: {{deets['disk_details']['iostats']['read_count']}}</div>
                <div>read_time: {{deets['disk_details']['iostats']['read_time']}}</div>
                <div>write_bytes: {{deets['disk_details']['iostats']['write_bytes']}}</div>
                <div>write_count: {{deets['disk_details']['iostats']['write_count']}}</div>
                <div>write_time: {{deets['disk_details']['iostats']['write_time']}}</div>
                

                % for partition in deets['disk_details']['partitions']:
                <div>Device name: {{partition['device']}}</div>
                <div>Mount point: {{partition['mountpoint']}}</div>
                <div>Total MB available: {{partition['total']/1024/1024}}</div>
                <div>Percent used: {{partition['percent']}}%</div>
                % end

            </div>                   
        </div>
    </body>
</html>