
# Cybersecurity RAG (Retrieval-Augmented Generation) System

## Project Overview

This project is a **graph-based Retrieval-Augmented Generation (RAG) system** designed for cybersecurity and penetration testing use cases. 
Using LangGraph and LangChain, it processes, structures, and retrieves cybersecurity data from various sources, including unstructured text and images.
The goal is to ingest raw data, build a dynamic graph, and provide contextually relevant answers to user queries, powered by a language model (LLM).

## Key Functionalities

1. **Data Ingestion**: Parses raw text and images, pre-processes them, and prepares them for integration into the graph.
2. **Graph Construction**: Dynamically constructs a graph with nodes (representing entities) and edges (representing relationships).
3. **Inference Pipeline**: Answers user queries by retrieving relevant graph data, generating context, and utilizing an LLM.
4. **Modularity**: Code is structured in a modular way, allowing flexibility and easy scalability.

---

## Project Structure

### Directory Layout

```plaintext
cybersecurity_rag_project/
│
├── config/
│   ├── config.py                   # Configuration settings for environment variables and API keys
│
├── data/
│   ├── raw_data/                   # Directory to store raw input files (e.g., text and image files)
│   ├── processed_data/             # Directory for preprocessed data
│
├── src/
│   ├── ingestion/                  # Module to handle data ingestion and preprocessing
│   ├── graph/                      # Module to manage graph construction and storage
│   ├── inference/                  # Module to handle user queries and responses
│   ├── utils/                      # Utility functions for logging, error handling, and benchmarking
│   ├── app.py                      # Main application entry point
│
├── tests/                          # Unit tests for validating each module
├── docker/                         # Docker configuration files
├── .env                            # Environment variables file (excluded from version control)
├── README.md                       # Project overview and setup instructions
└── requirements.txt                # List of required packages
```

---

## Detailed Explanation of Each Module

### config/config.py

- **Purpose**: Manages environment variables and configuration settings.
- **Environment Variables**:
  - `DATABASE_URI`: URI for MongoDB.
  - `VECTOR_DB_URI`: URI for vector database (optional).
  - `LLM_API_KEY` and `LLM_MODEL`: API key and model name for the LLM.

### data/

- **raw_data/**: Stores raw input files like scan text and screenshots.
- **processed_data/**: Holds data pre-processed for graph integration.

### src/

#### ingestion/

- **data_ingestion.py**: Main orchestrator for data ingestion. Calls text and image processors to structure the raw data.
- **text_parser.py**: Uses the LLM API to extract entities and relationships from raw text data.
- **image_processor.py**: Processes images (e.g., screenshots) that accompany text data.
- **entity_detection.py**: Identifies entities like hosts and services.
- **graph_update.py**: Ensures updates to the graph without duplicating nodes.

#### graph/

- **graph_builder.py**: Builds the graph using `networkx`, adding nodes and edges dynamically.
- **graph_utils.py**: Utility functions for managing graph nodes and edges.
- **database_handler.py**: Handles storage/retrieval of the graph in MongoDB.
- **entity_relations.py**: Defines and manages dynamic entities and relationships.

#### inference/

- **inference_pipeline.py**: Manages the entire inference process, integrating context retrieval and LLM response generation.
- **query_processor.py**: Parses and processes user queries.
- **context_retriever.py**: Retrieves relevant context from the graph for query response.
- **response_generator.py**: Calls the LLM to generate a natural language answer.

#### utils/

- **logging_setup.py**: Configures consistent logging across the application.
- **exception_handler.py**: Defines custom exceptions and error handling.
- **benchmarks.py**: Measures performance of key functions.

### src/app.py

- **Main Entry Point**: Sets up and orchestrates data ingestion, graph building, and inference processes.
- **Workflow**:
  - Ingests sample data.
  - Constructs/updates the graph.
  - Answers sample queries.

### tests/

- Contains unit tests to validate each module, including data ingestion, graph building, and inference.

### docker/

- **Dockerfile**: Builds a Docker image for containerized deployment.
- **docker-compose.yml**: Optional file to orchestrate multiple services (e.g., MongoDB and the app).

---

## Getting Started

### Prerequisites

1. **Python 3.11**
2. **Poetry**: Install via [Poetry's documentation](https://python-poetry.org/docs/#installation).
3. **Docker**: Install via [Docker's documentation](https://docs.docker.com/get-docker/).

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd cybersecurity_rag_project
   ```

2. **Create a Virtual Environment (Optional)**:
   ```bash
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   poetry install  # Or pip install -r requirements.txt if not using Poetry
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root with the following:
     ```plaintext
     DATABASE_URI=mongodb://localhost:27017
     VECTOR_DB_URI=localhost:5000
     LLM_API_KEY=your_openai_api_key
     LLM_MODEL=gpt-4
     ```

5. **Run the Application**:
   ```bash
   poetry run python src/app.py  # Or python src/app.py if using venv and pip
   ```

6. **Run Tests**:
   ```bash
   poetry run pytest tests/
   ```

---

## Docker Setup (Optional)

1. **Build the Docker Image**:
   ```bash
   docker build -t cybersecurity_rag .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run --env-file .env -p 8000:8000 cybersecurity_rag
   ```

---

## Usage

- **Adding Sample Data**: Place raw data in `data/raw_data/` and run the ingestion process.
- **Running Queries**: Modify queries in `app.py` and observe responses.

## Future Enhancements

- **Add new entity types** to improve graph granularity.
- **Optimize prompts** in the LLM API calls.
- **Expand image processing capabilities**.

---

## License

This project is licensed under the MIT License.

