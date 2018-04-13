​		python基础常见面试题

1.以下程序输出结果是什么

```python
a = 1
def fun(a):
    a = 2
fun(a)
print (a)  
```

```python
a = []
def fun(a):
    a.append(1)
fun(a)
print(a)
```



2.请简要说明什么是类变量，什么是实例变量，并观察以下程序的输出结果

```python
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print(p1.name)  
print(p2.name)
print(Person.name)
```



3.以下语句有什么弊端,name是元祖的时候，程序会是什么样的结果,如何避免

```python
"hi there %s" % name
```



4.阅读下面的代码，写出A0，A1至An的最终值。

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = [i for i in A1 if i in A0]
A3 = [A0[s] for s in A0]
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]



5.你如何管理不同版本的代码？



6.下面代码会输出什么：

```python
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l）
f(2)
f(3,[3,2,1])
f(3)
```



7.这两个参数是什么意思：`*args`，`**kwargs`？我们为什么要使用它们？



8.

阅读下面的代码，它的输出结果是什么？

```python
class A(object):
    def go(self):
        print "go A go!"
    def stop(self):
        print "stop A stop!"
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print "go B go!"

class C(A):
    def go(self):
        
        print super(C, self).go()"go C go!"
    def stop(self):
        super(C, self).stop()
        print "stop C stop!"

class D(B,C):
    def go(self):
        super(D, self).go()
        print "go D go!"
    def stop(self):
        super(D, self).stop()
        print "stop D stop!"
    def pause(self):
        print "wait D wait!"

class E(B,C): pass

a = A()
b = B()
c = C()
d = D()
e = E()

# 说明下列代码的输出结果

a.go()
b.go()
c.go()
d.go()
e.go()

a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

a.pause()
b.pause()
c.pause()
d.pause()
e.pause()
```



9.请写出一段Python代码实现删除一个list里面的重复元素



10.单引号，双引号，三引号的区别



11.写一个函数, 输入一个字符串, 返回倒序排列的结果

输入: `string_reverse(‘abcdef')` , 返回: ‘fedcba',写出你能想到的多种方法



最后：请大家自行了解一下python的内存管理机制，我会给大家进一步讲解，很重要的

Python引入了一个机制：**引用计数**。

python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。

总结一下对象会在一下情况下引用计数加1：

1.对象被创建：x=4

2.另外的别人被创建：y=x

3.被作为参数传递给函数：foo(x)

4.作为容器对象的一个元素：a=[1,x,'33']

引用计数减少情况

1.一个本地引用离开了它的作用域。比如上面的foo(x)函数结束时，x指向的对象引用减1。

2.对象的别名被显式的销毁：del x ；或者del y

3.对象的一个别名被赋值给其他对象：x=789

4.对象从一个窗口对象中移除：myList.remove(x)

5.窗口对象本身被销毁：del myList，或者窗口对象本身离开了作用域。



**垃圾回收**

1、当内存中有不再使用的部分时，垃圾收集器就会把他们清理掉。**它会去检查那些引用计数为0的对象**，然后清除其在内存的空间。当然除了引用计数为0的会被清除，还有一种情况也会被垃圾收集器清掉：当两个对象相互引用时，他们本身其他的引用已经为0了。

2、垃圾回收机制还有一个**循环垃圾回收器**, 确保释放循环引用对象(a引用b, b引用a, 导致其引用计数永远不为0)。



在Python中，许多时候申请的内存都是小块的内存，这些小块内存在申请后，很快又会被释放，由于这些内存的申请并不是为了创建对象，所以并没有对象一级的内存池机制。这就意味着Python在运行期间会大量地执行malloc和free的操作，频繁地在用户态和核心态之间进行切换，这将严重影响Python的执行效率。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。

**内存池机制**



Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。

Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的 malloc。另外Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。
