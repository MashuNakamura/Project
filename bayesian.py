# Import Dataset dari data_fetcher
from data_fetcher import DataFetcher

# Class utama MBTI
class BayesianMBTIApp:
    def __init__(self):
        # Probabilitas 16 tipe
        self.mbti_types = [
            "ISTJ", "ISFJ", "INFJ", "INTJ",
            "ISTP", "ISFP", "INFP", "INTP",
            "ESTP", "ESFP", "ENFP", "ENTP",
            "ESTJ", "ESFJ", "ENFJ", "ENTJ"
        ]

        # Inisialisasi setiap pertanyaan menjadi probabilitas 1/16
        self.type_probabilities = {mbti_type: 1/16 for mbti_type in self.mbti_types}

        # Load Data Question
        data = DataFetcher("./data.csv")
        self.questions = data.data

    # Fungsi untuk mengupdate probabilitas
    def update_probabilities(self, answer_likelihoods):
        for mbti_type in self.mbti_types:
            # Mengambil nilai yang ada
            probability = self.type_probabilities[mbti_type]

            # Mengambil per type (16 type)
            for i, letter in enumerate(mbti_type):
                if letter in answer_likelihoods:
                    probability *= answer_likelihoods[letter]

            # Mengudpate nilai yang ada
            self.type_probabilities[mbti_type] = probability

        # Semua totalnya di jumlah
        total = sum(self.type_probabilities.values())
        if total > 0:
            # Looping satu per satu, dan score per type di bagi lagi dengan total untuk normalisasi
            for mbti_type in self.type_probabilities:
                self.type_probabilities[mbti_type] /= total

    # Mengambil nilai yang paling besar
    def get_most_probable_type(self):
        return max(self.type_probabilities, key=self.type_probabilities.get)

    # Print tampilan pertanyaan
    def run(self):
        print("Welcome to the Bayesian MBTI Test!")
        print("Answer each question from 1 (Strongly Disagree) to 5 (Strongly Agree).")

        for idx, (question, answer_likelihoods) in enumerate(self.questions):
            print(f"\nQuestion {idx+1}: {question}")
            while True:
                answer = int(input("Your answer (1-5): "))
                if answer in [1, 2, 3, 4, 5]:
                    break
                else:
                    print("Please enter a number between 1 and 5.")

            # Kalau ditemukan jawaban, maka update si probabilities
            if answer in answer_likelihoods:
                self.update_probabilities(answer_likelihoods[answer])
            else:
                print("Warning: No likelihood data for this answer. Skipping update.")

        # Mengambil probabilitas terbesar
        final_type = self.get_most_probable_type()
        print(f"\nYour MBTI type is most likely: {final_type}")

if __name__ == "__main__":
    app = BayesianMBTIApp()
    app.run()