import plotly.express as px
checkin_records = []

adj_descriptions = {
    'CONF': 'confident',
    'EFF': 'efficient'
}
noun_descriptions = {
    'CONF': 'confidence',
    'EFF': 'efficiency'
}

# Define a global variable to store the code used in the first function
global_code = 'CONF'

def learning_checkin(str_code = 'CONF'):
    global global_code  # Access the global variable
    
    # Get the description corresponding to the provided code
    description = adj_descriptions.get(str_code, 'confident')  # 'confident' is the default if the code is not found
    
    # Prompt user for input
    number = input(f"On a scale of 0 (least {description}) to 10 (most {description}), how would you rate your experience in learning the content above: ")
    
    # Validate input
    while True:
        number = float(number)
        if 0 <= number <= 10:
            break
        number = input("Invalid input. Please try again. \nPlease enter an number between 0 and 10: ")
    print(f"The number you entered is: {number}")
    # Add the number to the list
    checkin_records.append(number)
    
    global_code = str_code  # Update the global variable with the code used in the function
    
def plot_checkin():
    global global_code  # Access the global variable
    
    # Get the description corresponding to the provided code
    description2 = noun_descriptions.get(global_code, 'confidence')  # 'confident' is the default if the code is not found
    x_values = list(range(1, len(checkin_records) + 1))  # Generate x-axis values as integers from 1 to the length of checkin_records
    
    fig = px.line(x=x_values, y=checkin_records, range_y=[0, 10])
    fig.update_layout(
        xaxis_title="Your entries for this session",
        yaxis_title=f"Your input on your {description2} level",
        title=f"Trend of your learning {description2} for this session",
        title_x=0.5,
        xaxis=dict(
            tickmode='linear',  # Use linear tick mode to display evenly spaced ticks
            dtick=1,  # Specify the interval between ticks as 1 (since we want to display only integers)
            tick0=1  # Start the tick sequence from 1 (the first x-axis value)
        ))
    fig.show()