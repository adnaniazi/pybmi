REM This batch file when executed converts the .ui file into a .py file. 
@echo off
call pyuic4 -x bmi_gui.ui -o bmi_gui.py