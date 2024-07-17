import pandas as pd


def read_csv(file_path):
    # Assuming the CSV file is named 'data.csv'
    

    # Read the CSV file
    df = pd.read_csv(file_path, delimiter=';', dtype=str, encoding='utf-8')

    # Display the DataFrame
    print(df)
    return df

# Function to get the message corresponding to a given number
def get_message(df, number):
    result = df[df['number'] == number]['message']
    if not result.empty:
        return result.values[0]
    else:
        return None

file_path = '/home/lena/Dokumente/Projects_to_try_2/PythonSnippets/12_Play_with_strings_and_csv/data.csv'
df = read_csv(file_path)

number = 123
message = get_message(df, number)
print(message)