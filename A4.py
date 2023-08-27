import numpy 
import pandas 
from matplotlib import pyplot

dataframe = pandas.read_excel(r"Lab Session1 Data.xlsx",sheet_name="IRCTC Stock Price")

price_data = dataframe['Price']

mean = numpy.mean(price_data)
variance = numpy.var(price_data)

print('Mean:', mean)
print('Variance:', variance)

wednesday_data = price_data[dataframe['Day'] == 'Wed']
sample_mean = numpy.mean(wednesday_data)

print('Sample mean:', sample_mean)

april_data = price_data[dataframe['Month'] == 'Apr']

april_mean = numpy.mean(april_data)

print('April mean:', april_mean)

chg_data = dataframe['Chg%']

is_loss = numpy.where(chg_data > 0, False, True)

probability_of_loss = numpy.mean(is_loss)

print('Probability of making a loss:', probability_of_loss)

wednesday_data = dataframe[dataframe['Day'] == 'Wed']

probability_of_profit_on_wednesday = numpy.mean(wednesday_data['Chg%'] > 0)

print('Probability of making a profit on Wednesday:', probability_of_profit_on_wednesday)

probability_of_wednesday = numpy.mean(dataframe['Day'] == 'Wed')

conditional_probability = probability_of_profit_on_wednesday / probability_of_wednesday

print('Conditional probability of making a profit, given that today is Wednesday:', conditional_probability)

pyplot.scatter(dataframe['Day'], dataframe['Chg%'])
pyplot.xlabel('Day')
pyplot.ylabel('Chg%')
pyplot.title('Chg% vs Day')
pyplot.show()