def mandelbrot(c, MAX_ITER):
    z = 0
    n = 0
    while(abs(z) <= 2 and n < MAX_ITER):
        z = z * z + c
        n += 1
    return n