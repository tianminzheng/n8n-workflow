from flask import Flask, render_template, request, jsonify

# 创建Flask应用实例
app = Flask(__name__)

# 定义路由
@app.route('/user/<name>')
def user(name):
    return f'你好，{name}！'

# 返回JSON数据
@app.route('/api/data')
def api_data():
    data = {
        'name': 'Flask Web服务',
        'version': '1.0',
        'author': 'Your Name'
    }
    return jsonify(data)

# 处理GET和POST请求
@app.route('/submit', methods=['POST'])
def submit():
  name = request.form.get('name')
  return f'提交成功！欢迎你，{name}</h1>'

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return '没有文件部分', 400
    file = request.files['file']
    if file.filename == '':
        return '没有选择文件', 400
    if file:
        filename = file.filename
        return f'文件 {filename} 已成功上传！'

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)