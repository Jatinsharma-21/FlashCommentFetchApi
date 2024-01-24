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

- `at_from`, `at_to`: (Optional) Filter comments by date range. These parameters allow you to specify a range of dates to retrieve comments posted within that period. Dates should be provided in the format YYYY-MM-DD.

  **Example:**
  ```http
  GET /search?at_from=2022-01-01&at_to=2022-12-31

![2](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/1ca7fd05-5907-4689-b03a-01f9c30083d3)


- `like_from`, `like_to`: (Optional) Filter comments by likes range. These parameters allow you to narrow down comments based on the number of likes they have received. You can specify a minimum (`like_from`) and maximum (`like_to`) number of likes for the comments to be included in the search.

  **Example:**
  ```http
  GET /search?like_from=0&like_to=5

![3](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/b19b10f0-5d0a-4669-806e-7244bd802612)

- `reply_from`, `reply_to`: (Optional) Filter comments by replies range. These parameters enable you to narrow down comments based on the number of replies they have received. Specify a minimum (`reply_from`) and maximum (`reply_to`) number of replies for the comments to be included in the search.

  **Example:**
  ```http
  GET /search?reply_from=2&reply_to=5

![Reply](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/4849859f-c978-450a-8c09-c23924f20fdf)


- `search_text`: (Optional) Filter comments by text. This parameter allows you to search for comments containing specific keywords or phrases. Provide the desired text as the value of the parameter to retrieve comments that match the specified criteria.

  **Example:**
  ```http
  GET /search?search_text=important

![text](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/11c5d03d-b512-448e-8741-7ecd7f109ba2)



