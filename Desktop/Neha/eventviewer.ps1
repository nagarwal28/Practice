$time = read-host -Prompt 'Enter the time before which you want to check the System Log'
$log = read-host -Prompt 'Enter the Log Name'
$type = read-host -Prompt 'Enter the Entrytype'
Get-EventLog -LogName $log -After (Get-Date).AddHours(-$time) -EntryType $type|Export-Csv -Path "EventViewer.csv"
