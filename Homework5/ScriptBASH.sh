#!/bin/bash
#variables
PWD=$(pwd)
FILE="$1"
LOGFILE="$PWD/$FILE"

# function
request_method(){
awk '{print $6}' \
| cut -d'"' -f2	
}

wordcount(){
sort \
| uniq -c
}

filter_like_4xx(){
grep "HTTP/1.1\" 4"
}

filter_like_5xx(){
grep "HTTP/1.1\" 5"
}


return_kv_url(){
awk '{print $1,$2}'
}

return_ukzi(){
awk '{print $7,$9,$10,$1}'
}

return_kv(){
awk '{
if($2=="GET"\
|| $2 =="HEAD"\ 
|| $2 =="POST"\
|| $2 =="PUT")
{
print $1,$2
}
else
{
print $1,"Unknown"
}
}'
}

sort_size(){
sort -rnk10
}

request_url(){
awk '{print $7}'
}

request_ip(){
awk '{print $1}'
}

sort_desc(){
sort -rn
}

return_count_string(){
count=$(wc -l $1)
echo ${count//$LOGFILE/''}

}

return_top_ten(){
head -10
}

return_top_five(){
head -5
}

## actions
get_count_all_string(){
echo "Task 1.Count of all string"
echo "====================="
return_count_string $LOGFILE
echo "--------"
echo""
}

get_request_top_bytes_and_4xx(){
echo "Task 4.Top 5 Request bytes"
echo "====================="
cat $LOGFILE \
| filter_like_4xx \
| sort_size \
| return_top_five \
| return_ukzi
echo "--------"
echo""
}

get_request_top_ip_and_5xx(){
echo "Task 5.Top 5 IP"
echo "====================="
cat $LOGFILE \
| filter_like_5xx \
| request_ip \
| wordcount \
| sort_desc \
| return_kv_url \
| return_top_five
echo "--------"
echo""
}

get_request(){
echo "Task 2.Count Request:"
echo "====================="
cat $LOGFILE \
| request_method \
| wordcount \
| return_kv \
echo "--------"
echo""
}

get_request_url(){
echo "Task 3.Top 10 Request url's:"
echo "===================="
cat $LOGFILE\
| request_url \
| wordcount \
| sort_desc \
| return_kv_url \
| return_top_ten
echo "--------"
echo""
}

# executing
get_count_all_string > solve.txt
get_request >> solve.txt
get_request_url >> solve.txt
get_request_top_bytes_and_4xx >> solve.txt
get_request_top_ip_and_5xx >> solve.txt
