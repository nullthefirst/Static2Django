def parser_core(db_url: str, delimiter: str):
    """ Extract essential element values from a PostgreSQL database URL.
    Args:
        db_url (str): PostgreSQL database URL.
        delimiter (str): element at which to end value character extraction.
    Returns:
        A new trimmed PostgreSQL database URL and the extracted element.    
    """

    element_ = ""  # initialize element base variable to empty string
    for char in db_url:  # iterate through trimmed database url
        element_ += char  # add characters to element base variable
        if char == delimiter:
            break  # break at selected character
    element = element_[:-1]  # trim element base variable

    element_gap = len(element_)
    db_url = db_url[element_gap:]  # trim database url, remove element

    return db_url, element  # return database url, and element


def database_url_postgres_parser(database_url: str):
    """ Collect all necessary information from PostgreSQL database URL.
    Args:
        database_url (str): PostgreSQL database URL.
    Returns:
        Dictionary object holding the value of essential elements mapped to their relevant descriptive keys.
    """

    db_url = database_url[11:]  # remove "postgres://" from database url

    # extract trimmed database url and user value
    db_url, user = parser_core(db_url, ':')

    # extract trimmed database url and password value
    db_url, password = parser_core(db_url, '@')

    # extract trimmed database url and host value
    db_url, host = parser_core(db_url, ':')

    # extract trimmed name value and port value
    db_name, port = parser_core(db_url, '/')

    # return mapped dictionary with values and keys for relevant elements
    return dict(user=user, password=password, host=host, port=port, name=db_name)


# postgres://USER:PASSWORD@HOST:PORT/NAME
