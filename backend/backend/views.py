# 创建一个简单的接口，让浏览器或前端程序可以通过访问某个 URL 获取一段固定的 JSON 数据。

from rest_framework.decorators import api_view
from rest_framework.response import Response
 
# api_view这个工具把普通的函数变成可以处理 API 请求的函数，同时你可以指定它只接受某些请求方式，比如 GET
# 这个函数只能处理 GET 请求
# 比如用户通过浏览器直接访问 URL，
# 或者前端通过 axios.get 发送请求
@api_view(['GET'])  

def get_data(request):
    data = {'message': 'Hello from Django!'}
    return Response(data)   
# 用于返回 JSON 格式的响应
# 用 Response 包裹后，内容会自动变成 JSON 格式发送给前端