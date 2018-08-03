x=0

for ((n=0;n<=42;n++));

do opencv_createsamples -img pos/$x.jpg -bg bg.txt -info info/info$x.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 900;
let "x++"

done

cd info/
cat *.lst >> main.lst
