#coding:utf-8
#python3
# a = b'\u60a3'
# print(a.decode("unicode-escape"))

#python2
a = '\u5229\u4ed6\u884c\u4e3a\u662f\u7531\u4e8e\u57fa\u56e0\u76f8\u4f3c\u0001\u9053\u5fb7\u5fb7\u751f\u7269\u5b66\u8d77\u6e90\u5f88\u53ef\u80fd\u5c31\u662f\u4e0e\u201c\u901a\u8fc7\u4eb2\u5c5e\u7684\u751f\u5b58\u800c\u5b8c\u6210\u5bb6\u65cf\u57fa\u56e0\u7684\u5907\u4efd\u201d\u8fd9\u4e00\u9690\u853d\u7684\u751f\u7269\u5b66\u76ee\u7684\u76f8\u5173\u7684\u3002\u0001\u5728\u5047\u5b9a\u7532\u3001\u4e59\u4e24\u4e2a\u751f\u7269\u5b66\u4e2a\u4f53\u4e4b\u95f4\u5177\u6709\u4e00\u5b9a\u7684\u9057\u4f20\u76f8\u4f3c\u6027\u7684\u524d\u63d0\u4e0b,\u53ea\u8981\u8fd9\u79cd\u76f8\u4f3c\u6027\u4e0e\u201c\u4e59\u4ece\u7532\u83b7\u5f97\u7684\u597d\u5904\u201c\u4e4b\u95f4\u4e58\u79ef\u80fd\u591f\u62b5\u6d88\u201c\u7532\u81ea\u8eab\u56e0\u5e2e\u52a9\u4e59\u800c\u906d\u53d7\u5230\u7684\u635f\u5931\u201d,\u90a3\u4e48,\u4f7f\u5f97\u4e92\u52a9\u884c\u4e3a\u5f97\u4ee5\u53ef\u80fd\u7684\u90a3\u4e9b\u57fa\u56e0\u5c31\u4f1a\u5728\u79cd\u7fa4\u4e2d\u4f20\u64ad\u3002 '
print(a.decode("unicode-escape"))




# import re
# import urllib

# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

# html = getHtml("https://mooc.beastwn.com/api/wechat/answer/search?keyword=机器翻译的局限性在于(%20)。")
# print(html.decode("unicode-escape"))