@echo off
SET mypath=%~dp0
echo %mypath:~0,-1%
C:
cd %ProgramFiles%\java\jdk1.8.0_131\bin\
start java.exe -jar %mypath:~0,-1%\BeutlerAdmin.jar 192.168.0.209
