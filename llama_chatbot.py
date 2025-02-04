 import streamlit as st
 import ollama

 # Function to generate a response from the Llama 3.2 model
 def generate(prompt):
     response = ollama.chat(model='llama3.2', messages=[
                             {
                                 'role': 'user',   # Setting the role of the message
                                 'content': prompt, # User's input prompt
                             }
     ])
     return response['message']['content']  # Extracting the generated response content

 # Streamlit app title
 st.title("Chat bot")
 st.write("Ask your question, and I'll have your answer ready in no time.")

 # Text area for user input
 user_prompt = st.text_area("Enter your question:")

 # When the "Generate Response" button is clicked
 if st.button("Click to get the answer"):
     if user_prompt.strip() != "":  # Check if the prompt is not empty
         with st.spinner("Response in progress..."):  # Show a spinner while generating the response
             try:
                 response = generate(user_prompt)  # Generate the response
                 st.success("Response completed!")  # Show success message
                 st.text_area("Final Response:", value=response, height=200)  # Display the response in a text area
             except Exception as e:
                 st.error(f"Error: {str(e)}")  # Show error message if there's an exception
     else:
         st.warning("Enter a question.")  # Show a warning if the prompt is empty
