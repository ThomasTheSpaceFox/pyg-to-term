#!/usr/bin/env python
# coding=utf-8
import os
import pygame


#pygtotermlib is a library for converting pygame surfaces to terminal block graphics.

#usage of the bwaa* and colaa* functions are as follows:

#bwaa(surface) -> string
#colaa(surface) -> string

#"surface" should be a pygame surface already at the desired resolution in lines and columns.

#the basic bwaa(surface) and colaa(surface) have an optional shade-interoplation option:
#bwaa(surface, shadinterpol=1)

#in addition, colaa(surface) has a separate interpolation option for color:
#colaa(surface, shadinterpol=1, colorinterpol=1)

#if you want a staggered interpolation, ensure "columns" (surface width) is even.
#likewise, for striped interpolation, ensure the width is odd.


#utf-8 terminal REQUIRED
#bwaa* functions are monochrome
#colaa*functions are color
#bwaa(surface) and colaa(surface) use escape sequences most terminals support. 


#bwaa24 and colaa216 use less common but more-capable 256-color mode escape sequences. terminals are less likely to support these. so:
#provide options in programs that use this library to enable/disable 256-color-mode (24-shade & 216-color) escape sequence color.

#colaa24bit uses 24bit RGB color escape sequences. these are, like the 256-color mode escape sequences, less likely to work.


#Notes:
# - while color is nice, you may find colla(surface) isn't worth the cpu time over bwaa(surface) in this scenario.
# - bwaa(surface) is usually the fastest choice, 
# - bwaa(surface) only needs basic cursor escape sequences and UTF-8 support. 
#        it only uses 2 escape sequences to ensure the terminal has a black background and white text for best appearance.

#requires unicode & curser-position-escape-sequence capable terminal.
def bwaa(surface, shadinterpol=0 ,colorindex=1, borderlevel1=51, borderlevel2=102, borderlevel3=153, borderlevel4=204):
	height=surface.get_height()
	defwidth=surface.get_width()
	DEF=('\033[0;40m\033[1;37m')
	strblock=DEF
	shadbias=0
	if shadinterpol:
		shadbias=20
	#strblock=""
	for ypos in xrange(0, height-1):
		for xpos in xrange(0, defwidth-1):
			if shadbias==-20:
				shadbias=20
			elif shadbias==20:
				shadbias=-20
			indexcolor=surface.get_at((xpos, ypos))
			#indexval=indexcolor[colorindex]
			indexval=(indexcolor[0]+indexcolor[1]+indexcolor[2])//3
			if indexval<borderlevel1-shadbias:
				#strblock+="█"
				strblock+=" "
			elif indexval<borderlevel2-shadbias:
				strblock+="░"
			elif indexval<borderlevel3-shadbias:
				strblock+="▒"
			elif indexval<borderlevel4-shadbias:
				strblock+="▓"
			else:
				#strblock+=" "
				strblock+="█"
		strblock+="\n"
	
	return strblock




#requres advanced 24-shade greyscale escape sequence support.
def bwaa24(surface):
	height=surface.get_height()
	defwidth=surface.get_width()
	DEF=('\033[0;40m\033[1;37m')
	strblock=DEF
	#strblock=""
	for ypos in xrange(0, height-1):
		for xpos in xrange(0, defwidth-1):
			indexcolor=surface.get_at((xpos, ypos))
			#indexval=indexcolor[colorindex]
			indexval=(indexcolor[0]+indexcolor[1]+indexcolor[2])//3
			rangeval=(((indexval- 0 ) * (255 - 232) / (255 - 0)) + 232)
			strblock+=("\033[0;48;5;"+str(rangeval)+"m")
			strblock+=" "
		strblock+="\033[0m\n"
	
	return strblock
#requires 216-tone color escape sequence support.
def colaa216(surface):
	height=surface.get_height()
	defwidth=surface.get_width()
	DEF=('\033[0;40m\033[1;37m')
	strblock=DEF
	#strblock=""
	for ypos in xrange(0, height-1):
		for xpos in xrange(0, defwidth-1):
			indexcolor=surface.get_at((xpos, ypos))
			#indexval=indexcolor[colorindex]
			r=(((indexcolor[0] - 0 ) * (5 - 0) / (255 - 0)) + 0)
			g=(((indexcolor[1] - 0 ) * (5 - 0) / (255 - 0)) + 0)
			b=(((indexcolor[2] - 0 ) * (5 - 0) / (255 - 0)) + 0)
			rangeval=(16 + 36 * r + 6 * g + b)
			#indexval=(indexcolor[0]+indexcolor[1]+indexcolor[2])//3
			#rangeval=(((indexval- 0 ) * (255 - 232) / (255 - 0)) + 232)
			strblock+=("\033[0;48;5;"+str(rangeval)+"m")
			strblock+=" "
		strblock+="\033[0m\n"
	
	return strblock

def colaa24bit(surface):
	height=surface.get_height()
	defwidth=surface.get_width()
	DEF=('\033[0;40m\033[1;37m')
	strblock=DEF
	#strblock=""
	for ypos in xrange(0, height-1):
		for xpos in xrange(0, defwidth-1):
			indexcolor=surface.get_at((xpos, ypos))
			#indexval=indexcolor[colorindex]
			#indexval=(indexcolor[0]+indexcolor[1]+indexcolor[2])//3
			#rangeval=(((indexval- 0 ) * (255 - 232) / (255 - 0)) + 232)
			strblock+=("\033[0;48;2;"+str(indexcolor[0])+ ";" +str(indexcolor[1]) + ";" + str(indexcolor[2]) + "m")
			strblock+=" "
		strblock+="\033[0m\n"
	return strblock


def colpick(color, colorbias):
	if colorbias==1:
		chanlevel=170
	elif colorbias==0:
		chanlevel=90
	else:
		chanlevel=127
		
	if color[0]<chanlevel:
		r=0
	else:
		r=1
	if color[1]<chanlevel:
		g=0
	else:
		g=1
	if color[2]<chanlevel:
		b=0
	else:
		b=1
	if r and g and b:
		return ('\033[0;40m\033[1;37m')
	if not r and not g and not b:
		return ('\033[0;40m\033[1;37m')
	if r and not g and not b:
		return ('\033[0;40m\033[0;31m')
	if r and g and not b:
		return ('\033[0;40m\033[0;33m')
	if r and not g and b:
		return ('\033[0;40m\033[0;35m')
	if not r and not g and b:
		return ('\033[0;40m\033[0;34m')
	if not r and g and b:
		return ('\033[0;40m\033[0;36m')
	if not r and g and not b:
		return ('\033[0;40m\033[0;32m')
	#return ('\033[0;40m\033[1;37m')
#requires basic color escape sequence support in terminal.
def colaa(surface, shadinterpol=0, colorinterpol=0, colorindex=1, borderlevel1=51, borderlevel2=102, borderlevel3=153, borderlevel4=204):
	height=surface.get_height()
	defwidth=surface.get_width()
	DEF=('\033[0;40m\033[1;37m')
	strblock=DEF
	if colorinterpol:
		colorbias=0
	else:
		colorbias=2
	shadbias=0
	if shadinterpol:
		shadbias=20
	for ypos in xrange(0, height-1):
		for xpos in xrange(0, defwidth-1):
			if colorinterpol:
				if colorbias:
					colorbias=0
				else:
					colorbias=1
			if shadbias==-20:
				shadbias=20
			elif shadbias==20:
				shadbias=-20
			indexcolor=surface.get_at((xpos, ypos))
			#indexval=indexcolor[colorindex]
			indexval=(indexcolor[0]+indexcolor[1]+indexcolor[2])//3
			COL=colpick(indexcolor, colorbias)
			if indexval<borderlevel1-shadbias:
				#strblock+="█"
				strblock+=COL+" "
			elif indexval<borderlevel2-shadbias:
				strblock+=COL+"░"
			elif indexval<borderlevel3-shadbias:
				strblock+=COL+"▒"
			elif indexval<borderlevel4-shadbias:
				strblock+=COL+"▓"
			else:
				#strblock+=" "
				strblock+=COL+"█"
		strblock+="\033[0m\n"
	
	return strblock

