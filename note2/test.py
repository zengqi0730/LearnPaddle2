import paddle.fluid as fluid

# 定义两个维度是1，值也是1的张量
x1 = fluid.layers.fill_constant(shape=[1], value=1, dtype='int64')
x2 = fluid.layers.fill_constant(shape=[1], value=1, dtype='int64')

# 将两个张量求和
y = fluid.layers.sum(x=[x1, x2])

# 创建一个使用CPU的解释器
place = fluid.CPUPlace()
exe = fluid.executor.Executor(place)
# 进行参数初始化
exe.run(fluid.default_main_program())

# 进行运算，并把y的结果输出
result = exe.run(program=fluid.default_main_program(),
                 fetch_list=[y])
# 输出计算结果
print(result)