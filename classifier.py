from pathlib import Path


def classify_message(message):
    text = message.lower()

    complaint_words = [
        "очеред", "холодн", "пропал", "не работает",
        "сломал", "проблем", "жалоб"
    ]

    reference_words = [
        "как получить", "где", "справк", "парковк"
    ]

    if any(word in text for word in complaint_words):
        return "жалоба"

    if any(word in text for word in reference_words):
        return "справка"

    return "другое"


def create_draft(message, category):
    if category == "жалоба":
        return (
            "Спасибо за обращение. Мы зарегистрировали проблему "
            "и передадим информацию ответственному подразделению."
        )

    if category == "справка":
        return (
            "Спасибо за обращение. Мы уточним необходимую информацию "
            "и сообщим вам порядок дальнейших действий."
        )

    return (
        "Спасибо за обращение. Уточните, пожалуйста, удобное время "
        "и контактные данные для обратной связи."
    )


file_path = Path(__file__).with_name("messages.txt")
messages = file_path.read_text(encoding="utf-8").splitlines()

for number, message in enumerate(messages, start=1):
    if not message.strip():
        continue

    category = classify_message(message)
    draft = create_draft(message, category)

    print(f"{number}. Обращение: {message}")
    print(f"   Категория: {category}")
    print(f"   Черновик ответа: {draft}")
    print()
