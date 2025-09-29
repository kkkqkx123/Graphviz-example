# -*- coding: utf-8 -*-
from graphviz import Digraph

# 定义样式常量 - 使用中文字体，选择更美观的字体样式
# 字体选择：SimHei(黑体) - 笔画粗重，适合ER图；SimSun(宋体) - 传统印刷体；Microsoft YaHei(微软雅黑) - 现代简洁
CHINESE_FONT = 'SimHei'  # 黑体，笔画粗重，视觉效果更好
# CHINESE_FONT = 'SimSun'  # 宋体，传统印刷体
# CHINESE_FONT = 'Microsoft YaHei'  # 微软雅黑，现代简洁

# 定义样式常量
ENTITY_STYLE = {'shape': 'box', 'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '16', 'style': 'filled', 'fillcolor': 'lightblue'}
ATTRIBUTE_STYLE = {'shape': 'ellipse', 'fontname': CHINESE_FONT, 'penwidth': '2', 'fontsize': '14', 'style': 'filled', 'fillcolor': 'lightyellow'}
RELATIONSHIP_STYLE = {'shape': 'diamond', 'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '16', 'style': 'filled', 'fillcolor': 'lightgreen'}
EDGE_STYLE = {'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '12'}

# 创建一个有向图（ER图通常用无向图，但这里为了演示，也可使用有向图并合理设置）
# 设置中文字体支持，使用更美观的黑体字体
er = Digraph('ER图', format='png', encoding='utf-8')

# 设置图形的一些属性，使看起来更美观，使用黑体字体和合适的布局
er.attr(rankdir='LR', size='10,6', fontname=CHINESE_FONT, penwidth='2', dpi='300', bgcolor='white')

# 定义实体 - 使用样式常量
er.node('学生', **ENTITY_STYLE)
er.node('课程', **ENTITY_STYLE)
er.node('教师', **ENTITY_STYLE)

# 定义属性 - 使用样式常量
er.node('学号', **ATTRIBUTE_STYLE)
er.node('学生姓名', **ATTRIBUTE_STYLE)
er.node('课程号', **ATTRIBUTE_STYLE)
er.node('课程名', **ATTRIBUTE_STYLE)
er.node('教师编号', **ATTRIBUTE_STYLE)
er.node('教师姓名', **ATTRIBUTE_STYLE)
er.node('成绩', **ATTRIBUTE_STYLE)

# 建立实体与属性的连接 - 使用边样式常量
er.edge('学号', '学生', **EDGE_STYLE)
er.edge('学生姓名', '学生', **EDGE_STYLE)
er.edge('课程号', '课程', **EDGE_STYLE)
er.edge('课程名', '课程', **EDGE_STYLE)
er.edge('教师编号', '教师', **EDGE_STYLE)
er.edge('教师姓名', '教师', **EDGE_STYLE)

# 定义关系（这里用菱形表示关系）- 使用样式常量
er.node('选修', **RELATIONSHIP_STYLE)
er.node('讲授', **RELATIONSHIP_STYLE)

# 建立实体与关系的连接，并标注 cardinality（m、n、1等）- 使用边样式常量
er.edge('学生', '选修', label='m', **EDGE_STYLE)
er.edge('选修', '课程', label='n', **EDGE_STYLE)
er.edge('选修', '成绩', **EDGE_STYLE)
er.edge('课程', '讲授', label='n', **EDGE_STYLE)
er.edge('讲授', '教师', label='1', **EDGE_STYLE)

# 渲染并保存图形
er.render('er_diagram', view=True)