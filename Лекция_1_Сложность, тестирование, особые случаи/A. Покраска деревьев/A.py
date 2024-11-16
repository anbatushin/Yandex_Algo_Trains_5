p, v = map(int, input().split())
q, m = map(int, input().split())

p_left, p_right = p - v, p + v
q_left, q_right = q - m, q + m

if ((q_left <= p_left <= q_right) or
        (q_right >= p_right >= q_left) or
        (p_left <= q_left and p_right >= q_right)):

    result = max(p_right, q_right) - min(p_left, q_left) + 1
else:
    result = p_right + q_right - p_left - q_left + 2

print(result)
