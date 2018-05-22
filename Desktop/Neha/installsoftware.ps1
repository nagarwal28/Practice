$uri="https://notepad-plus-plus.org/repository/7.x/7.5.6/npp.7.5.6.Installer.x64.exe"
$out= "C:\Users\nagarwal\npp.exe"
Invoke-WebRequest -Uri $uri -OutFile $out
Start-Process -FilePath "npp.exe" -ArgumentList "/i $out /quiet /norestart /l C:\installlog.txt"
$out= "C:\Users\nagarwal\npp.exe"
Start-Process -Wait -FilePath $out -ArgumentList "/S" -PassThru
echo "Software  installed successfully."