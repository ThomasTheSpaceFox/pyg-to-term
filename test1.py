#!/usr/bin/env python
import pygame
import pygtotermlib as ptl
import time

pygame.display.init()
picture=pygame.image.load("test.png")

#color space tests
print(ptl.bwaa(picture, shadinterpol=0))
time.sleep(1)
print(ptl.bwaa(picture, shadinterpol=1))
time.sleep(1)
print(ptl.bwaa24(picture))
time.sleep(1)
print(ptl.colaa(picture, shadinterpol=0, colorinterpol=0))
time.sleep(1)
print(ptl.colaa(picture, shadinterpol=0, colorinterpol=1))
time.sleep(1)
print(ptl.colaa(picture, shadinterpol=1, colorinterpol=0))
time.sleep(1)
print(ptl.colaa(picture, shadinterpol=1, colorinterpol=1))
time.sleep(1)
print(ptl.colaa216(picture))
time.sleep(1)
print(ptl.colaa24bit(picture))

