# -*- coding: gb2312 -*- 

import random, string



#print random.randint(1,29)
# ����һ���÷�Χ�ڵ������


#print random.randrange(0,30,5)
# �����һ����Χ�ڵ������Ե���������Ϊ����,Ҳ����ֻ��ȡ0,5,10,15,20,25,30�⼸��ֵ��


#print random.random()
# ����0��1֮��ĸ��������, ע��, ���ܴ�����


#print random.uniform(1,20)
# ����1��20֮��ĸ��������



#print '������ɵ��ַ�(a~z)��%c' %random.choice('abcdefghijklmnopqrstuvwxyz')
#print '������ɵ��ַ���(�����ġ����)��%s' %random.choice(['spring', 'summer',
#'fall', 'winter'])
# ������ַ�����ѡ��һ���ַ�, ���Ǵ��б���ѡ��һ��Ԫ��#





print random.sample('abcdefghijklmnopqrstuvwxyz', 4)
# ���ַ��������ѡ��4���ַ������б�ʽ����
# ����: ['e', 'y', 'u', 'f'] 





'''
print '������ɵ��ַ�����%s' % string.join(
    random.sample('abcdefghijklmnopqrstuvwxyz', 4), '')
'''
# �������һ�� 4���ַ� ���ַ���

#join��һ���ַ����б��еĸ����ַ��������������м����ָ�����ַ���














