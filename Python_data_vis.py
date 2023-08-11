#!/usr/bin/env python
# coding: utf-8

# # Python Data Visualization Exercises

# ### Intro
# These exercises are intended to show foundational knowledge of Python data visualization using pandas and matplotlib. The following items are covered in the examples below:
# * Line Graph
# * Bar Graph
# * Scatterplot
# * Pie Chart
# * Unstacked Bar Graph
# * Subplot
# * Stack Plot
# * Various graph settings (labels, grid, color, style, legend)

# In[20]:


# import data
import pandas as pd
salesdata = pd.read_csv('/Users/nklpu/OneDrive/Desktop/Python Data Vis/company_sales_data.csv')

# verify data imported correctly
salesdata


# In[21]:


# exercise 1: Create a line graph showing profit v month with main label and axis labels
import matplotlib.pyplot as plt
plt.plot(salesdata.month_number, salesdata.total_profit)
plt.title('Total Profit per Month')
plt.xlabel('Month')
plt.ylabel('Total Profit')


# In[33]:


# exercise 2: Change the style and color of the line on the previous graph, add legend in the bottom right, and add data point makers
plt.plot(salesdata.month_number, salesdata.total_profit, linestyle="--", color = 'Red', label = 'Total Profit', marker = '.')
plt.title('Total Profit per Month')
plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.legend(loc = 4)


# In[23]:


# exercise 3: Add all product sales data to line graph, remove total profit, and update legend.
plt.plot(salesdata.month_number, salesdata.facecream, label = 'Face Cream')
plt.plot(salesdata.month_number, salesdata.facewash, label = 'Face Wash')
plt.plot(salesdata.month_number, salesdata.toothpaste, label = 'Toothpaste')
plt.plot(salesdata.month_number, salesdata.bathingsoap, label = 'Bathing Soap')
plt.plot(salesdata.month_number, salesdata.shampoo, label = 'Shampoo')
plt.plot(salesdata.month_number, salesdata.moisturizer, label = 'Moisturizer')
plt.legend()
plt.title('Total Profit per Month by Product')
plt.xlabel('Month')
plt.ylabel('Profit')


# In[45]:


# exercise 4: Create a scatterplot of toothpaste sales v month. Add legend, gridlines, main title, and axis titles.
plt.scatter(salesdata.month_number, salesdata.toothpaste, label = 'Toothpaste Profit')
plt.grid(True, linestyle = '--')
plt.xticks(salesdata.month_number)
plt.title('Total Toothpaste Profit per Month')
plt.xlabel('Month')
plt.ylabel('Total Toothpaste Profit')
plt.legend()


# In[90]:


# exercise 5: Create a bar chart of sales units in numbers v month. 
# There should be one bar for each month for face cream and face wash.
monthbar  = salesdata['month_number'].tolist()
facecreambar  = salesdata['facecream'].tolist()
facewashbar  = salesdata['facewash'].tolist()
plt.bar([a-0.25 for a in monthbar], facecreambar, label = 'Face Cream', align = 'edge', width= 0.25)
plt.bar([a+0.25 for a in monthbar], facewashbar, label = 'Face Wash', align = 'edge', width= -0.25)
plt.legend()
plt.xlabel('Month')
plt.ylabel('Sales units in numbers by product')
plt.title('Product Sales Units in Numbers by Month')


# In[93]:


# exercise 6: Create a bar chart of bathing soap by month. Add gridlines, main title, and axis titles.
bathbar  = salesdata['bathingsoap'].tolist()
plt.bar([a-0.25 for a in monthbar], bathbar)
plt.title('Bathing Soap Sales by Month')
plt.xlabel('Month')
plt.ylabel('Bathing Soap Unit Sales')
plt.grid(True)


# In[117]:


# exercise 7: Create a pie chart showing total sales for the year by product.
sales2 = salesdata.sum()
sales2[1:7]
labspie = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]
import numpy as np
piedata = np.array(sales2[1:7])
plt.pie(piedata, labels = labspie, autopct='%1.1f%%')
plt.legend(bbox_to_anchor = (0,1))


# In[136]:


# exercise 8: Plot Bathing soap v facewash for all months using the Subplot
soapray  = salesdata['bathingsoap'].tolist()
faceray  = salesdata['facewash'].tolist()
moray = salesdata['month_number'].tolist()
f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(moray, soapray, label = 'Bathing Soap')
axarr[0].set_title('Bathing Soap Sales')
axarr[1].plot(moray, faceray, label = 'Face Wash')
axarr[1].set_title('Face Wash Sales')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()


# In[123]:


# exercise 9: Read all product sales data and show it using the stack plot
plt.stackplot(salesdata.month_number, salesdata.toothpaste, salesdata.facewash, salesdata.facecream, salesdata.moisturizer, salesdata.shampoo, salesdata.bathingsoap)
plt.legend(["Toothpaste", "Face Wash", "Face Cream", "Moisturizer", "Shampoo", "Bathing Soap"])
plt.xlabel("Month")
plt.ylabel("Product Sales by Unit")
plt.title("Product Sales Date by Month")


# #### Appendix
# The data used to create these visualizations can be found in the repository. It was taken from a publically available Python exercise website: https://pynative.com/python-matplotlib-exercise/

# #### Created by: Nickie Norris 
# #### August 10, 2023
