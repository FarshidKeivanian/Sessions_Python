# Lambda Function to calculate the total number of animals seen
total_animals = lambda sightings: sum(sightings.values())

# Recursive Function to find the total number of distinct species
def count_species(species_list):
    if not species_list:
        return 0
    else:
        first, *rest = species_list
        if isinstance(first, list):
            return count_species(first) + count_species(rest)
        else:
            return 1 + count_species(rest)

# Pass by Reference to add new species sightings
def add_sighting(sightings, species, count):
    if species in sightings:
        sightings[species] += count
    else:
        sightings[species] = count

# Example Data
sightings = {
    'Kangaroo': 150,
    'Koala': 75,
    'Dingo': 40
}

# Add new sightings
add_sighting(sightings, 'Emu', 30)
add_sighting(sightings, 'Kangaroo', 20)

# Nested list of species for counting distinct species
species_nested_list = ['Kangaroo', ['Koala', 'Dingo'], ['Emu', ['Wombat', 'Wallaby']]]

# Outputs
print("Total number of animals sighted:", total_animals(sightings))
print("Total distinct species counted:", count_species(species_nested_list))
print("Updated sightings:", sightings)
