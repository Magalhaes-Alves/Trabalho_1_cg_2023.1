from classes.Window import Window

janela = Window(500,500,"Teste")

#janela.drawEllipse(250, 250, 50, 100, (255, 255, 255))

janela.drawCircle(250,250,70,(255,255,255))

janela.bresenham(10, 10, 200, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 10, (255, 255, 255))
janela.bresenham(10, 10, 10, 200, (255, 255, 255))
janela.bresenham(10, 10, 200, 90, (255, 255, 255))
janela.bresenham(10, 10, 90, 200, (255, 255, 255))


""" janela.ddaLine(10, 10, 200, 200, (255, 255, 255))
janela.ddaLine(10, 10, 200, 10, (255, 255, 255))
janela.ddaLine(10, 10, 10, 200, (255, 255, 255))
janela.ddaLine(10, 10, 200, 90, (255, 255, 255))
janela.ddaLine(10, 10, 90, 200, (255, 255, 255))
 """

janela.floodFill(250,250, (0,0,255), (0,0,0))
janela.show()

