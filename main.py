from datetime import datetime

def customerSupportHandler(phone, option):

    timestamp = str(datetime.now())

    if option == "1":
        message = "Your order is currently being processed."

    elif option == "2":
        message = "Returns and refunds team will contact you shortly."

    elif option == "3":
        message = "Technical support team is working on your issue."

    else:
        message = "Invalid option selected."

    data = {
        "PhoneNumber": phone,
        "SelectedOption": option,
        "Timestamp": timestamp
    }

    print(data)

    return message


print(customerSupportHandler("6300413201", "1"))