# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import sys

class BarcodeScanner(Node):
    def __init__(self):
        super().__init__('barcode_scanner')
        self.publisher_ = self.create_publisher(Int32, 'scanned_id', 10)

    def read_and_publish(self):
        try:
            line = sys.stdin.readline()
            if line:
                try:
                    msg = Int32()
                    msg.data = int(line.strip())
                    self.publisher_.publish(msg)
                except ValueError:
                    pass
            else:
                return False 
        except KeyboardInterrupt:
            return False
        return True

def main(args=None):
    rclpy.init(args=args)
    node = BarcodeScanner()

    try:
        while rclpy.ok():
            if not node.read_and_publish():
                break
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
