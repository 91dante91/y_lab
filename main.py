point_1 = (0, 2)
point_2 = (2, 5)
point_3 = (5, 2)
point_4 = (6, 6)
point_5 = (8, 3)

start_point = point_1
points = {"(2, 5)": (2, 5),
          "(5, 2)": (5, 2),
          "(6, 6)": (6, 6),
          "(8, 3)": (8, 3)
          }
string_len = {}
result = f"{start_point}"
step = len(points)
total_dist = 0

while True:
    for point in points.values():
        if start_point != point:
            distance = ((point[0] - start_point[0]) ** 2 + (point[1] - start_point[1]) ** 2) ** 0.5
            string_len.update({f"{point}": distance})
    step -= 1
    nearest_point = min(string_len, key=string_len.get)
    dist_nearest_point = string_len.get(min(string_len, key=string_len.get))
    total_dist += dist_nearest_point
    result += f" -> {nearest_point}[{dist_nearest_point}]"
    start_point = points.get(nearest_point)
    string_len = {}
    if step == 0:
        last_dist = ((start_point[0] - point_1[0]) ** 2 + (start_point[1] - point_1[1]) ** 2) ** 0.5
        total_dist += last_dist
        result += f" -> {point_1}[{last_dist}] = {total_dist}"
        break

print(result)
