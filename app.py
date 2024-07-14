import os
import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Answer
from openai import OpenAI, OpenAIError
import openai

# Load environment variables
load_dotenv()

# Get database URL from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debugging

# Bind metadata and create tables if not exists
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# OpenAI API key
open_ai_key = os.getenv('OPEN_AI_KEY')
client = openai.OpenAI(api_key=open_ai_key)

app = Flask(__name__)

def insert_answer(answer_text, question, user_id=None):
    new_answer = Answer(answer=answer_text, user_id=user_id, created_at=datetime.datetime.now(), question=question)
    session.add(new_answer)
    session.commit()
    print("Inserted answer", answer_text, "successfully")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    if not question:
        return jsonify({'error': 'No question provided'}), 400

    messages = [{"role": "user", "content": question}]

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        answer = completion.choices[0].message['content']
        print(answer)
        insert_answer(answer, question)
        return jsonify({'answer': answer}), 200

    except OpenAIError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
