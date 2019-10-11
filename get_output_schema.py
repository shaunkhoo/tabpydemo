def get_output_schema():
    return pd.DataFrame({
        'Name': prep_string(),
        'ID': prep_int(),
        'Student': prep_bool(),
        'Birth_Date': prep_date(),
        'Fastest_Speed': prep_decimal(),
        'Test_DateTime': prep_datetime()
    })