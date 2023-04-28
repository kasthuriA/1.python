#Create function
class MultipleFunctions():
    
        def subfields():
            sub_fields = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
            print("Sub-fields in AI are:")
            print( sub_fields[0])
            for sub_field in sub_fields[1:]:
                print(sub_field)

        def oddEven():
                num=int(input("Enter the number:"))
                if((num%2)==1):
                     print(num,"is an odd number")

                else:
                     print(num,"is an Even number")

        def percentage():
                subject1 = float(input("Subject 1= "))
                subject2 = float(input("Subject 2= "))
                subject3 = float(input("Subject 3= "))
                subject4 = float(input("Subject 4= "))
                subject5 = float(input("Subject 5= "))

        # Calculate the total score and percentage
                total_score = subject1 + subject2 + subject3 + subject4 + subject5
                percentage = (total_score / 500) * 100
                print ("Total:",total_score)
                # Print the percentage
                print("Percentage: {:.2f}%".format(percentage))

        def triangle():
                Height = int(input("Height= "))
                Breadth = int(input("Breadth= "))
                areaFormula=(Height*Breadth)/2
                print("AreaFormula=(Height*Breadth)/2")
                print("Area of Triangle : ",areaFormula)
                Height1 = int(input("Height= "))
                Height2 = int(input("Height2= "))
                Breadth = int(input("Breadth= "))
                PerimeterFormula=Height1+Height2+Breadth
                print("PerimeterFormula=Height1+Height2+Breadth")
                print("Perimeter of Triangle : ",PerimeterFormula)
