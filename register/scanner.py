# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BarcodeScanner(Node):
    def __init__(self):
        super().__init__('barcode_scanner')
        self.publisher_ = self.create_publisher(Int32, 'scanned_id', 10)
        self.timer = self.create_timer(1.0, self.input_callback) # 定期的に入力を促す

    def input_callback(self):
        try:
            user_input = input("商品IDを入力してください (例: 1, 2, 3...): ")
            msg = Int32()
            msg.data = int(user_input)
            self.publisher_.publish(msg)
            self.get_logger().info(f'送信: ID {msg.data}')
        except ValueError:
            self.get_logger().warn('数字を入力してください！')

def main(args=None):
    rclpy.init(args=args)
    node = BarcodeScanner()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
