# config/settings.py
API_LIMITS = {
    'reddit': {
        'requests_per_minute': 60,
        'requests_per_hour': 3600,
        'batch_size': 100
    },
    'hackernews': {
        'requests_per_minute': 60,
        'requests_per_hour': None,  # No official limit
        'batch_size': 50
    },
    'github': {
        'requests_per_minute': 60,
        'requests_per_hour': 5000,  # Authenticated
        'batch_size': 30
    }
}

# Processing targets
PROCESSING_TARGETS = {
    'posts_per_run': 300,
    'daily_records': 10000,
    'sentiment_accuracy_target': 0.75  # 75% minimum
}