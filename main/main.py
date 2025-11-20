# 1-misol
words = ['apple', 'banana', 'cherry', 'date']

def reverse_list(lst):
    return lst[::-1]

def swap_ends(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

def sort_alpha(lst):
    return sorted(lst)

def length_list(lst):
    return len(lst)

print("=== MASALA 7 ===")
print("Boshlang'ich:", words)
print("Teskari:", reverse_list(words))
print("Almashtirilgan:", swap_ends(words.copy()))
print("Alifbo tartibi:", sort_alpha(words))
print("Uzunligi:", length_list(words))
print()

# 2-misol
data = [10, 20, 30, 40, 50]

def find_element(lst, element):
    if element in lst:
        return lst.index(element)
    return -1

def check_element(lst, element):
    return element in lst

def replace_element(lst, old, new):
    if old in lst:
        idx = lst.index(old)
        lst[idx] = new
    return lst

def append_element(lst, element):
    lst.append(element)
    return lst

print("=== MASALA 8 ===")
print("Boshlang'ich:", data)

print("30 ning indeksi:", find_element(data, 30))
print("35 bor-mi?", check_element(data, 35))
print("Almashtirish (30 → 35):", replace_element(data.copy(), 30, 35))
print("Oxiriga 60 qo'shish:", append_element(data.copy(), 60))
print()

# 3-misol
nums = [1, 2, 3, 4, 5, 6, 7, 8]

def filter_evens(lst):
    return [x for x in lst if x % 2 == 0]

def sum_evens(lst):
    return sum(filter_evens(lst))

def sort_evens(lst):
    return sorted(filter_evens(lst))

def add_even(lst, num):
    lst.append(num)
    return lst

print("=== MASALA 9 ===")
print("Boshlang'ich:", nums)
print("Juftlar:", filter_evens(nums))
print("Juft yig'indisi:", sum_evens(nums))
print("Juft tartiblangan:", sort_evens(nums))
print("Ro'yxatga 10 qo'shish:", add_even(nums.copy(), 10))
