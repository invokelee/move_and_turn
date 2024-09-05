#!/bin/bash
set -e
rostopic pub /drone/takeoff std_msgs/Empty '{}' &
TAKEOFF_ID=$!
sleep 10s
kill $TAKEOFF_ID
echo 'takeoff the drone'