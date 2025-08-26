# address-duplicate-search

This project provides a REST service for normalizing addresses. It exposes an endpoint that utilizes the address normalization capabilities defined in the `utils/normalizer.py` module.

## Project Structure

```
address-duplicate-search
├── src
│   ├── api
│   │   ├── __init__.py
│   │   ├── app.py
│   │   └── routes.py
│   └── utils
│       ├── __init__.py
│       └── normalizer.py
├── tests
│   └── test_api.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd address-duplicate-search
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python src/api/app.py
   ```

## API Endpoints

- **POST /normalize**
  - Request Body: 
    ```json
    {
      "address": "string"
    }
    ```
  - Response: 
    ```json
    {
      "normalized_address": "string"
    }
    ```

## Testing

To run the tests, use the following command:
```bash
pytest tests/test_api.py
```

## License

This project is licensed under the MIT License.