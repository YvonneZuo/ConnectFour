from connect_four_dfs import ConnectFour
board = ConnectFour()
print(board.is_game_over())

# count = 0
# x = 1
# b = 2
# while count != 10 and x != 2:
#     count += 1
#     print(count)
#     x += 1
#     print(x)
#     b += 1
#     print(b)


# x = [["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"],
#          ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]]

#
# xstring = "".join(x)
# # print(xstring)
# # xstring.join(y)
# xstring = "x"
# print(xstring.join(y))
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         print(x[i][j], end="")
#     print()

# x = [" ", " "]
# y = ["|" "|"]




x = [["X", " ", " ", " ", " ", " ", " "],
 ["X", " ", " ", " ", " ", " ", " "],
 ["x", " ", " ", " ", " ", " ", " "],
 ["X", " ", " ", " ", " ", " ", " "],
 ["x", " ", " ", " ", " ", " ", " "],
 ["X", " ", " ", " ", " ", " ", " "]]

# col0 = []
# for row in range(len(x)):
#     col0.append(x[row][0])
# # print(col0)




# col0 = ['0', '1', '2', 'X', 'x', 'X']
# col1 = [" ", " ", " ", " ", " ", " "]

# x = [col0, col1]
# rows = []
# for i in range(2):
#     row = []
#     for col in x:
#         row.append(col.pop(0))
#     rows.append(row)
# print(rows)

# for i in rows:
#     print(i)

board = [["x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["x", "x", "x", "X", "x", "x", "x"],
        ["x", "x", "X", "x", "x", "x", "x"],
        ["x", "X", "x", "x", "x", "x", "x"],
        ["X", "x", "x", "x", "x", "x", "x"]]

intervels = ["|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|", " ", "|"]
underlines = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]

# output = ""
# for i in range(12):
#     if i % 2 == 0:
#         index = 0
#         for j in range(15):
#             if j % 2 == 0:
#                 output += "|"
#             else:
#                 output +=

# x = {(0, 0): 0, (0, 1): 1}
# for i in x:
#     if x[i] == 1:
#         print(i)