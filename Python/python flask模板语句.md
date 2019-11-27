- 语句,if判断、for循环等:
  {%......%}

- 表达式,字符串、变量、函数等:
  {{......}}

- 注释:
  {#......#}

- include标签插入一个局部模板，为了和普通模板区分，局部模板的命名通常以一个下划线开始
  ```
  {% include '_banner.html'%}
  ```

- {% block headbanner %}{% endblock %}

###### #自定义过滤器：@app.template_filter()
###### #自定义测试器：@app.template_test()



