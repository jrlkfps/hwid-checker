@echo off
setlocal

:: Obtém o HWID da CPU
for /f "skip=1 tokens=2 delims==" %%a in ('wmic cpu get processorid /value') do set "cpu_id=%%a"

:: Obtém o HWID da placa-mãe
for /f "skip=1 tokens=2 delims==" %%a in ('wmic baseboard get serialnumber /value') do set "motherboard_id=%%a"

:: Obtém o HWID do HD principal (C:)
for /f "skip=1 tokens=2 delims==" %%a in ('wmic diskdrive where "DeviceID='\\\\.\\PHYSICALDRIVE0'" get serialnumber /value') do set "hd_id=%%a"

:: Exibe os IDs coletados
echo CPU ID: %cpu_id%
echo Motherboard ID: %motherboard_id%
echo Hard Drive ID: %hd_id%

:: Salva os IDs em um arquivo
(
echo CPU ID: %cpu_id%
echo Motherboard ID: %motherboard_id%
echo Hard Drive ID: %hd_id%
) > hwid.txt

endlocal
pause