import requests
import json
from datetime import datetime

LINK1 = 'https://user-management-backend-a68g.onrender.com/api/users'
LINK2 = 'https://event-booking-system-pex8.onrender.com/api/events/'

def check_link(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException:
        return 'Error'

def main():
    result = {
        'timestamp': datetime.now().isoformat(),
        'link1_status': check_link(LINK1),
        'link2_status': check_link(LINK2)
    }
    
    print(json.dumps(result, indent=2))
    
    with open('check_result.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()