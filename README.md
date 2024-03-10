# GH Search Backend

This is a Python server designed to serve results for user queries. It is the backend for a lightweight frontend that lets users search the best GitHub projects with free search text.

## Project Structure

The project consists of the following files:

- `.gitignore`: Specifies intentionally untracked files to ignore when using Git.
- `README.md`: This file, contains information about the project and instructions on how to use it.
- `requirements.txt`: Contains the necessary dependencies that need to be installed.
- `app.py`: The main application file.
- `search.py`: Handles the search functionality.
- `tests.py`: Contains the tests for the application.

## Setup

1. Clone the repository
2. Install the dependencies using `pip install -r requirements.txt`
3. Run the application using `python app.py`

## Usage

To use the application, send a GET request to the `/search` endpoint with your query as a parameter.

## Testing

To run the tests, use the command `python -m unittest tests.py`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
