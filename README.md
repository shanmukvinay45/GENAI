# Conversational RAG with PDF & Chat History + YouTube Summarizer

This repository includes two AI-powered tools built with **LangChain** and **Streamlit** that use retrieval-augmented generation (RAG) to enhance document interaction and content summarization.

---

## Project One: Conversational RAG with PDF and Chat History

This tool allows users to upload PDF documents and query their content through a conversational interface, with context-aware responses maintained across multiple interactions.

### Features

- **PDF Document Upload**: Upload one or more PDF files to interact with.
- **Conversational AI**: Ask questions and receive contextually relevant answers from the PDF content.
- **Chat History**: Maintains conversation history for more insightful and coherent responses.
- **Powered by**: RAG using Groq’s Llama model and HuggingFace embeddings.

### How to Use

1. **Upload PDFs**: Start by uploading the PDF documents you want to query.
2. **Ask Questions**: Type your questions to interact with the document's content.
3. **Receive Context-Aware Responses**: Benefit from a conversation history that improves response quality.

---

## Project Two: YouTube & Website Summarizer

This tool provides concise summaries of YouTube videos or website articles by extracting transcripts or text and summarizing them effectively.

### Features

- **YouTube Video Summarization**: Input a YouTube URL to generate a concise summary.
- **Website Content Summarization**: Input a website URL to receive a summary of the article or page content.
- **Streamlined Summaries**: Delivers clear and concise summaries, saving time on lengthy content.

### How to Use

1. **Input URL**: Provide a YouTube or website URL.
2. **Generate Summary**: Receive a brief, accurate summary of the video or web content.

---
   ```bash
   pip install streamlit langchain google-generativeai PyPDF2
