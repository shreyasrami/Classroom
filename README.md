# Classroom

A classroom where teacher can assign quizzes on various topics to students.
Students can submit the quiz and view their results.

## Installation Instructions

1. Clone the project.
    ```shell
    $ git clone https://github.com/shreyasrami/Classroom
    ```
2. `cd` intro the project directory
    ```shell
    $ cd Classroom
    ```
3. Create a new virtual environment activate it.
    ```shell
    $ python3 -m venv env
    $ source env/bin/activate
    ```
4. Install dependencies from requirements.txt:
    ```shell
    (env)$ pip install -r requirements.txt
    ```
5. Migrate the database.
    ```shell
    (env)$ python manage.py migrate
    ```

6. Run the local server via:
    ```shell
    (env)$ python manage.py runserver
    ```

### Done!
The local application will be available at <a href="http://localhost:8000" target="_blank">http://localhost:8000</a>.

## Contributing
Pull requests are welcome. For major
changes, please open an issue first 
to discuss what you would like to change.

