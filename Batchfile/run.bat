cd /d %~dp0\1_YJ\
"w2_v4_64.exe"
xcopy two_sp1_seg236.opt /d %~dp0\2_WNL\ /Y

cd /d %~dp0\2_WNL\
rename two_sp1_seg236.opt tin_zr2.csv

cd /d %~dp0\1_YJ\
xcopy two_sp1_seg236.opt /d %~dp0\2_WNL\ /Y

cd /d %~dp0\2_WNL\
rename two_sp1_seg236.opt tdt_zr2.csv
"w2_v4_64.exe"
xcopy two_sp1_seg92.opt /d %~dp0\3_LD\ /Y

cd /d %~dp0\3_LD\
rename two_sp1_seg92.opt tin_zr3.csv

cd /d %~dp0\2_WNL\
xcopy two_sp1_seg92.opt /d %~dp0\3_LD\ /Y

cd /d %~dp0\3_LD\
rename two_sp1_seg92.opt tdt_zr3.csv
"w2_v4_64.exe"
xcopy two_sp1_seg43.opt /d %~dp0\4_HD\ /Y

cd /d %~dp0\4_HD\
rename two_sp1_seg43.opt tin_zr4.csv

cd /d %~dp0\3_LD\
xcopy two_sp1_seg43.opt /d %~dp0\4_HD\ /Y

cd /d %~dp0\4_HD\
rename two_sp1_seg43.opt tdt_zr4.csv
"w2_v4_64.exe"
xcopy two_sp1_seg342.opt /d %~dp0\5_DHQ\ /Y

cd /d %~dp0\5_DHQ\
rename two_sp1_seg342.opt tin_zr5.csv

cd /d %~dp0\4_HD\
xcopy two_sp1_seg342.opt /d %~dp0\5_DHQ\ /Y

cd /d %~dp0\5_DHQ\
rename two_sp1_seg342.opt tdt_zr5.csv
"w2_v4_64.exe"

pause







