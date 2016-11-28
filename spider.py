# -*- coding:utf-8 -*-

import urllib2
import uuid
pic_url = 'http://www.show160.com/commn/validatekey2.aspx?rnd=2136.1969224348086'

for i in xrange(100):
    content = urllib2.urlopen(pic_url).read()
    pic_name = str(uuid.uuid1()) + '.jpg'
    with open('./pic/'+pic_name, 'wb') as f:
        f.write(content)
    print '第 %s / 100 张验证码图片抓取完毕' % (i + 1)