# -*- coding: utf-8 -*-
from graphviz import Digraph
import os

# 测试不同的中文字体
fonts = ['SimHei', 'Microsoft YaHei', 'SimSun', 'Arial Unicode MS']

for font in fonts:
    print(f"测试字体: {font}")
    try:
        # 创建简单的测试图
        test = Digraph('测试', format='png', encoding='utf-8')
        test.attr(fontname=font)
        test.node('测试节点', '学生', fontname=font)
        test.node('测试节点2', '课程', fontname=font)
        test.edge('测试节点', '测试节点2', '选修', fontname=font)
        
        # 保存为临时文件
        filename = f'test_{font.replace(" ", "_")}.png'
        test.render(f'test_{font.replace(" ", "_")}', format='png', cleanup=True)
        print(f"  ✓ {font} - 成功生成")
        
    except Exception as e:
        print(f"  ✗ {font} - 失败: {str(e)}")

print("\n测试完成！请检查生成的PNG文件是否显示中文正常。")