# new_string = "Hello , World"
# #H e l l o   ,   w o r l d
# #0 1 2 3 4 5 6 7 8 9 10 11 12
# print(len(new_string))
#
# for i in range(len(new_string)):
#     print(f"pos:{i} value at pos {i} is : {new_string[i]}")
#
# print(new_string[0:5])
# print(new_string[8:13])
# print(new_string[-1])
#
# def reverse_string(string: str) -> str:
#     """
#     Return a reversed string
#     """
#     list_string = list(string)
#     temp = 0
#     for i in range(len(string) // 2):
#         temp = list_string[i]
#         list_string[i] = list_string[len(string) - i - 1]
#         list_string[len(string) - i - 1] = temp
#     return "".join(list_string)
#
# print(reverse_string(new_string))
# print(new_string[::-1])
#
#
# new_list = [1, 2, 3, 4, [1,2,3,4], 6, 7, 8, "Hello"]
# print(len(new_list))
# print(new_list[8])
# print(new_list[0])
# print(new_list[4])
#
# for ele in range(len(new_list)):
#     print(new_list[ele])
#
# for value in new_list:
#     print(value)
#
#
# new_dict = {"page one": "Introduction",
#             2: "Operators",
#             3: "Classes",
#             4: "Strings"}
# print(new_dict["page one"])
#
# for key in new_dict.keys():
#     print(key)
# for value in new_dict.values():
#     print(value)
# for key, value in new_dict.items():
#     print(f"key:{key} value:{value}")