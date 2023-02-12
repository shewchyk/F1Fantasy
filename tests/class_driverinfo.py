
class trying:
    def two_plus_two(num):
        return num + 2

class sprint:
    def __init__(self, driver_index_a: int, list):
        self.driver_index_a = driver_index_a
        self.list = list[str]

    def fp_sprint(driver_index, list):
     print("Enter FP finishing positions for", str(list[driver_index][0]))
     fp1 = [int(x) for x in input().split()]
     fp_point_by_session = list[driver_index].extend(fp1)
     return fp_point_by_session


