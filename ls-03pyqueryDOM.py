#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author: liusheng time:2018/4/7
from pyquery import PyQuery as pq

html ="""
<div class="wrap">
    Hello word
    <p>this is a paragraph</p>
    <p>nanannanan</p>
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link2.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
</div>
"""
doc = pq(html)
li = doc('.item-0.active')
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

#修改属性,样式
li.attr('name','link')
print(li)
li.css('font-size','20px')
print(li)

#伪类选择器
lit = doc('#container li:first-child')
print(lit)
lit = doc('#container li:nth-child(2)')  #获取第二个元素
print(lit)
lit = doc('#container li:gt(2)')  #0开始索引,输出序号2以后的
print(lit)
#li:nth-child(2n)获取序号（不从0开始）偶数元素
lit = doc('#container li:contains(second)') #输出包含second的标签
print(lit)

#remove  删除后的元素后续不可用
warp = doc('.wrap')
#print(warp.text())
#warp.find('p').remove()
warp('p:first-child').remove()
warp.find('#container').remove()
print(warp.text())
