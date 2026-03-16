from flask import Flask, request, jsonify

app = Flask(__name__)

# 硬编码库存数据
INVENTORY = {
    "ITEM-001": True,  # 有库存
    "ITEM-002": False  # 无库存
}


@app.route('/check-stock', methods=['POST'])
def check_stock():
    """
    检查商品库存接口
    接收订单信息，返回指定SKU的库存状态
    """
    try:
        # 获取JSON数据
        data = request.get_json()

        # 验证必要字段
        if not data or 'sku' not in data or 'orderId' not in data:
            return jsonify({
                "error": "Missing required fields: sku and orderId are required"
            }), 400

        sku = data.get('sku')
        order_id = data.get('orderId')

        # 查询库存状态（硬编码）
        stock_available = INVENTORY.get(sku, False)

        # 构建响应
        response = {
            "orderId": order_id,
            "sku": sku,
            "stockAvailable": stock_available
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({
            "error": f"Internal server error: {str(e)}"
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)