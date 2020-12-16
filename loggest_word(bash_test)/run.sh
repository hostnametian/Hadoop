HADOOP_CMD="/usr/local/module/hadoop-2.7.2/bin/hadoop"
STREAM_JAR_PATH="/usr/local/module/hadoop-2.7.2/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"

INPUT_FILE_PATH_1="/user/miro/input/wiki.txt"

OUTPUT_PATH="/user/miro/output"

#$HADOOP_CMD fs -rmr -skipTrash $OUTPUT_PATH

# Step 1.
$HADOOP_CMD jar $STREAM_JAR_PATH \
    -input $INPUT_FILE_PATH_1 \
    -output $OUTPUT_PATH \
    -mapper "python mapper.py" \
    -reducer "python reducer.py" \
    -file ./map.py \
    -file ./red.py

