#!/usr/bin/env python
# coding=utf-8

from xml.etree.ElementTree import ElementTree, Element
import xml.dom.minidom


def read_xml(in_path):
    """ 读取并解析xml文件
       in_path: xml路径
       return: ElementTree """
    dom = xml.dom.minidom.parse(in_path)                       # 读取xml文件
    root = dom.documentElement                                  # 获取xml对象
    return root


def xmlclass_to_str(root):
    """将xml对象转换字符串"""
    return root.toxml()


def updata_node_value(root, node_name, new_value):
    """根据节点名称定位节点,并修改这个节点的值，适用于节点名称唯一"""
    name = root.getElementsByTagName(node_name)
    name[0].firstChild.data = new_value
    return root


def get_node_value(root, node_name):
    """根据节点名称定位节点,获取节点的值返回，适用于节点名称唯一"""
    name = root.getElementsByTagName(node_name)
    node_value = name[0].firstChild.data
    return node_value


def updata_node_attribute(root, node_name, attribute_name, new_value):
    """根据节点名称定位节点, 并修改这个节点的属性的值，适用于节点名称唯一"""
    name = root.getElementsByTagName(node_name)
    name = name[0]
    name.setAttribute(attribute_name, new_value)
    return root


def write_xml(tree, out_path):
    """将xml文件写出
       tree: xml树
       out_path: 写出路径"""
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def if_match(node, kv_map):
    """判断某个节点是否包含所有传入参数属性
       node: 节点
       kv_map: 属性及属性值组成的map"""
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True


def find_nodes(tree, path):
    """查找某个路径匹配的所有节点
       tree: xml树
       path: 节点路径"""
    return tree.findall(path)


def get_node_by_keyvalue(nodelist, kv_map):
    """根据属性及属性值定位符合的节点，返回节点
       nodelist: 节点列表
       kv_map: 匹配属性及属性值map"""
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes


def change_node_properties(nodelist, kv_map, is_delete=False):
    """修改/增加 /删除 节点的属性及属性值
       nodelist: 节点列表
       kv_map:属性及属性值map"""
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))


def change_node_text(nodelist, text, is_add=False, is_delete=False):
    """改变/增加/删除一个节点的文本
       nodelist:节点列表
       text : 更新后的文本"""
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
            node.text = ""
        else:
            node.text = text


def create_node(tag, property_map, content):
    """新造一个节点
       tag:节点标签
       property_map:属性及属性值map
       content: 节点闭合标签里的文本内容
       return 新节点"""
    element = Element(tag, property_map)
    element.text = content
    return element


def add_child_node(nodelist, element):
    """给一个节点添加子节点
       nodelist: 节点列表
       element: 子节点"""
    for node in nodelist:
        node.append(element)


def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    """
    同过属性及属性值定位一个节点，并删除之
       nodelist: 父节点列表
       tag:子节点标签
       kv_map: 属性及属性值列表
    """
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)


def edit_node_value(file_xml, node_name, old_value, new_value):
    """
    批量修改某个节点的值
       file_xml: 修改的xml文件
       node_name:标签名称
       old_value：标签原来的值
       new_value：标签的新值
    """
    dom = xml.dom.minidom.parse(file_xml)                       # 读取xml文件
    root = dom.documentElement                                  # 获取xml对象
    name = root.getElementsByTagName(node_name)                 # 获取对应的标签列表
    for i in range(len(name)):                                  # 校验标签的value是否为传入的旧值，如果则改成传入的新值
        if name[i].firstChild.data == old_value:
            name[i].firstChild.data = new_value
    with open(file_xml, 'w', encoding='utf-8') as fh:           # 将修改后的xml文件保存，注意指定编码格式
        dom.writexml(fh, encoding='utf-8')


def zhekou_wu_to_you(file_xml, zhikou):
    """
    批量修改某个节点的值
       file_xml: 修改的xml文件
       node_name:标签名称
       old_value：标签原来的值
       new_value：标签的新值
    """
    dom = xml.dom.minidom.parse(file_xml)                       # 读取xml文件
    root = dom.documentElement                                  # 获取xml对象
    SPDJ = root.getElementsByTagName("SPDJ")                    # 获取对应的单价标签列表
    JYZJE = root.getElementsByTagName("JYZJE")                  # 获取对应的金额标签列表
    ZKZJE = root.getElementsByTagName("ZKZJE")                  # 获取对应的折扣标签列表
    SPSL = root.getElementsByTagName("SPSL")                    # 获取对应的商品数量标签列表
    sub_OD_JE = root.getElementsByTagName("OD_JE")              # 获取对应的总金额标签列表
    sub_je = 0
    for i in range(len(SPDJ)):
        DJ = SPDJ[i].firstChild.data                            # 获取单价标签对应单价值
        SL = SPSL[i].firstChild.data                            # 获取商品数量
        zheqian_JE = round(float(DJ)) * round(float(SL), 6)     #算出商品折扣前金额
        ZK = round(zheqian_JE * zhikou, 6)                      # 按传入的折扣率算出折扣值
        JE = zheqian_JE - ZK                                    # 用折扣前金额减去折扣额得出付款金额
        JYZJE[i].firstChild.data = str(JE)
        ZKZJE[i].firstChild.data = str(ZK)
        sub_je = sub_je + float(JE)
    sub_OD_JE[0].firstChild.data = sub_je
    with open(file_xml, 'w', encoding='utf-8') as fh:           # 将修改后的xml文件保存，注意指定编码格式
        dom.writexml(fh, encoding='utf-8')


