# Graphviz 中文字体最佳实践指南

## 📋 概述

在使用 Python Graphviz 库生成包含中文的图表时，经常会遇到中文乱码或显示异常的问题。本文档提供了完整的解决方案和最佳实践。

## 🔍 问题分析

### 常见中文显示问题
1. **乱码显示**：中文显示为方框、问号或乱码字符
2. **字体缺失**：系统缺少中文字体支持
3. **编码问题**：文件编码或环境变量配置不当
4. **字体不兼容**：选择的字体在 Graphviz 中不可用

### 问题根源
- Graphviz 默认使用系统字体，可能不支持中文
- Windows、Linux、macOS 系统字体配置差异
- 字体名称在不同系统中可能不同

## ✅ 最佳实践解决方案

### 1. 自动字体检测机制

```python
def find_available_font():
    """自动检测系统中可用的中文字体"""
    CHINESE_FONTS = [
        'SimSun',           # 宋体 - Windows默认，兼容性最好
        'Microsoft YaHei',  # 微软雅黑 - 现代简洁
        'SimHei',           # 黑体 - 笔画粗重，视觉效果佳
        'NSimSun',          # 新宋体
        'Arial Unicode MS'  # Unicode字体 - 国际通用
    ]
    
    for font in CHINESE_FONTS:
        try:
            test_graph = Digraph('test', format='png', encoding='utf-8')
            test_graph.node('test_node', '测试', fontname=font)
            test_graph.render('font_test', cleanup=True)
            print(f"✅ 成功使用字体: {font}")
            return font
        except Exception as e:
            print(f"❌ 字体 {font} 不可用: {str(e)}")
            continue
    
    return 'Arial'  # 回退到默认字体
```

### 2. 环境变量配置

```python
import os

# 设置环境变量确保中文支持
os.environ['GRAPHVIZ_DOT'] = 'dot'
os.environ['LC_ALL'] = 'zh_CN.UTF-8'
os.environ['LANG'] = 'zh_CN.UTF-8'
```

### 3. 完整的文件编码声明

```python
# -*- coding: utf-8 -*-
from graphviz import Digraph
import os
```

### 4. 全局字体配置

```python
# 创建图表时设置编码
graph = Digraph('图表名称', format='png', encoding='utf-8')

# 设置全局字体属性
graph.graph_attr['fontname'] = CHINESE_FONT
graph.node_attr['fontname'] = CHINESE_FONT
graph.edge_attr['fontname'] = CHINESE_FONT

# 主要属性设置
graph.attr(
    rankdir='LR',      # 布局方向
    size='10,6',       # 图形尺寸
    fontname=CHINESE_FONT,  # 全局字体
    dpi='300',         # 分辨率
    bgcolor='white'    # 背景色
)
```

### 5. 样式常量定义

```python
# 实体样式（浅蓝色填充）
ENTITY_STYLE = {
    'shape': 'box', 
    'fontname': CHINESE_FONT, 
    'penwidth': '2.5', 
    'fontsize': '16', 
    'style': 'filled', 
    'fillcolor': 'lightblue'
}

# 属性样式（浅黄色填充）
ATTRIBUTE_STYLE = {
    'shape': 'ellipse', 
    'fontname': CHINESE_FONT, 
    'penwidth': '2', 
    'fontsize': '14', 
    'style': 'filled', 
    'fillcolor': 'lightyellow'
}

# 关系样式（浅绿色填充）
RELATIONSHIP_STYLE = {
    'shape': 'diamond', 
    'fontname': CHINESE_FONT, 
    'penwidth': '2.5', 
    'fontsize': '16', 
    'style': 'filled', 
    'fillcolor': 'lightgreen'
}

# 边样式
EDGE_STYLE = {
    'fontname': CHINESE_FONT, 
    'penwidth': '2.5', 
    'fontsize': '12'
}
```

## 🎨 字体选择建议

### Windows 系统
| 字体名称 | 特点 | 适用场景 |
|---------|------|----------|
| `SimSun` | 宋体，系统默认 | ✅ 兼容性最好，推荐首选 |
| `Microsoft YaHei` | 微软雅黑，现代简洁 | ✅ 视觉效果佳 |
| `SimHei` | 黑体，笔画粗重 | ✅ 图表显示效果好 |
| `NSimSun` | 新宋体 | ✅ 传统印刷风格 |

### Linux/macOS 系统
| 字体名称 | 特点 | 安装建议 |
|---------|------|----------|
| `WenQuanYi Zen Hei` | 文泉驿正黑 | 需要手动安装 |
| `AR PL UMing CN` | 宋体风格 | 需要手动安装 |
| `Arial Unicode MS` | Unicode字体 | 跨平台兼容性最好 |

## 🔧 系统字体检查

### Windows 系统字体检查
```powershell
# 检查已安装的中文字体
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts" | findstr /i "simhei simsun yahei"
```

### 字体文件位置
- **Windows**: `C:\Windows\Fonts\`
- **Linux**: `/usr/share/fonts/`, `~/.fonts/`
- **macOS**: `/System/Library/Fonts/`, `/Library/Fonts/`

## 🚨 常见问题解决

### 问题1：字体显示为方框
**解决方案**：
1. 确认字体已安装
2. 使用字体检测函数
3. 尝试不同的字体名称

### 问题2：字体显示异常
**解决方案**：
1. 检查文件编码是否为 UTF-8
2. 确认 Python 文件有编码声明
3. 检查环境变量设置

### 问题3：图表生成失败
**解决方案**：
1. 检查 Graphviz 是否安装
2. 确认字体名称拼写正确
3. 使用简单的测试代码验证

## 📊 完整示例代码

```python
# -*- coding: utf-8 -*-
from graphviz import Digraph
import os

# 设置环境变量
os.environ['GRAPHVIZ_DOT'] = 'dot'
os.environ['LC_ALL'] = 'zh_CN.UTF-8'
os.environ['LANG'] = 'zh_CN.UTF-8'

# 自动字体检测
def find_available_font():
    CHINESE_FONTS = [
        'SimSun', 'Microsoft YaHei', 'SimHei', 
        'NSimSun', 'Arial Unicode MS'
    ]
    
    for font in CHINESE_FONTS:
        try:
            test_graph = Digraph('test', format='png', encoding='utf-8')
            test_graph.node('test_node', '测试', fontname=font)
            test_graph.render('font_test', cleanup=True)
            return font
        except Exception:
            continue
    
    return 'Arial'

# 获取可用字体
CHINESE_FONT = find_available_font()

# 创建ER图
er = Digraph('ER图', format='png', encoding='utf-8')

# 设置全局属性
er.attr(rankdir='LR', size='10,6', fontname=CHINESE_FONT, 
        penwidth='2', dpi='300', bgcolor='white')

# 确保所有元素使用中文字体
er.graph_attr['fontname'] = CHINESE_FONT
er.node_attr['fontname'] = CHINESE_FONT
er.edge_attr['fontname'] = CHINESE_FONT

# 使用样式常量定义节点和边
# ... (具体实现见完整代码)

# 渲染生成图表
er.render('er_diagram', view=True)
```

## 💡 最佳实践总结

1. **✅ 使用自动字体检测**：确保跨平台兼容性
2. **✅ 设置环境变量**：确保中文环境支持
3. **✅ 使用样式常量**：代码更整洁，易于维护
4. **✅ 添加文件编码声明**：避免编码问题
5. **✅ 全局字体配置**：确保所有元素一致
6. **✅ 提供字体备选方案**：增加容错性

## 📚 相关资源

- [Graphviz 官方文档](https://graphviz.org/documentation/)
- [Python Graphviz 库文档](https://graphviz.readthedocs.io/)
- [Windows 字体管理](https://docs.microsoft.com/en-us/typography/)
- [中文字体设计原理](https://www.typeisbeautiful.com/)

---

*最后更新：2024年*  
*适用于：Python Graphviz 0.20+，Graphviz 2.0+*