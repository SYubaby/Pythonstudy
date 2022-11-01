'''
面向对象三大特性
类属性和实例属性
类方法和静态方法
封装
继承
多态
传入不同的对象，产生不同的结果

'''
# 多态指一类事物有多重形态：使用对象的方式。子类重写父类方法，调用不同子类对象的相同父类方法，可以产生不同的执行结果。

# 警务人员跟警犬工作，警犬分2类，追击敌人和追查毒品，携带不同的警犬

# 1.定义父类 并提供公共方法： 警犬和人

class Dog(object):
    def work(self):
        print('指哪儿打哪儿。。。')

#2.定义子类，并重写父类方法：定义两个类表示不同的警犬

class ArmyDog(Dog):
    def work(self):
        print('追击敌人。。。')

class DrugDog(Dog):
    def work(self):
        print('追查毒品。。。')



class Person(object):
    def work_with_dog(self, dog):
        dog.work()


#3.传递子类对象给调用者，可以看到不同子类执行效果不同：观察执行结果

ad = ArmyDog()
dd = DrugDog()

Peter = Person()
Peter.work_with_dog(ad)
Peter.work_with_dog(dd)