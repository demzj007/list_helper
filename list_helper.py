class ListHelper:
    """
        列表助手
    """
    @staticmethod
    def find(list_target,func_condition):
        """
            在列表中根据指定条件查找所有元素
        :param list_target:目标列表
        :param func_condition:查找条件
        :return:生成器对象
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(list_target, func_condition):
        """
            在列表中查找满足条件的第一个元素
        :param list_target: 目标列表
        :param func_condition: 查找条件
        :return: 满足条件的第一个元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target,func_condition):
        """
            获取满足条件的元素数量
        :param list_target: 目标列表
        :param func_condition: 查找条件
        :return: 满足条件的元素数量
        """
        count = 0
        for item in list_target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def sum(list_target,func_handle):
        """
            自定义类的列表对象求和
        :param list_target: 目标列表
        :param func_handle: 自定义元素的处理逻辑
        :return: 总和
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def get_max(list_target, func_condition):
        """
            在列表中获取满足条件的最大元素
        :param list_target: 目标列表
        :param func_condition: 条件
        :return: 最大的元素
        """
        max = list_target[0]
        for i in range(len(list_target)):
            if func_condition(max) < func_condition(list_target[i]):
                max = list_target[i]
        return max

    @staticmethod
    def get_min(list_target, func_condition):
        """
            在列表中获取满足条件的最小元素
        :param list_target: 目标列表
        :param func_condition: 条件
        :return: 最小的元素
        """
        min = list_target[0]
        for i in range(len(list_target)):
            if func_condition(min) > func_condition(list_target[i]):
                min = list_target[i]
        return min

    @staticmethod
    def select(list_target,func_handle):
        """
           根据条件,筛选列表
        :param list_target: 目标列表
        :param func_handle: 自定义元素的处理逻辑
        :return:需要的数据所组成的列表
        """
        result = []
        for item in list_target:
            result.append(func_handle(item))
        return result

    @staticmethod
    def order_by(list_target,func_handle):
        """
            根据条件对列表进行升序排列
        :param list_target: 目标列表
        :param func_handle: 升序条件
        """
        for r in range(len(list_target)-1):
            for c in range(r+1,len(list_target)):
                if func_handle(list_target[r]) > func_handle(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]