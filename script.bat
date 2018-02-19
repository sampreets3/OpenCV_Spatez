@echo off
D: 
cd Spatez
cd Program
python handrec_1.py
move D:\Spatez\Program\*.png D:\Spatez\Screenshots
move D:\Spatez\Program\output.avi D:\Spatez\Video
exit