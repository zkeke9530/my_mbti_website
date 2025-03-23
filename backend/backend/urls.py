"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# 在这里定义路由规则（前端访问某个URL，会链接到views.py中定义的哪个处理函数），
# 然后在views.py中定义函数（如何接受/处理前端请求，并返回正确内容给前端）。
# 把特定的 URL 和对应的视图函数（get_data）关联起来
# 让用户可以通过访问这个 URL 触发视图函数执行。
from django.urls import path
from .views import get_data # get_data是之前在views.py定义的函数，处理用户请求并返回 JSON 数据
from django.contrib import admin
from django.urls import path, include
 
# 创建一个列表，包含所有 URL 路径和对应函数的配置
# 工作流程：
# 当前端访问 http://localhost:8000/api/data/ 时，Django 检查 urlpatterns 列表。
# 找到了该路径 'api/data/'
# 调用对应的视图函数 get_data
# 在views.py中执行 get_data 函数
# 返回 JSON 数据给前端
urlpatterns = [
    path('api/data/', get_data, name='get_data'),
    # 用户在浏览器中访问 http://localhost:8000/api/data/ 时会匹配到这个路由。
    path('admin/', admin.site.urls),  # 确认包含这行
    path('api/', include('mbti.urls')),  # 示例：引入mbti文件夹的接口，即交由mbti.urls处理
]
