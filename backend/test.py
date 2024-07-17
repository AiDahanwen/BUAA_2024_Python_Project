# -*- coding: utf-8 -*-
import oss2

# 填写RAM用户的访问密钥（AccessKey ID和AccessKey Secret）。
accessKeyId = 'LTAI5tNicQ2EWpzvo7YAYB7D'
accessKeySecret = 'UvT8HCUfLb8Y8Vu2hPgSADdZyNmQCV'
# 使用代码嵌入的RAM用户的访问密钥配置访问凭证。
auth = oss2.Auth(accessKeyId, accessKeySecret)
# 填写Bucket所在地域对应的Endpoint。以华东1（杭州）为例，Endpoint填写为https://oss-cn-hangzhou.aliyuncs.com。
endpoint = 'https://oss-cn-beijing.aliyuncs.com'

# 填写Bucket名称。
bucket = oss2.Bucket(auth, endpoint, 'buaa-python-2024')
bucket.put_object_from_file('test/test.txt', 'D:/S4/python/BUAA_2024_Python_Project/test.txt')
bucket.get_object_to_file('test/test.txt', 'D:/S4/python/BUAA_2024_Python_Project/test1.txt')
bucket.delete_object('yourObjectName')
