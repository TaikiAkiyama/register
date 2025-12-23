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
            1: {"name": "りんご", "price": 150},
            2: {"name": "バナナ", "price": 100},
            3: {"name": "おにぎり", "price": 120},
            100: {"name": "高級ステーキ", "price": 5000}
        }

    def listener_callback(self, msg):
        item_id = msg.data
        if item_id in self.products:
            item = self.products[item_id]
            # ログ出力でレジの表示を再現
            self.get_logger().info(f'\n--- レシート ---\n商品名: {item["name"]}\n価格  : ¥{item["price"]}\n----------------')
        else:
            self.get_logger().warn(f'ID: {item_id} は登録されていません。')

def main(args=None):
    rclpy.init(args=args)
    node = PriceDisplay()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
