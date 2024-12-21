def main():
    while True:
        print("""
        1. Додати фільм
        2. Додати актора
        3. Показати всі фільми з акторами
        4. Показати унікальні жанри
        5. Показати кількість фільмів за жанром
        6. Показати середній рік народження акторів у фільмах певного жанру
        7. Пошук фільму за назвою
        8. Показати фільми (з пагінацією)
        9. Показати імена всіх акторів та назви всіх фільмів
        10. Показати фільми з їх віком
        0. Вихід
        """)
        choice = input("Виберіть дію: ")

        if choice == "1":
            add_movie()
        elif choice == "2":
            add_actor()
        elif choice == "3":
            show_movies_with_actors()
        elif choice == "4":
            show_unique_genres()
        elif choice == "5":
            show_movies_by_genre()
        elif choice == "6":
            show_average_birth_year_by_genre()
        elif choice == "7":
            search_movies()
        elif choice == "8":
            paginate_movies()
        elif choice == "9":
            union_movies_actors()
        elif choice == "10":
            show_movies_with_age()
        elif choice == "0":
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()




