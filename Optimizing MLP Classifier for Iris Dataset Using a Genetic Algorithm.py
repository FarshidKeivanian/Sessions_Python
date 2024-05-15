import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import random
import matplotlib.pyplot as plt

# Load data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Define the genetic algorithm
class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self._initialize_population()

    def _initialize_population(self):
        return [self._create_chromosome() for _ in range(self.population_size)]

    def _create_chromosome(self):
        return {
            'learning_rate': 10**np.random.uniform(-5, -1),
            'hidden_layer_sizes': (random.randint(1, 100), random.randint(1, 100)),
            'activation': random.choice(['logistic', 'tanh', 'relu'])
        }

    def _fitness(self, chromosome):
        model = MLPClassifier(
            learning_rate_init=chromosome['learning_rate'],
            hidden_layer_sizes=chromosome['hidden_layer_sizes'],
            activation=chromosome['activation'],
            max_iter=1000
        )
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        return accuracy_score(y_test, predictions)

    def _select(self):
        fitness_scores = [(chromosome, self._fitness(chromosome)) for chromosome in self.population]
        fitness_scores.sort(key=lambda x: x[1], reverse=True)
        self.population = [chromosome for chromosome, score in fitness_scores[:self.population_size//2]]
        return fitness_scores[0]

    def _crossover(self, parent1, parent2):
        child = parent1.copy()
        for key in parent1.keys():
            if random.random() < self.crossover_rate:
                child[key] = parent2[key]
        return child

    def _mutate(self, chromosome):
        for key in chromosome.keys():
            if random.random() < self.mutation_rate:
                if key == 'learning_rate':
                    chromosome[key] = 10**np.random.uniform(-5, -1)
                elif key == 'hidden_layer_sizes':
                    chromosome[key] = (random.randint(1, 100), random.randint(1, 100))
                elif key == 'activation':
                    chromosome[key] = random.choice(['logistic', 'tanh', 'relu'])

    def run(self):
        best_chromosome = None
        best_score = 0
        fitness_over_generations = []
        for generation in range(self.generations):
            self._select()
            next_generation = self.population.copy()
            while len(next_generation) < self.population_size:
                parent1, parent2 = random.sample(self.population, 2)
                child = self._crossover(parent1, parent2)
                self._mutate(child)
                next_generation.append(child)
            self.population = next_generation
            best_chromosome, best_score = self._select()
            fitness_over_generations.append(best_score)
            print(f'Generation {generation + 1}: Best Accuracy = {best_score:.4f}')
        plt.plot(fitness_over_generations, label='GA')
        plt.xlabel('Generation')
        plt.ylabel('Best Accuracy')
        plt.title('Accuracy over Generations')
        return best_chromosome, best_score

# Run without genetic algorithm
default_model = MLPClassifier(max_iter=1000, random_state=42)
default_model.fit(X_train, y_train)
default_predictions = default_model.predict(X_test)
default_accuracy = accuracy_score(y_test, default_predictions)
print(f'Default Model Accuracy: {default_accuracy:.4f}')

# Run the genetic algorithm
ga = GeneticAlgorithm(population_size=20, generations=50, mutation_rate=0.1, crossover_rate=0.5)
best_params, best_accuracy = ga.run()
plt.axhline(y=default_accuracy, color='r', linestyle='-', label='Default Model')
plt.legend()
plt.show()
print(f'Best Parameters: {best_params}')
print(f'Best Accuracy: {best_accuracy:.4f}')
