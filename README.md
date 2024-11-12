# Cybersecurity RAG System

## Overview
This project is a graph-based Retrieval-Augmented Generation (RAG) system tailored for cybersecurity and penetration testing use cases. The system uses LangGraph and LangChain for efficient retrieval and inference on cybersecurity data.

## Features
- **Data Ingestion**: Ingests raw text and images from security scan outputs, preprocesses, and structures the data into a graph.
- **Graph Construction**: Builds and updates a graph database with entities (e.g., hosts, ports) and relationships (e.g., vulnerabilities).
- **Inference Pipeline**: Processes user queries, retrieves relevant context from the graph, and generates responses with LLMs.

## Directory Structure
- `config/`: Contains configuration files for environment variables, database URIs, and API keys.
- `data/`: Directory for raw and processed data files.
- `src/`: Core modules, organized by functionality (e.g., ingestion, graph, inference).
- `tests/`: Unit tests for validating each module.
- `docker/`: Docker setup files for containerization.

## Setup

1. **Environment Setup**  
   Ensure you have Python 3.11 and Poetry installed. Clone the repository and install dependencies:

   ```bash
   poetry install
#   P i n e W h e e l . A I  
 