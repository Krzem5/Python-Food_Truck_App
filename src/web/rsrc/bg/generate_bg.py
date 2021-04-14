from PIL import Image
import random



IMAGES=["burger.png","burgerCheese.png","burgerCheeseDouble.png","burgerDouble.png","chinese.png","chinese.png","chinese.png","chinese.png","sodaBottle.png","sodaBottle.png","sodaBottle.png","sodaBottle.png","taco.png","taco.png","taco.png","taco.png","fries.png","fries.png","fries.png","fries.png"]
SIZE=256
MIN_SCALE=4
MAX_SCALE=6



il=[]
for k in IMAGES:
	il.append(Image.open(k).convert("RGBA"))
o=Image.new("RGBA",(SIZE,SIZE))
for _ in range(0,1000):
	tmp=il[random.randint(0,len(il)-1)]
	sc=random.random()*(MAX_SCALE-MIN_SCALE)+MIN_SCALE
	tmp=tmp.resize((int(tmp.width/sc),int(tmp.height/sc))).rotate(random.randint(0,360),expand=True)
	x=random.randint(0,SIZE)
	y=random.randint(0,SIZE)
	for i in range(-1,2):
		for j in range(-1,2):
			o.paste(tmp,(x+i*SIZE,y+j*SIZE),tmp)
m=Image.new("RGBA",(SIZE,SIZE),(180,180,180,25))
o.paste(m,(0,0),m)
o.save("background.png")
