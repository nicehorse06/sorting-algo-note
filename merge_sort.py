from utils import Sort_handler

def merge_sort(arr):
    # 獲得列表的長度
    length = len(arr)
    
    # 如果列表長度小於或等於1，則直接返回，因為它已經是有序的
    if length <= 1:
        return arr

    # 定義合併函數來合併兩個已排序的子列表
    def merge(left, right):
        sorted_list = []  # 合併後的新列表
        i = 0  # 左子列表的索引
        j = 0  # 右子列表的索引
        
        # 遍歷兩個列表，將較小的元素逐一添加到新列表中
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                sorted_list.append(right[j])
                j += 1
            else:
                sorted_list.append(left[i])
                i += 1
        
        # 如果左列表還有剩餘元素，將其全部添加到新列表中
        if i < len(left):
            sorted_list.extend(left[i:])
        
        # 如果右列表還有剩餘元素，將其全部添加到新列表中
        if j < len(right):
            sorted_list.extend(right[j:])

        return sorted_list

    # 對列表進行分割，遞歸排序每個子列表
    mid = length // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # 合併兩個已排序的子列表
    return merge(left_half, right_half)


if __name__ == '__main__':
    handler = Sort_handler(merge_sort)
    handler.run_sort()