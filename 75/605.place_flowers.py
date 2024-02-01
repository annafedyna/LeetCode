def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    k = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0)and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            k += 1
            flowerbed[i] = 1
             
    return k >= n

print(canPlaceFlowers([1,0,0,0,0,1], 2))