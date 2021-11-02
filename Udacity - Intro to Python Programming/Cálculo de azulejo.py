''' In this quiz you're going to do some calculations for a tiler. 
Two parts of a floor need tiling. 
One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. 
Tiles come in packages of 6. 
1 - How many tiles are needed? 
2 - You buy 17 packages of tiles containing 6 tiles each. 
How many tiles will be left over?
'''
#Expression that calculates how many tiles are needed

def tilesneeded (w,l):
    return w * l

tiles = tilesneeded(9,7) + tilesneeded(5,7)

print(tiles)

#Expression that calculates how many tiles will be left over

tiles_package = 6

remainder = tiles % tiles_package

left_over = tiles_package - remainder

print(left_over)

'''
Solution: Calculate 
print(9*7 + 5*7)
print(17*6 - (9*7 + 5*7))
'''