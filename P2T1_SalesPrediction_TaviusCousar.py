#Sales Prediction Program Excercise
#02/13/2019
#CTI-110 P2T1 - Sales Prediction
#Tavius Cousar
#
#Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

#Calculate the profit s 23 percent of tottal sales.
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit, ',.2f'), sep='')
