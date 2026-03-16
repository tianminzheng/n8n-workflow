from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟图书数据库 - 使用下划线命名法
books_database = {
    "9787111788737": {
        "title": "AI Agent开发实战：从基础原理到企业级应用",
        "author": "郑天民",
        "isbn": "9787111788737",
        "publisher": "机械工业出版社",
        "publish_date": "2025年09月",
        "price": "¥71.00",
        "competitor_url": "https://product.dangdang.com/29949448.html"
    }
}


@app.route('/book/<isbn>', methods=['GET'])
def get_book_by_isbn(isbn):
    """根据ISBN查询图书信息"""
    book_info = books_database.get(isbn)

    if book_info:
        return jsonify({
            "title": book_info["title"],
            "author": book_info["author"],
            "isbn": book_info["isbn"],
            "publisher": book_info["publisher"],
            "publish_date": book_info["publish_date"],
            "price": book_info["price"],
            "competitor_url": book_info["competitor_url"]
        }), 200
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/pricing-analysis', methods=['POST'])
def pricing_analysis():
    """
    定价分析API
    输入: {"owner_price": 71, "competitor_price": 66.7}
    输出: 包含定价分析结果的JSON
    """
    try:
        # 获取输入数据
        data = request.get_json()

        # 支持单条或批量处理
        if not isinstance(data, list):
            data = [data]

        results = []
        for item in data:
            owner_price = item.get('owner_price')
            competitor_price = item.get('competitor_price')

            # 参数校验
            if owner_price is None or competitor_price is None:
                return jsonify({
                    "error": "Missing required fields: owner_price and competitor_price"
                }), 400

            # 计算价格差异百分比
            price_diff_percent = ((owner_price - competitor_price) / competitor_price) * 100

            # 判断是否需要调价（owner比competitor高5%以上）
            needs_adjustment = price_diff_percent > 5

            # 计算建议价格（competitor价格的105%）
            suggested_price = round(competitor_price * 1.05, 2) if needs_adjustment else owner_price

            # 计算降价金额
            price_reduction = round(owner_price - suggested_price, 2) if needs_adjustment else 0

            # 构建结果
            result = {
                **item,
                "pricing_analysis": {
                    "price_diff_percent": round(price_diff_percent, 2),
                    "needs_adjustment": needs_adjustment,
                    "current_price": owner_price,
                    "suggested_price": suggested_price,
                    "price_reduction": price_reduction,
                    "competitor_price": competitor_price,
                    "adjustment_reason": (
                        f"当前价格比竞品高{price_diff_percent:.1f}%，超过5%阈值，建议调价"
                        if needs_adjustment
                        else "价格在合理范围内，无需调价"
                    )
                }
            }
            results.append(result)

        # 单条数据直接返回对象，批量返回数组
        return jsonify(results[0] if len(results) == 1 else results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route('/price-adjustment', methods=['POST'])
def execute_price_adjustment():
    """
    执行调价操作API
    输入: {"isbn": "9787111788737", "suggested_price": "70.4"}
    输出: 调价执行结果
    """
    try:
        data = request.get_json()

        # 支持单条或批量处理
        if not isinstance(data, list):
            data = [data]

        results = []
        for item in data:
            isbn = item.get('isbn')
            suggested_price = item.get('suggested_price')

            # 参数校验

            # TODO: 在这里调用实际的调价API或数据库操作
            # 例如：更新数据库中的价格、调用电商平台API等
            # 当前仅模拟成功执行

            adjustment_result = {
                "success": True,
                "isbn": isbn,
                "adjusted_price": suggested_price,
                "currency": "CNY",
                "status": "completed",
                "message": f"价格已成功调整至 {suggested_price}",
                "timestamp": "2026-01-01T00:00:00Z"  # 实际应使用当前时间
            }

            results.append(adjustment_result)

        # 单条数据直接返回对象，批量返回数组
        return jsonify(results[0] if len(results) == 1 else results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)