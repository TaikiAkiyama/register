#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source ~/.bashrc

export PYTHONUNBUFFERED=1

rm -rf /dev/shm/fastrtps_*
pkill -f register
LOGfile=/tmp/register.log
rm -f $LOGfile

stdbuf -oL ros2 run register display> $LOGfile 2>&1 &
PID=$!
sleep 3

(sleep 2; echo "1") | ros2 run register scanner 
sleep 2
cat $LOGfile | grep 'Apple 150' || { echo "Test Failed: Apple not found"; kill $PID; exit 1; }


(sleep 2; echo "0") | ros2 run register scanner
sleep 2
cat $LOGfile | grep 'Error: ID' || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 2; echo "a") | ros2 run register scanner
sleep 2
cat $LOGfile | grep 'Input Error' || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 2; echo "あ") | ros2 run register scanner
sleep 2
cat $LOGfile | grep 'Input Error' || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }

(sleep 2; echo "") | ros2 run register scanner
sleep 2
cat $LOGfile | grep 'Input Error' || { echo "Test Failed: Error message not found"; kill $PID; exit 1; }
echo "All Tests Passed"
kill $PID
