# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PriceDisplay(Node):
    def __init__(self):
        super().__init__('price_display')
        self.subscription = self.create_subscription(
            Int32,
            'scanned_id',
            self.listener_callback,
            10)
        self.products = {
            1: {"name": "Apple", "price": 150},
            2: {"name": "Banana", "price": 100},
            3: {"name": "Onigiri", "price": 120},
        }

    def listener_callback(self, msg):
        item_id = msg.data
        if item_id in self.products:
            item = self.products[item_id]
            print(f'{item["name"]} {item["price"]}', flush=True)
        else:
            pass

def main(args=None):
    rclpy.init(args=args)
    node = PriceDisplay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
