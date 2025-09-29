# -*- coding: utf-8 -*-
from graphviz import Digraph
import os

# 设置环境变量确保中文支持
os.environ['GRAPHVIZ_DOT'] = 'dot'
os.environ['LC_ALL'] = 'zh_CN.UTF-8'
os.environ['LANG'] = 'zh_CN.UTF-8'

# 定义多个中文字体备选方案
CHINESE_FONTS = [
    'SimSun',           # 宋体，Windows系统默认，兼容性最好
    'Microsoft YaHei',  # 微软雅黑，现代简洁
    'SimHei',           # 黑体，笔画粗重
    'NSimSun',          # 新宋体
    'Arial Unicode MS'  # Unicode字体，国际通用
]

# 尝试找到可用的字体
def find_available_font():
    """找到系统中可用的中文字体"""
    test_graph = Digraph('test', format='png', encoding='utf-8')
    
    for font in CHINESE_FONTS:
        try:
            # 测试字体
            test_graph.clear()
            test_graph.node('test_node', '测试', fontname=font)
            test_graph.render('font_test', cleanup=True)
            print(f"成功使用字体: {font}")
            return font
        except Exception as e:
            print(f"字体 {font} 不可用: {str(e)}")
            continue
    
    # 如果都不可用，返回默认字体
    print("使用默认字体")
    return 'Arial'

# 找到可用的中文字体
CHINESE_FONT = find_available_font()

# 定义样式常量
ENTITY_STYLE = {'shape': 'box', 'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '16', 'style': 'filled', 'fillcolor': 'lightblue'}
ATTRIBUTE_STYLE = {'shape': 'ellipse', 'fontname': CHINESE_FONT, 'penwidth': '2', 'fontsize': '14', 'style': 'filled', 'fillcolor': 'lightyellow'}
RELATIONSHIP_STYLE = {'shape': 'diamond', 'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '16', 'style': 'filled', 'fillcolor': 'lightgreen'}
EDGE_STYLE = {'fontname': CHINESE_FONT, 'penwidth': '2.5', 'fontsize': '12'}

# 创建ER图
print(f"使用字体 {CHINESE_FONT} 生成ER图...")
er = Digraph('ER图', format='png', encoding='utf-8')

# 设置全局属性
er.attr(rankdir='LR', size='10,6', fontname=CHINESE_FONT, penwidth='2', dpi='300', bgcolor='white')

# 确保所有元素都使用中文字体
er.graph_attr['fontname'] = CHINESE_FONT
er.node_attr['fontname'] = CHINESE_FONT
er.edge_attr['fontname'] = CHINESE_FONT

# 定义实体
er.node('学生', **ENTITY_STYLE)
er.node('课程', **ENTITY_STYLE)
er.node('教师', **ENTITY_STYLE)

# 定义属性
er.node('学号', **ATTRIBUTE_STYLE)
er.node('学生姓名', **ATTRIBUTE_STYLE)
er.node('课程号', **ATTRIBUTE_STYLE)
er.node('课程名', **ATTRIBUTE_STYLE)
er.node('教师编号', **ATTRIBUTE_STYLE)
er.node('教师姓名', **ATTRIBUTE_STYLE)
er.node('成绩', **ATTRIBUTE_STYLE)

# 建立实体与属性的连接
er.edge('学号', '学生', **EDGE_STYLE)
er.edge('学生姓名', '学生', **EDGE_STYLE)
er.edge('课程号', '课程', **EDGE_STYLE)
er.edge('课程名', '课程', **EDGE_STYLE)
er.edge('教师编号', '教师', **EDGE_STYLE)
er.edge('教师姓名', '教师', **EDGE_STYLE)

# 定义关系
er.node('选修', **RELATIONSHIP_STYLE)
er.node('讲授', **RELATIONSHIP_STYLE)

# 建立实体与关系的连接
er.edge('学生', '选修', label='m', **EDGE_STYLE)
er.edge('选修', '课程', label='n', **EDGE_STYLE)
er.edge('选修', '成绩', **EDGE_STYLE)
er.edge('课程', '讲授', label='n', **EDGE_STYLE)
er.edge('讲授', '教师', label='1', **EDGE_STYLE)

# 渲染并保存图形
er.render('er_diagram_fixed', view=True)
print("ER图生成完成！")

# 清理测试文件
import glob
for f in glob.glob('font_test*'):
    os.remove(f)