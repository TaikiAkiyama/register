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

    def scan_loop(self):
        try:
            while rclpy.ok():
                line = sys.stdin.readline()
            
                if not line:
                    break

                line = line.strip()

                if not line:
                    continue

                try:
                    msg = Int32()
                    msg.data = int(line)
                    self.publisher_.publish(msg)
                except ValueError:
                    pass

        except KeyboardInterrupt:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = BarcodeScanner()
    
    node.scan_loop()

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
