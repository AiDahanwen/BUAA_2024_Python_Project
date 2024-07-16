**上传描述：前端/后端-修复/更新/...-内容-作者**

# frontend



# backend

## database.py

#### `get_constant(file_name, constant_name)`

用于从数据库中获得常量的值，参数为**文件名**和**常量名**，返回值均为**字符串类型**。下面的代码可以获得发送方邮箱地址。

```python
send_by = get_constant(file_name, 'send_by')
```

把一些参数常量放在数据库，是为了不用修改代码就可以直接改变程序的运行状况。

#### 数据库

使用阿里云数据库，可通过外网链接访问。

```python
host='rm-cn-g6z3tw7xl00052co.rwlb.rds.aliyuncs.com'
port=3306
user='buaa_python_2024'
passwd='DCJBzxhy2024'
database='python_todo'
```

## send_email_code.py

#### `send_email_code(send_to)`

用于向指定邮箱发送验证码，参数为**接收方邮箱地址**，发送成功将返回**验证码（字符串类型）**，发送失败将返回**False**。验证码为随机生成的六位大小写字母、数字的组合。下面的代码可以向`2892278592@qq.com` 发送并返回验证码。

```python
email_code=send_email_code('2892278592@qq.com')
```

使用 QQ 邮箱发送验证码，相关服务信息默认如下（可在数据库中修改，发送前会先更新）：

```python
send_by = '2892278592@qq.com'
email_password = 'kwniejavvatkdgcf'
mail_host = 'smtp.qq.com'
send_port = 465
```

### daily_sentence.py

#### `get_sentence()`

用于随机产生每日一句格言，内容涵盖文学、影视、诗词、哲学等方面，返回值为**格言内容（字符串类型）与出处的元组**。下面的代码可以获得一句格言及出处。

```python
sentenct=get_sentence()	# ('人生如逆旅，我亦是行人。', '临江仙·送钱穆父')
```

