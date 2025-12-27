# SPDX-FileCopyrightText: 2025 Taiki Akiyama
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String 
import sys

class PriceDisplay(Node):
    def __init__(self):
        super().__init__('price_display')
        self.subscription = self.create_subscription(
            String,
            'scanned_id',
            self.listener_callback,
            10)
        self.products = {
            1: {"name": "Apple", "price": 150},
            2: {"name": "Banana", "price": 100},
            3: {"name": "Onigiri", "price": 120},
        }

    def listener_callback(self, msg):
        raw_data = msg.data
        try:
            item_id = int(raw_data)

            if item_id in self.products:
                item = self.products[item_id]
                print(f'{item["name"]} {item["price"]}', flush=True)
            else:
                print(f'Error: ID {item_id} not registered', file=sys.stderr, flush=True) 

        except ValueError:
             print(f'Input Error: {raw_data} not a number', file=sys.stderr, flush=True)

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
