#-----------------------
# Step 1: import libraries
#-----------------------
import pandas as pd
import matplotlib.pyplot as plt 



#-----------------------
# Step 3: load dataset
#-----------------------
df = pd.read_csv("outputs/analyzed_call_center_data.csv")



#-----------------------
# Step 3: Scater plot
#-----------------------
# to show relationship between answer speed and service level

plt.scatter(df["answer_speed_(avg)"], df["service_level_(20_seconds)"])

plt.title("Answer Speed vs Service Level")
plt.xlabel("Answer Speed (seconds)")
plt.ylabel("Service Level (%)")

plt.show()



#-----------------------
#Step 4: Scatter plot - waiting time
#-----------------------
plt.scatter(df["waiting_time_(avg)"], df["service_level_(20_seconds)"])

plt.title("Waiting Time vs Service Level")
plt.xlabel("Waiting Time (seconds)")
plt.ylabel("Service Level (%)")

plt.show()