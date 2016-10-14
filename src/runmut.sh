echo $1
for i in `cat testsArgs.txt`;
do
    echo $1
    timeout 1 $1e $i ../../../inputs/grep0.dat >/dev/null 2> $1.undef 
#    echo #?
done

