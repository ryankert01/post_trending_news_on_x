# Post Trending News on X

This project automates the process of posting trending news on X (formerly known as Twitter). It fetches trending news from a source, processes it, and posts it to your X account.

## Features

- Fetch trending news from a specified source.
- Process and format news for posting.
- Automatically post news to X.

## GitHub Actions Setup

This project includes a GitHub Actions workflow that automatically runs the news posting script once daily at 9:00 AM UTC.

### Setting up Secrets

In your GitHub repository, go to Settings > Secrets and variables > Actions, and add the following secrets:

- `GOOGLE_API_KEY`: Your Google Gemini API key
- `CONSUMER_KEY`: Your Twitter consumer key
- `CONSUMER_SECRET`: Your Twitter consumer secret
- `ACCESS_TOKEN`: Your Twitter access token
- `ACCESS_TOKEN_SECRET`: Your Twitter access token secret

### Manual Execution

You can also trigger the workflow manually from the Actions tab in your GitHub repository.

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/uv-mgr/uv) as the Python environment manager
- An X API key and secret for authentication

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/post_trending_news_on_x.git
cd post_trending_news_on_x
```

### 2. Install `uv`

Follow the instructions on the [uv GitHub page](https://github.com/uv-mgr/uv) to install `uv`.

### 3. Create and Activate the Environment

```bash
uv create
uv activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root and add the following:

```
GOOGLE_API_KEY=your_gemini_api_key
CONSUMER_KEY=your_twitter_consumer_key
CONSUMER_SECRET=your_twitter_consumer_secret
ACCESS_TOKEN=your_twitter_access_token
ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

### 6. Run the Application

```bash
python main.py
```

## Usage

- The application will fetch trending news and post it to your X account.
- Logs will be generated in the `logs/` directory for debugging purposes.

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
