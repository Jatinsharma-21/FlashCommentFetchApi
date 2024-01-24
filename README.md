# Comment Search API

This Flask API allows you to search and filter comments from a remote API based on various parameters such as author, date, likes, replies, and text.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Requests library

### Installation

pip install flask

### Run the Flask application
python app.py

## API Endpoints

### Search Comments

**Endpoint:** `/search`  
**Method:** `GET`


#### Query Parameters

- `search_author`: (Optional) Filter comments by the author's name. This parameter allows you to narrow down the search to comments posted by a specific author. Provide the author's name as a query parameter value.

  **Example:**
  ```http
  GET /search?search_author=JohnDoe


![1](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/29e4d49d-b4e5-43c9-a4c8-5e4a1b6e6257)
![2](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/1ca7fd05-5907-4689-b03a-01f9c30083d3)
![3](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/b19b10f0-5d0a-4669-806e-7244bd802612)
![Reply](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/4849859f-c978-450a-8c09-c23924f20fdf)
![text](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/11c5d03d-b512-448e-8741-7ecd7f109ba2)



