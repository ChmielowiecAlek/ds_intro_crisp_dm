from MasculinitySurvey import DataSource, MetaData

# DataSource.download_data()
print(DataSource.get_data_path())

for column_name in MetaData.get_column_names():
    print(MetaData.get_description(column_name))
    print(MetaData.get_allowed_values(column_name))
    print('\n')

df = DataSource.load_data_frame()
print(df.head())
num_rows = df.shape[0]
num_cols = df.shape[1]
print('There are ' + str(num_rows) + ' rows and ' + str(num_cols) + ' columns')

no_nulls = set(df.columns[df.isnull().mean()==0])
print('There are ' + str(len(no_nulls)) + ' columns without missing values:' + str(no_nulls))

with_nulls = set(df.columns[df.isnull().mean()!=0])
print('There are ' + str(len(with_nulls)) + ' columns with missing values:' + str(with_nulls))

most_missing_cols = set(df.columns[df.isnull().mean() > 0.5])
print('There are ' + str(len(most_missing_cols)) + ' columns with most missing values:' + str(most_missing_cols))


# TODO: Some columns are boolean/3-values, maybe they should be corrected.
#       Raw answers should be verified against the dictionary (and vice versa).
#       I see some in double quotes - to be checked.
#       Handle 'Not selected' and 'NA'
#       Apply a consistency check (SHOW IF)
#       Oh, they removed age from the results.
#       And not all are described in the pdf. Some of them look like repetitions...
