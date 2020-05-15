import math


def solve():
	w, h, l, u, r, d = [int(it) for it in input().split()]
	size = w if w > h else h
	nn = [0]
	for ii in range(1, 2 * size):
		# nn[i] = log2(i!)
		nn.append(nn[ii - 1] + math.log2(ii))

	def pp(xx, yy):
		if xx == 1 and yy == 1:
			return 1
		elif xx == 1:
			return pow(0.5, yy - 1)
		elif yy == 1:
			return pow(0.5, xx - 1)
		elif xx == w:
			return pp(xx - 1, yy) * 0.5 + pp(xx, yy - 1)
		elif yy == h:
			return pp(xx - 1, yy) + pp(xx, yy - 1) * 0.5
		else:
			return pow(0.5, xx + yy - 2) * (
				pow(2, nn[xx + yy - 2] - nn[yy - 1] - nn[xx - 1])
			)

	total_p = 0
	x, y = r + 1, u - 1
	while x <= w and y >= 1:
		total_p += pp(x, y)
		x += 1
		y -= 1
	x, y = l - 1, d + 1
	while x >= 1 and y <= h:
		total_p += pp(x, y)
		x -= 1
		y += 1

	return "{:.5f}".format(total_p)


if __name__ == '__main__':
	cases = int(input())
	for i in range(cases):
		ans = solve()
		print("Case #{}: {}".format(i + 1, ans))
