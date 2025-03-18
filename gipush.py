import os
import subprocess

def git_push():
    # Путь к вашему локальному git-репозиторию
    repo_path = os.getcwd()  # Или укажите конкретный путь к репозиторию

    try:
        # Перейти в директорию репозитория
        os.chdir(repo_path)
        
        # Выполнить git add .
        subprocess.run(['git', 'add', '.'], check=True)

        # Выполнить git commit -m "Your commit message"
        commit_message = input("Введите сообщение коммита: ")
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)

        # Выполнить git push
        subprocess.run(['git', 'push'], check=True)

        print("Изменения успешно отправлены в репозиторий!")

    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    git_push()