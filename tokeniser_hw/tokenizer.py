"""
Модуль для токенизации текста различными способами
"""

import re

class TextTokenizer:
    def __init__(self):
        """Инициализация токенизатора: не изменяйте эту строчку кода"""
        # Добавляем проверки доступности библиотек
        self._nltk_available = self._check_nltk()
        self._spacy_available = self._check_spacy()
    
    def _check_nltk(self):
        """Проверка доступности NLTK"""
        try:
            import nltk
            return True
        except ImportError:
            return False
    
    def _check_spacy(self):
        """Проверка доступности spaCy"""
        try:
            import spacy
            return True
        except ImportError:
            return False

    def simple_tokenize(self, text):
        """
        Простая токенизация по пробелам и знакам препинания

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов
        """
        # Реализация простой токенизации 
        if not text or not isinstance(text, str):
            return ["Ошибка: Входной текст должен быть непустой строкой."]
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text) # Раздялем по словам и знакам препинания с помощью регулярных выражений
        tokens = [token for token in tokens if token.strip()] # Удаляем пустые токены
        return tokens
    
    def nltk_tokenize(self, text):
        """
        Токенизация с использованием NLTK

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация NLTK токенизации
        if not self._nltk_available: # Промерим, установлен ли NLTK
            return ["NLTK не установлен. Установите: pip install nltk"] 
        if not text or not isinstance(text, str): # Проверка входных данных на пустые строки
            return ["Ошибка: Входной текст должен быть непустой строкой."]
        try:
            from nltk.tokenize import word_tokenize # Импортируем функцию токенизации из NLTK
            tokens = word_tokenize(text)
            return tokens
        except Exception as e: # Обработка ошибок токенизации
            return [f"Ошибка NLTK токенизации: {str(e)}"] 

    def spacy_tokenize(self, text):
        """
        Токенизация с использованием spaCy

        Args:
            text (str): Входной текст

        Returns:
            list: Список токенов или сообщение об ошибке
        """
        # Реализация spaCy токенизации
        if not self._spacy_available: # Проверка, установлен ли spaCy
            return ["spaCy не установлен. Установите: pip install spacy"]
        if not text or not isinstance(text, str): # Проверка входных данных на пустые строки
            return ["Ошибка: Входной текст должен быть непустой строкой."]
        try:
            import spacy
            nlp = spacy.load("ru_core_news_sm") # Загрузка русской модели spaCy
        except OSError: # Обработка ошибки отсутствия модели
            return ["Модель spaCy не найдена. Установите её командой: python -m spacy download ru_core_news_sm"]
        try:
            doc = nlp(text) # Применим модель к тексту
            tokens = [token.text for token in doc] # Извлечение токенов
            return tokens
        except Exception as e: # Обработка ошибок токенизации
            return [f"Ошибка spaCy токенизации: {str(e)}"]


    def tokenize_all(self, text):
        """
        Применяет все доступные методы токенизации

        Args:
            text (str): Входной текст

        Returns:
            dict: Словарь с результатами всех методов
        """
        # Реализация вызова всех методов
        results = { # Словарь для хранения результатов токенизации
            'simple': self.simple_tokenize(text), # Вызов всех методов токенизации
            'nltk': self.nltk_tokenize(text),
            'spacy': self.spacy_tokenize(text)
        }
        
        return results

def demo():
    """Демонстрационная функция"""
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
    demo()