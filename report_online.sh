#!/bin/ksh

#----------------------------------------------------------------------------------------------------- online

###################### step 1

file_input1="/log/1630/dingwei_loc1/20220120/*/*"
file_output1="/app/lbs/lbs-dingwei/users/gh_internship/pv_uv06"


/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -rmr -skipTrash $file_output1

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop jar /home/map/liumin/hadoop-client_yq01_online/hadoop/contrib/streaming/hadoop-2-streaming.jar \
-D mapred.job.name="dingwei_perm-point-build_guihan_18810925036_202108_pv1" \
-D mapred.job.priority="VERY_HIGH" \
-D mapred.compress.map.output=true \
-D mapred.map.output.compression.codec=org.apache.hadoop.io.compress.QuickLzCodec \
-D mapred.max.split.size=67108864 \
-D mapred.map.tasks=10000 \
-D mapred.reduce.tasks=1000 \
-D mapred.job.map.capacity=10000 \
-D mapred.job.reduce.capacity=10000 \
-inputformat "org.apache.hadoop.mapred.TextInputFormat" \
-outputformat "org.apache.hadoop.mapred.lib.SuffixMultipleTextOutputFormat" \
-input $file_input1 \
-output $file_output1 \
-mapper 'python mapper.py' -file /home/map/gh_internship/counter_update/mapper.py \
-reducer 'python reducer.py' -file /home/map/gh_internship/counter_update/reducer.py

###################### step 2

file_input2="/app/lbs/lbs-dingwei/users/gh_internship/pv_uv06/*"
file_output2="/app/lbs/lbs-dingwei/users/gh_internship/result06"

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -rmr -skipTrash $file_output2

/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop jar /home/map/liumin/hadoop-client_yq01_online/hadoop/contrib/streaming/hadoop-2-streaming.jar \
-D mapred.job.name="dingwei_perm-point-build_guihan_18810925036_202108_pv2" \
-D mapred.job.priority="VERY_HIGH" \
-D mapred.compress.map.output=true \
-D mapred.map.output.compression.codec=org.apache.hadoop.io.compress.QuickLzCodec \
-D mapred.max.split.size=67108864 \
-D mapred.map.tasks=3000 \
-D mapred.reduce.tasks=100 \
-D mapred.job.map.capacity=3000 \
-D mapred.job.reduce.capacity=1000 \
-input $file_input2 \
-output $file_output2 \
-mapper 'python mapper.py' -file /home/map/gh_internship/counter_gps/mapper.py \
-reducer 'python reducer.py' -file /home/map/gh_internship/counter_gps/reducer.py


/home/map/liumin/hadoop-client_yq01_online/hadoop/bin/hadoop fs -cat /app/lbs/lbs-dingwei/users/gh_internship/result06/* > /home/map/gh_internship/st03.txt

python3 summary02.py > email.txt
echo $file_input1 >> email.txt #date_times
python report_sql.py > sql_sentence.txt
python3 send_email.py
