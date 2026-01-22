#!/usr/bin/env python3
"""
Demo script to test the Rock-Paper-Scissors-Lizard-Spock REST API
"""
import requests
import json
import time
import subprocess
import sys

API_URL = "http://localhost:8000"

def test_api():
    """Test the API endpoints."""
    print("🎮 Testing Rock-Paper-Scissors-Lizard-Spock REST API\n")
    print("=" * 60)
    
    # Test 1: Get API info
    print("\n1️⃣  Testing GET / (API Info)")
    print("-" * 60)
    try:
        response = requests.get(f"{API_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n⚠️  Make sure the API server is running: python api.py")
        sys.exit(1)
    
    # Test 2: Get rules
    print("\n2️⃣  Testing GET /rules")
    print("-" * 60)
    response = requests.get(f"{API_URL}/rules")
    print(f"Status Code: {response.status_code}")
    print(f"Rules: {json.dumps(response.json(), indent=2)}")
    
    # Test 3: Play with JSON payload
    print("\n3️⃣  Testing POST /play with JSON payload")
    print("-" * 60)
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    for choice in choices:
        response = requests.post(
            f"{API_URL}/play",
            json={"choice": choice}
        )
        result = response.json()
        print(f"\n   Your choice: {choice}")
        print(f"   Computer: {result['computer_choice']}")
        print(f"   Result: {result['result']}")
        print(f"   {result['message']}")
    
    # Test 4: Play using specific endpoints
    print("\n4️⃣  Testing POST /rock endpoint")
    print("-" * 60)
    response = requests.post(f"{API_URL}/rock")
    result = response.json()
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(result, indent=2)}")
    
    # Test 5: Health check
    print("\n5️⃣  Testing GET /health")
    print("-" * 60)
    response = requests.get(f"{API_URL}/health")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 6: Invalid choice
    print("\n6️⃣  Testing invalid choice (should return 422)")
    print("-" * 60)
    response = requests.post(
        f"{API_URL}/play",
        json={"choice": "invalid"}
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)[:200]}...")
    
    print("\n" + "=" * 60)
    print("✅ All API tests completed successfully!")
    print("\n📚 Visit http://localhost:8000/docs for interactive API documentation")
    print("=" * 60)

if __name__ == "__main__":
    test_api()
