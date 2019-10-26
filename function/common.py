import random,os

def make_people_name():
    a1=['张','金','李','王','赵']

    a2=['玉','明','龙','芳','军','玲']

    a3=['','立','玲','','国','']

    for i in range(15):
        name=random.choice(a1)+random.choice(a2)+random.choice(a3)
    return name

def read_data_from_file(input_file):
    file_full_path = os.path.realpath('tests/api_testing/'+input_file)
    with open(file_full_path, 'rb') as f:
        data = f.read()
    return data

def random_email(emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email