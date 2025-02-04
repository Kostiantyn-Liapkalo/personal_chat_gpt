## 1. Create a token in ChatGPT settings
## 2. Copy the token to: mychatgpt/settings.py (OPENAI_API_KEY = 'your-openai-api-key')

1. Sign up or log in to OpenAI
Go to the OpenAI website.

- If you don't have an account yet, sign up by clicking Sign Up.

- If you already have an account, log in by clicking Log In.

2. Go to the API Keys section
- After logging in, go to the API Keys panel.

- Click the Create new secret key button.

3. Create a new API key
Enter a name for the key (for example, "My ChatGPT App").

- Click Create secret key.

Copy the generated key and save it in a safe place. Note: The key will no longer be displayed after you close the window, so be sure to save it.

# Start comads:
```
poetry run python manage.py createsuperuser
```
```
poetry run python manage.py runserver
```
# Go to the login page:
```
http://127.0.0.1:8000/accounts/login/
```
