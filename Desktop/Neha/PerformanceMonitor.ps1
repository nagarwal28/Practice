echo (Get-Counter -counter "\LogicalDisk(_Total)\% Free Space").CounterSamples.CookedValue
echo (Get-Counter -counter "\Processor(_Total)\% Processor Time”).CounterSamples.CookedValue
echo (Get-Counter -counter "\Memory\Available MBytes”).CounterSamples.CookedValue
echo "Processor Performance="(Get-Counter -counter "\TCPv6\Connections Active").CounterSamples.CookedValue
echo "File Write Operations="(Get-Counter -counter "\TCPv6\Connections Established").CounterSamples.CookedValue