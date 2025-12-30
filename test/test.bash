#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
source /opt/ros/humble/setup.bash 
colcon build
source install/setup.bash

export PYTHONUNBUFFERED=1

rm -rf /dev/shm/fastrtps_*
LOGfile=/tmp/register.log
rm -f $LOGfile

stdbuf -oL ros2 run register display> $LOGfile 2>&1 &
PID=$!
sleep 10

(sleep 3; echo "1") | ros2 run register scanner 
sleep 3
grep 'Apple 150' $LOGfile || { echo "Test Failed: Apple not found"; kill $PID; exit 1; }


(sleep 3; echo "0") | ros2 run register scanner
sleep 3
grep 'Error: ID' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 3; echo "1.1") | ros2 run register scanner
sleep 3
grep 'Error: ID' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 3; echo "a") | ros2 run register scanner
sleep 3
grep 'Input Error' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 3; echo "あ") | ros2 run register scanner
sleep 3
grep 'Input Error' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 3; echo "") | ros2 run register scanner
sleep 3
grep 'Input Error' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 3; echo "1\n2") | ros2 run register scanner
sleep 3
grep 'Input Error' $LOGfile || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }
echo "All Tests Passed"
kill $PID
