from tokenizer import TextTokenizer

def main():

    # Пример использования
    tokenizer = TextTokenizer()
    sample_text = "Здравствуйте! 123 Это. текст. для! токенизации! тест;;;"
    print('*'*20)
    print(f"Текст: {sample_text}\n")
    results = tokenizer.tokenize_all(sample_text)
    print('*'*20)
    print('Токенизация в процессе')
    print('*'*20)
    for method, tokens in results.items():
        print(f"Метод: {method}\nТокены: {tokens}\n")
    print('='*40)

if __name__ == "__main__":
    main()