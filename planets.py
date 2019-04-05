def weight_on_planets():
   EWeight = int(input("What do you weigh on earth? "))

   MWeight = EWeight * 0.38
   JWeight = EWeight * 2.34

   print("\nOn Mars you would weigh {} pounds.\nOn Jupiter you would weigh {} pounds.".format(MWeight, JWeight))
   
   
if __name__ == '__main__':
   weight_on_planets()
