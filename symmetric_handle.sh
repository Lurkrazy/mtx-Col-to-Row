#!/bin/bash
if [[ $#<1 ]]; then
	echo "please add the input file .mtx"
	exit 1
fi

output=${1/.mtx/_symm.mtx}
echo $output
cp $1 $output

# 复制原矩阵，删掉除数据以外的所有行
sed  '/%/d' $1 > tmp
sed -i '1d' tmp

#交换数据行的第一列和第二列，并追加到输出文件
awk ' { t = $1; $1 = $2; $2 = t; print; } ' tmp >> $output	
line=`sed -n '/%/=' $output`
line1=($line)
#echo ${line1[-1]}
#lines=`expr ${line:0-1:1} + 2`

#获取数据第一行行号
lines=$[line1[-1]+2]	
# echo $lines

#获取第一行行号
lines1=$[$lines-1] 
# sed -n "${lines1}p" L-9-1.mtx | awk '{print $3}'

#获取非零元数量
nnz=$(sed -n "${lines1}p" $output | awk '{print $3}')
# echo $nnz

nnz_new=($nnz)
nnz_new=$[nnz_new*2]
# echo $nnz_new

#将非零元数量乘以2
sed -i "s/$nnz/$nnz_new/g" $output	
# echo $nnz

#若没有给出矩阵的值，在数据行后面加上值1
num=$(sed -n "${lines}p" $output | awk '{print NF}')
# echo $num
if [ $num -lt 3 ]
then
   	# echo "no val"
	sed -i "${lines},$ s/$/&\ 1/g" $output	
fi

rm tmp

