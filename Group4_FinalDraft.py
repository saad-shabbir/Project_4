
"""Code written by Saad Shabbir and Cam Heitkamp for Professor Tom Mattson's Machine Learning for Business Analyst"""

# STEP ONE: We first start by importing all the necessary python functions to properly run our script!
import statistics
import math
import csv
import random
import json


# STEP TWO: We then welcome the user with a message and tell them the purpose of this script.
def welcome_message():
    """Prints a welcome message to the user explaining the purpose of the tool."""
    print('Welcome! This tool helps to score international markets for potential expansion!')


# STEP THREE: We then created a function 'user_input' in order to gather a specific user-chosen number of iterations
# for the simulation that we will later be running to generate data for each country!
def user_input():
    """Prompts the user for the number of iterations for the simulation. Ensures the input is between 500 and 25,000
    and is an integer. Then returns an integer which is the number of iterations provided by the user. If the entered
    number is not between 500 and 25,000 then a corresponding message will be printed to the user, however, if there is a
    float string or boolean input rather than an integer then there will be a corresponding ValueError message printed."""

    while True:
        try:
            num = int(input('First, Please Enter the number of desired iterations (must be between 500 and 25,000): '))
            if 500 <= num <= 25000:
                return num
            else:
                print(f'Please enter a value between 500 and 25,000.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')


# STEP FOUR: Loading the Data from a json file, 'Market_Scores'!
def load_json_data(file_name):
    """Loads data from the given JSON file."""
    with open(file_name, 'r') as handle:
        return json.load(handle)
# This part is identifying the .json file 'Market_Scores' and opening it in read mode so that data can be extracted


# STEP FIVE: This creates the function 'calculate_statistics' which, as the name implies, creates local variables that
# can be used to calculate the mean, stdev, median, min, max, and range of the RAW RESULTS for each country
def calculate_statistics(raw_results):
    """Calculates the statistical measures such as average, standard deviation, median, min, max, and range using the
    statistics function. Also returns the tuple raw_results which stores the numerical results of the input data."""
    avg = statistics.mean(raw_results)
    stdev = statistics.stdev(raw_results)
    median = statistics.median(raw_results)
    minimum = min(raw_results)
    maximum = max(raw_results)
    result_range = maximum - minimum
    return avg, stdev, median, minimum, maximum, result_range

# STEP SIX: This function writes the results to a pipe-delimited file as rounded numbers to the second decimal place
def write_results(results, filename):
    """Write the results to a pipe-delimited file with specified formatting. In this function, results is a list which
    contains the dictionaries with each countries results. The filename serves as the name of the output file and placing
    the raw results into a list so the simulation data can be easily extracted to check the results for each country"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['Country', 'Average', 'StDev', 'Median', 'Min', 'Max', 'Range', 'RawResults'])
        for result in results:
            raw_results_list = result['raw_results']
            writer.writerow([
                result['country'],
                result['average'],
                result['stdev'],
                result['median'],
                result['min'],
                result['max'],
                result['range'],
                raw_results_list
            ])



# STEP SEVEN: This function helped the user get the top/bottom reporting options that they desire
def get_top_bottom_count():
    """Prompts the user to select the number of top and bottom countries to display in the python console output. Note:
    This does not cause the results printed to the pipe-delimited text file to be only the prompted upper and lower
    bounds, all results for the 30 countries will be listed. By using a simple try and except block, our function makes
    sure that there are no numbers provided that are less than or greater than 10 reporting options."""
    while True:
        try:
            num = int(input('Enter the desired number of top and bottom reporting options (1-10): '))
            if 1 <= num <= 10:
                return num
            else:
                print('Please enter a number that is between 1 and 10.')
        except ValueError:
            print('Invalid input. Please make sure that the value is an integer!')




# STEP EIGHT: This function asks the user to then further decide what values they want to see in the metric format
def metric():
    """This function displays six different metrics options in which the user can choose from and returns dictionary
    mapping options to result keys. The dictionary created is what allows the user's input to correlate with the metric
    that is in the simulation's result dictionary."""
    metric_map = {
        'average': 'average',
        'standard deviation': 'stdev',
        'median': 'median',
        'minimum': 'min',
        'maximum': 'max',
        'range': 'range'
    }
    print('Please select a metric to report:')
    print('Options: Average, Standard Deviation, Median, Minimum, Maximum, Range \nEnter "Done" when finished.')
    return metric_map





# STEP NINE: This function, and ultimate point of the script, is to simulate the iterations given by the user and to
# then use the 5 previous functions to get varying values for the 30 different countries until ultimately uploading
# the results into a pipe-delimited-file where the user can then see the results they requested, as well as the raw
# results gathered within the simulation!
def run_simulation():
    """This function is entirely responsible for running the market simulation, calculating statistics, and providing
    results based on user inputs. It also handles input for the number of iterations, selected metrics, and top/bottom
    reporting. After it runs through the number of iterations provided and simulates accordingly, it asks the user if
    after the first set of metrics they would like to see more potential outcomes using other metrics. The user will
    continue to be prompted until they have entered 'done', when this occurs the simulation will then end and print the
    results to the txt file 'Market_Simulation_Results'. These results are for all 30 countries and not specific to the
    individual user inputs, aside from the number of iterations provided for the simulation data."""

    # Welcomes the users
    welcome_message()
    # Load the JSON data
    json_loaded = load_json_data('Market_Scores.json')

    iterations = user_input()
    results = []

    for my_dict in json_loaded['countries']:
        raw_results = []
        # This part of the function extracts the mean and stdev for size, growth rate, and political/economic risk and
        # places them into the list 'raw_results' so they can be stored and used for later in the function
        size_avg = float(my_dict.get('Size').get('Average'))
        size_std = float(my_dict.get('Size').get('StDev'))
        growth_avg = float(my_dict.get('Potential_Growth_Rate').get('Average'))
        growth_std = float(my_dict.get('Potential_Growth_Rate').get('StDev'))
        political_avg = float(my_dict.get('Political_Economic_Risk').get('Average'))
        political_std = float(my_dict.get('Political_Economic_Risk').get('StDev'))

        # This part extracts the remaining information, the min and max, for talent risk and competition risk
        talent_min = int(my_dict.get('Talent_Risk').get('Min'))
        talent_max = int(my_dict.get('Talent_Risk').get('Max'))
        competition_min = int(my_dict.get('Competition_Risk').get('Min'))
        competition_max = int(my_dict.get('Competition_Risk').get('Max'))


        # Now we ise the 'num' from the 'user_input' function and run simulation that specified number of times
        for i in range(iterations):
            # This step generates random values for each variable using the given formulas in the project instructions
            size = random.normalvariate(math.log(size_avg), math.log(size_std))
            growth_rate = random.normalvariate(math.log(growth_avg), math.log(growth_std))
            political_economic_risk = random.normalvariate(math.log(political_avg), math.log(political_std))
            talent_risk = math.log(random.randint(talent_min, talent_max))
            competition_risk = math.log(random.randint(competition_min, competition_max))

            # This part then assigns a market score using the provided formula from the project instructions
            market_score = (10 + 0.22 * size + 0.64 * growth_rate
                            - 0.65 * competition_risk
                            - 1.03 * political_economic_risk
                            - 1.37 * talent_risk)

            # We then append the market_score to the raw_results list
            raw_results.append(market_score)

        # Calculate statistics for the raw results
        avg, stdev, median, minimum, maximum, result_range = calculate_statistics(raw_results)

        # Store the result for this country
        results.append({
            'country': my_dict.get('name'),
            'average': avg,
            'stdev': stdev,
            'median': median,
            'min': minimum,
            'max': maximum,
            'range': result_range,
            'raw_results': raw_results
        })

    # This loop is what enables the user to continuously enter in different metrics that they want to test!
    top_bottom_count = get_top_bottom_count()

    while True:
        metric_map = metric()
        metric_choice = input('Please enter the metric you want to report on (or "done" to finish): ').strip().lower()

        if metric_choice == 'done':
            write_results(results, 'Market_Simulation_Results.txt')
            print(
                "Simulation complete! Results written to 'Market_Simulation_Results.txt'. Thank you for trying out our Market Simulation!")
            break

        if metric_choice not in metric_map:
            print('Invalid metric. Please choose from the provided options.')
            continue

        # Access the correct key for the chosen metric
        chosen_metric = metric_map[metric_choice]

        # Sort the countries based on the chosen metric
        sorted_results = sorted(results, key=lambda x: x[chosen_metric], reverse=True)

        # Display the top and bottom countries based on the chosen metric
        print(f"\nThe top {top_bottom_count} countries based on {metric_choice} are:")
        for i, result in enumerate(sorted_results[:top_bottom_count]):
            print(f"{i + 1}. {result['country']} with a {metric_choice} of {result[chosen_metric]:.2f}")

        print(f"\nThe bottom {top_bottom_count} countries based on {metric_choice} are:")
        for i, result in enumerate(sorted_results[-top_bottom_count:], start=1):
            print(
                f"{len(sorted_results) - top_bottom_count + i}. {result['country']} with a {metric_choice} of {result[chosen_metric]:.2f}")

run_simulation()