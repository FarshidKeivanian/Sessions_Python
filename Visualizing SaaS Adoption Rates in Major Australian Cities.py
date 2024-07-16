import matplotlib.pyplot as plt

# Data for SaaS adoption rates in different cities
cities = ['Sydney', 'Melbourne', 'Brisbane', 'Canberra']
adoption_rates = [75, 70, 65, 80]  # hypothetical percentages

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(cities, adoption_rates, color=['blue', 'orange', 'green', 'red'])
plt.title('SaaS Adoption Rates in Major Australian Cities')
plt.xlabel('Cities')
plt.ylabel('Adoption Rate (%)')
plt.ylim(0, 100)

# Adding value labels on top of the bars
for i in range(len(cities)):
    plt.text(i, adoption_rates[i] + 2, str(adoption_rates[i]) + '%', ha='center')

plt.show()
