from PIL import Image, ImageDraw
from mandelbrot import mandelbrot

def plotMandelbrot(RE_START, RE_END, IM_START, IM_END, WINDOW_WIDTH, WINDOW_HEIGHT, MAX_ITER, RENDER_SCALE):
        WIDTH = int(WINDOW_WIDTH * RENDER_SCALE)
        HEIGHT = int(WINDOW_HEIGHT * RENDER_SCALE)
        im = Image.new("HSV", (WIDTH, HEIGHT), (0,0,0))
        draw = ImageDraw.Draw(im)

        for x in range(0, WIDTH):
                for y in range(0, HEIGHT):
                        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                                IM_START + (y / HEIGHT) * (IM_END - IM_START))
                        m = mandelbrot(c, MAX_ITER)
                        hue = int(255 * m / MAX_ITER)
                        saturation = 255
                        value = 255 if m < MAX_ITER else 0
                        draw.point([x, HEIGHT - y], (hue, saturation, value))
                
        im = im.resize((WINDOW_WIDTH, WINDOW_HEIGHT),Image.BICUBIC)
        im.convert('RGB').save('output.png', 'PNG')