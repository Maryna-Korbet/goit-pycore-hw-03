import re

def normalize_phone(phone_number: str) -> str:
    phone_number = re.sub(r"[^\d+]", "", phone_number.strip())
    
    if not phone_number.startswith('+'):
        if phone_number.startswith('380'):  
            phone_number = f"+{phone_number}"
        else:
            phone_number = f"+38{phone_number}"
    
    return phone_number
    
if __name__ == "__main__":
    test_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "+380501112233"
    ]
    
    for number in test_numbers:
        print(f"Start number: {number} -> Normalized number: {normalize_phone(number)}")

