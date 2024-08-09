import time
from functools import wraps

class Sort_handler:
    def __init__(self, sort):
        self.sort = sort

    def get_numbers_list(self):
        with open('numbers.txt', 'r') as file:
            numbers = [int(float(line)) for line in file]
        return numbers

    @staticmethod
    def time_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 在函數執行前記錄時間
            start_time = time.time()
            print(f"開始時間: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
            
            # 執行函數
            result = func(*args, **kwargs)
            
            # 在函數執行後記錄時間並計算執行時間
            end_time = time.time()
            print(f"結束時間: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
            print(f"執行時間: {end_time - start_time:.6f} 秒")
            
            return result
        
        return wrapper

    @time_decorator
    def run_sort(self):
        print(self.sort(self.get_numbers_list()))
