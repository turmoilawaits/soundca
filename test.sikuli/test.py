"""
reg = Region(Region(85,152,131,56))
reg.highlight()
wait(5)
k = reg.inside().text()
#foundText = find(Pattern("region.png").similar(0.90).targetOffset(-2,4)).text()

print k


retg = Region(Region(86,509,174,174))

retg.highlight()
wait(10)
"""
targetImage = "ds.png"
def specialClick():
  mouseMove(targetImage) # move to target
  wait(0.3) # hover for 300 msecs
  mouseDown(Button.LEFT) # press and hold left button
  wait(0.1) # wait 100 msecs
  mouseUp() # release button again

specialClick()  