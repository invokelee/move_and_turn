#!/bin/bash
env -e
rostopic pub /drone/land std_msgs/Empty '{}' &
LAND_ID=$!
sleep 5s
kill $LAND_ID
echo 'land the drone'