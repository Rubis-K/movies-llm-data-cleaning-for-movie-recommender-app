# AI Movie Recommendation System – NLP & Data Processing

## Overview

A Python-based movie recommendation project that explores Natural Language Processing (NLP), text classification, sentiment analysis, and semantic search.

The project focuses on processing movie descriptions, extracting emotional characteristics, and building a recommendation system that understands the meaning of user queries rather than relying solely on keyword matching.

This project also served as the foundation for my cross-platform movie recommendation application developed using C# and .NET MAUI.

## Technologies Used

- **Python** – Data processing and recommendation logic
- **Pandas & NumPy** – Data manipulation and preprocessing
- **Jupyter Notebook** – Data analysis and experimentation
- **NLP & Transformers** – Text classification and emotion analysis
- **LangChain** – Document processing and semantic search
- **OpenAI Embeddings** – Generating vector representations of text
- **ChromaDB** – Vector database for similarity search
- **Gradio** – Interactive recommendation interface
- **FastAPI** – REST API for accessing recommendations

## Project Components

### 1. Movie Data Processing
`data-movies1.ipynb`

Explores and prepares movie data for the recommendation system.

### 2. Sentiment Analysis
`sentiment-analysis.ipynb`

Explores NLP techniques for analyzing emotional characteristics of movie descriptions.

### 3. Text Classification
`text-classification.ipynb`

Experiments with text classification to organize movie descriptions into meaningful categories.

### 4. Semantic Vector Search
`vector-search.ipynb`

Explores vector embeddings and similarity search for retrieving movies based on semantic meaning.

### 5. Recommendation Engine
`semantic_movie_recommendations.py`

Implements movie recommendations using LangChain, OpenAI embeddings, and ChromaDB.

Users can search for movies using natural language and filter recommendations by category and emotional tone.

### 6. REST API
`movie_recommender_api.py`

Provides a FastAPI endpoint for accessing recommendations from external applications.

## How It Works

1. Movie descriptions and metadata are prepared for analysis.
2. NLP techniques are explored to classify text and identify emotional characteristics.
3. Movie descriptions are transformed into vector embeddings.
4. Embeddings are stored in ChromaDB for semantic similarity search.
5. User queries are compared against stored movie descriptions.
6. Recommendations can be filtered by category and emotional tone.
7. Results are returned through a Gradio interface or REST API.

## Features

- Movie dataset processing and preparation
- NLP-based text classification
- Sentiment and emotion analysis
- Semantic similarity search
- Vector database integration
- Natural language movie recommendations
- Category and emotional tone filtering
- REST API integration

## Project Status

This is an early learning project focused on exploring NLP, machine learning techniques, vector databases, and AI-powered recommendation systems.

The repository contains experimental notebooks and implementation code. Some datasets, generated files, dependencies, or environment configuration may be required to reproduce the application.

## What I Learned

- Processing and preparing datasets using Python
- Working with NLP models for text classification and sentiment analysis
- Understanding text embeddings and vector similarity
- Implementing semantic search using LangChain and ChromaDB
- Building recommendation systems based on semantic meaning
- Developing REST APIs with FastAPI
- Integrating AI functionality into larger software applications

## Related Project

This project contributed to the development of my cross-platform movie recommendation application built with C# and .NET MAUI.

**[Semantic Movie Recommender – C# & Python Application](https://github.com/Rubis-K/senmatic-movie-recommdender)**
