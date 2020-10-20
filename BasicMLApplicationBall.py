from sklearn import tree

def AppProcess(weight,surface) :
	BallFeatures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]

	Name = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]
	
	clf = tree.DecisionTreeClassifier()
	
	clf = clf.fit(BallFeatures,Name)
	
	result = clf.predict([[weight,surface]])

	if result == 1 :
		print("Your object looks like a Tennis ball")
	elif result == 2 :
		print("Your object looks like a Cricket ball")
	

def main():
	
	print("Basic Machine Learning Application By Ashish Shinde")
	
	print("Enter weight of object :")
	weight = input()

	print("What is the surface of object rough or smooth :")
	surface = input()

	if surface.lower() == "rough" :
		surface = 1
	elif surface.lower() =="smooth" :
		surface = 0
	else :
		print("****Error : Invalid Input****")
		exit()

	AppProcess(weight,surface)

if __name__ == "__main__":
	main()
