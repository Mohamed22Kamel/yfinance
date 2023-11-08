from InvestChat.settings import MODEL, CHECK


def bot_answer(message):
    company_name = MODEL.extract(message)
    if len(company_name) == 0:
        return "Sorry, I didn't understand that."
    print(company_name[0])
    prediction = CHECK.can_invest(company_name[0])
    if prediction == "failure":
        return "Sorry, I didn't understand that."
    if (len(prediction)):
        if prediction[0]:
            return f"i predict that {company_name[0]} will go up tomorrow so i recommend you speculate this stock "
        return f"i predict that {company_name[0]} will go down tomorrow so i recommend you check another stock "
    else:
        return 'failure'
