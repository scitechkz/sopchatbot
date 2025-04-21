from .settings import *

# Disable database during build
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

# Disable OpenAI initialization during build
openai_client = None