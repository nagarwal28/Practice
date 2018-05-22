Get-Process | Sort CPU -descending | Select -first 1 -Property ID,ProcessName,CPU > taskmanager.txt
