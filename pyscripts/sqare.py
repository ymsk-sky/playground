# 矩形が重なっているかの判定

# x軸は右側が+, y軸は下側が+ : numpy等と同じ/直交座標のy軸が反転した感じ
# ((左上x, 左上y), (右下x, 右下y))
r1 = ((10, 10), (80, 80))
r2 = ((40, 40), (100, 100))

def has_intersect(r1, r2):
    r1_x0, r1_y0 = r1[0]
    r1_x1, r1_y1 = r1[1]
    r2_x0, r2_y0 = r2[0]
    r2_x1, r2_y1 = r2[1]
    max1 = max(r1_x0, r2_x0)  # 小さいほうのx
    min1 = min(r1_x1, r2_x1)  # 大きいほうのx
    max2 = max(r1_y0, r2_y0)  # 小さいほうのy
    min2 = min(r1_y1, r2_y1)  # 大きいほうのy
    return max1 <= min1 and max2 <= min2

print(has_intersect(r1, r2))

print("----")

l = (
    (((0, 0), (10, 10)), ((20, 20), (40, 40))),  # 外: False
    (((0, 0), (100, 100)), ((20, 20), (40, 40))),  # 中に入っている: True
    (((50, 0), (100, 50)), ((0, 50), (50, 100))),  # ／: True
)
for r1, r2 in l:
    print(has_intersect(r1, r2))
