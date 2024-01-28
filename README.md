# Q&A Chatbot

This is a Q&A chatbot built with Streamlit and OpenAI's GPT-3.5-turbo model.


## Code Explanation

The `app.py` script is the main entry point of the application. It uses the Streamlit library to create a web-based user interface for the chatbot.

The function `getLLamaresponse(input_text, no_words, blog_style)` is used to generate a response from the LLAMA model. It takes three parameters:

- `input_text`: The topic of the blog.
- `no_words`: The desired length of the blog in words.
- `blog_style`: The style of the blog.

The function initializes a `CTransformers` object with the LLAMA model and a specific configuration. It then defines a template for the prompt that will be sent to the model. The `PromtTemplate` object is used to format this prompt with the provided input variables.


## Setup

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/yourrepository.git
    ```

2. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

3. Set up your OpenAI API key in a `.env` file:
    ```
    OPENAI_API_KEY=yourapikey
    ```

## Usage

1. Run the Streamlit app:
    ```
    streamlit run app.py
    ```

2. Enter your question in the text input field.

3. Click the "Ask the question" button to get the response from the chatbot.

## License

This project is licensed under the terms of the MIT license.
