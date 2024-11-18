from flask import Flask
from flask import render_template, request

# 创建一个 Flask 应用实例
app = Flask("__name__")  # 功能署名，__name__ 是 Python 内置的变量，表示当前模块的名称

# 定义根路由，当用户访问根 URL 时调用 index 函数
@app.route("/", methods=['GET', 'POST'])  # 允许 GET 和 POST 请求
def index():
    # 渲染并返回 index.html 模板
    return render_template('index.html')

# 定义另一个路由，当用户访问 /main URL 时调用 main 函数
@app.route("/main", methods=['GET', 'POST'])  # 允许 GET 和 POST 请求
def main():
    # 从请求中获取名为 "q" 的表单字段的值
    name = request.form.get("q")
    # 渲染并返回 main.html 模板
    return render_template('main.html')

# 检查当前模块是否是主程序
if __name__ == '__main__':  # 下划线是系统预留的，确保只有在直接运行该脚本时才会启动 Flask 应用
    app.run()  # 启动 Flask 应用，默认在 localhost:5000 上运行