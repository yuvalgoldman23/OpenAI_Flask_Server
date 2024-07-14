This project implements a simple Flask server that has a single endpoint "/ask", used to contact OpenAI's API. The API's answers to the sent questions is then stored in a postgresql DB, in the format of "question" and "answer" for every entry, with its own generated ID. Both the server and the DB are dockerized - instructions of usage right here.

Usage

Replace the placeholder in the docker-compose.yml file with your own OpenAI key before composing.

Run "docker-compose up --build" from the directory in which this project is saved; Now, if everything went smoothly, you should be able to get answers to your question by using the /ask endpoint in localhost:5000.

The required format for asking a question is by sending an application/json POST request with a body of such format:

{"question":"question text here"}

Also added to this Github repository is a simple test file called "test.py". It validates the format of the response to a sample question, and makes sure that the status is "200", a successful response from OpenAI.

Run it by typing "python test.py" and see its results in the terminal.