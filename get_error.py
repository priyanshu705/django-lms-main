import requests

def get_full_error():
    url = "https://django-lms-main-auu8dwilc-gy068644-8794s-projects.vercel.app/django-diag/"
    try:
        response = requests.get(url, timeout=30)
        print(f"Status: {response.status_code}")
        print("Full Response:")
        print("=" * 50)
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_full_error()