#!/bin/ksh

#----------------------------------------------------------------------------------------------------- online

###################### step 1

file_input3="/log/1630/dingwei_loc1/20220209/*/*"
file_output3="/app/lbs/lbs-dingwei/users/gh_internship/badcase06"

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -rmr -skipTrash $file_output3

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop jar /home/map/liumin/hadoop-client_yq01_online/hadoop/contrib/streaming/hadoop-2-streaming.jar \
-D mapred.job.name="dingwei_perm-point-build_guihan_18810925036_202108_pv3" \
-D mapred.job.priority="VERY_HIGH" \
-D mapred.max.split.size=67108864 \
-D mapred.map.tasks=10000 \
-D mapred.reduce.tasks=1000 \
-D mapred.job.map.capacity=10000 \
-D mapred.job.reduce.capacity=10000 \
-input $file_input3 \
-output $file_output3 \
-mapper 'python mapper.py' -file /home/map/gh_internship/counter11/mapper.py \
-reducer 'python reducer.py' -file /home/map/gh_internship/counter11/reducer.py

###################### step 2

file_input4="/app/lbs/lbs-dingwei/users/gh_internship/badcase06/*"
file_output4="/app/lbs/lbs-dingwei/users/gh_internship/result16"

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -rmr -skipTrash $file_output4

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop jar /home/map/liumin/hadoop-client_yq01_online/hadoop/contrib/streaming/hadoop-2-streaming.jar \
-D mapred.job.name="dingwei_perm-point-build_guihan_18810925036_202108_pv4" \
-D mapred.job.priority="VERY_HIGH" \
-D mapred.max.split.size=67108864 \
-D mapred.map.tasks=3000 \
-D mapred.reduce.tasks=10 \
-D mapred.job.map.capacity=3000 \
-D mapred.job.reduce.capacity=1000 \
-input $file_input4 \
-output $file_output4 \
-mapper 'python mapper.py' -file /home/map/gh_internship/counter12/mapper.py \
-reducer 'python reducer.py' -file /home/map/gh_internship/counter12/reducer.py

###################### step 3
/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -cat /app/lbs/lbs-dingwei/users/gh_internship/result16/* > /home/map/gh_internship/testing02.txt

cat testing02.txt |python badcase_analysis.py > testing03.txt
echo $file_input3 >> testing03.txt
python badcase_conclusion.py > testing04.txt
python email_badcase.py 
