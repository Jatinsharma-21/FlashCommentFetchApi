# Comment Search API


The Flask API defined in the provided script establishes an endpoint, `/search`, designed to handle HTTP GET requests. It processes various query parameters, including `search_author`, `at_from`, `at_to`, and more, extracting them from the request URL. Constructing a parameter dictionary, the API sends a GET request to an external API specified by `BASE_URL` and parses the resulting comments. The `filter_comments` function systematically iterates through each comment, applying filters based on parameters like author, date range, likes, replies, and search text. Filtered comments meeting all specified criteria are compiled into a `filtered_comments` list. Additional functions handle specific filtering logic for author, date, likes, replies, and text. The script includes a block ensuring that the Flask app runs only when executed directly, launching the development server with debugging enabled. In summary, this API acts as a middleware, facilitating the retrieval and filtration of comments from an external source based on user-defined parameters.



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


 **Example:**
To demonstrate how to use the Comment Search API, consider the following example query parameters:

![all](https://github.com/Jatinsharma-21/FlashCommentFetchApi/assets/96420426/d9a7b95d-fb00-4518-aa64-f68a18baa7a9)
```http
GET http://127.0.0.1:5000/search?like_from=0&search_author=Did%20you%20know%3F&at_from=25-01-2023&at_to=25-01-2023&reply_from=1&search_text=hope



