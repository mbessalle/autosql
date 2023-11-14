def main():
    # parse prompt param using argparse

    # connect to db with statement and create a db_manager

    # call db_manager.get_table_definition_for_prompt() to get tables in prompt ready form

    # create two blank calls to llm.add _cap_ref() that update our current prompt passed in from the cli

    # call llm.prompt to get a prompt_response variable

    # parse sql response from prompt_response using SQL_QUERY_DELIMITER "---------"

    # call db_manager.runsql() with the parsed sql

    pass

if __name__ == '__main__':
    main()