
import statistics
import numpy as numpy
import pandas as pandas
data_set = []
data_set_input = float(input("Enter the data-set one number at a time: "))
data_set.append(data_set_input)


print(data_set)

def operation_selection():
        
        operation =  input("Select an operation:" "\n"
                         "1: mean" "\n"
                         "2: median" "\n"
                         "3. range" "\n"
                         "4. Interquartile range" "\n"
                         "5. Standard Deviation" "\n"
                         "6. Outliers \n") 
        
        if operation == '1':
            
            answer = statistics.mean(data_set)
            print("the mean is: " + str(answer))
            operation_selection()
        
        elif operation == "2":
           
            answer = statistics.median(data_set)
            print("the median is: " + str(answer))
            operation_selection()
       
        elif operation == '3':
            
            answer = max(data_set) - min(data_set)
            print("the range is: " + str(answer))
            operation_selection()
        
        elif operation == '4':
             
             half_list = len(data_set) // 2
             q1 = statistics.median(data_set[0 : half_list])
             q3 = statistics.median(data_set[half_list + 1 :])
             answer = q3 -q1
             print("Quartile 3 is : " +str(q3) + "\n")
             print("Quartile 1 is : " + str(q1) + "\n")
             print("the interquartile range is: " + str(answer))
             operation_selection()

        elif operation == '5':
            
            answer = statistics.stdev(data_set)
            print("The standard deviation is: " + str(answer))
            operation_selection()

        elif operation == '6':
            
            half_list = len(data_set) // 2
            q1 = statistics.median(data_set[0 : half_list])
            q3 = statistics.median(data_set[half_list + 1 :])
            IQR = q3 - q1
            low_outlier = q1 - 1.5 * IQR
            high_outlier = q3 + 1.5 * IQR
            answer = print("Low Outlier: " + str(low_outlier) + "\n"
                           "High Outlier: " +str(high_outlier) + "\n")
            operation_selection()
        
        else:
            

            operation_selection()


for data_set_input in data_set:
   
    try:
       
       data_set_input = float(input("Enter the next number: "))
       
       data_set.append(data_set_input)
       data_set.sort()
       print(data_set)

    except:
        
        operation_selection()
  
