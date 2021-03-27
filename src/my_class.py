# -*- coding: utf-8 -*-
__auth__ = "timbby"


class MyClass:
    class_pro = 1  # 类属性

    # 构造函数
    def __init__(self, pro):
        self.obj_pro = pro  # 实例属性

    def get_obj_pro_I(self):  # 实例方法
        return self.class_pro

    def get_obj_pro(self):  # 实例方法
        return self.obj_pro

    @classmethod
    def get_class_pro(cls):  # 类方法
        return cls.class_pro

    @staticmethod
    def static_method():  # 静态方法
        return 'hello world'


print(MyClass.class_pro)
my_class1 = MyClass(1)
my_class2 = MyClass(2)

print(my_class1.get_obj_pro())
print(my_class2.get_obj_pro())
print(my_class1.get_class_pro())
print(my_class2.get_class_pro())
print(my_class1.class_pro)
my_class1.class_pro = 5
print(my_class1.class_pro)
print(my_class2.class_pro)
print(my_class1.get_class_pro())
print(my_class2.get_class_pro())
print(my_class1.get_obj_pro_I())
