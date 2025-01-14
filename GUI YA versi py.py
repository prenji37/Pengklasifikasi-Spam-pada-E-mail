import tkinter as tk
from tkinter import scrolledtext, StringVar, OptionMenu, Button, Label, Frame, messagebox
from PIL import Image, ImageTk
import re
import pickle
import csv
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from num2words import num2words
from sklearn.neighbors import KNeighborsClassifier
from gensim.models import Word2Vec  # Import Word2Vec
from gensim.models import KeyedVectors  # Import Word2Vec
import joblib  # Import joblib for loading the pre-trained KNN model

class SpamDetectorApp:
    def __init__(self, master):
        self.window = master
        self.window.state('zoomed')
        self.window.title('DETEKSI SPAM/HAM EMAIL')  

        self.register_frame = Frame(self.window, bg="#ede0da", width=1460, height=779)
        self.bgrn_image = ImageTk.PhotoImage(Image.open('gambar/bgrnn3.png').resize((1460, 779)))
        self.bgrnlabl = Label(self.register_frame, image=self.bgrn_image, background="#ede0da")
        self.bgrnlabl.place(x=0, y=0)
        self.register_frame.place(x=35, y=35)

        self.label = Label(self.window, text="Enter your text email:", bg="#cbb2a6", fg="#181b29", font=("yu gothic ui", 25, "bold"), borderwidth=0, relief="solid")
        self.label.place(x=800, y=270, anchor="center")

        self.entry = scrolledtext.ScrolledText(self.window, font=("yu gothic ui", 20, "bold"), width=40, height=6, wrap='word', bd=5, relief="sunken", insertbackground="#999999", highlightthickness=2, highlightcolor="#cbb2a6")
        self.entry.place(x=658, y=327)  

        self.detect_label = Label(self.window, text="Select Detection Method:", font=("yu gothic ui", 20, 'bold'), bg="#ede0da", fg="black", borderwidth=0)
        self.detect_label.place(x=365, y=300, anchor="center")

        self.detect_methods = ["SVM", "KNN", "Naive Bayes"]
        self.selected_method_var = StringVar()
        self.selected_method_var.set(self.detect_methods[0])  

        self.detect_option_menu = OptionMenu(self.window, self.selected_method_var, *self.detect_methods)
        self.detect_option_menu.config(indicatoron=0, compound='right', font=("yu gothic ui ", 20,'bold'), width=12, bd=1, relief="solid")
        self.detect_option_menu["menu"].config(font=("yu gothic ui ", 20))
        self.detect_option_menu.place(x=365, y=435, anchor="center")

        self.detect_button = Button(master, text="Detect", command=self.detect_selected_method, font=("yu gothic ui", 20, 'bold'), bg="#ede0da", fg="black", borderwidth=0)
        self.detect_button.place(x=365, y=570, anchor="center")
        self.clear_button = Button(master, text="Clear", command=self.clear_entry, font=("yu gothic ui", 20, 'bold'), bg='#ede0da', fg="black", borderwidth=0)
        self.clear_button.place(x=1280, y=722, anchor="center")

        self.load_models()

    def remove_emoji(self, text):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  
                            u"\U0001F300-\U0001F5FF"  
                            u"\U0001F680-\U0001F6FF"  
                            u"\U0001F1E0-\U0001F1FF"  
                            u"\U00002500-\U00002BEF"  
                            u"\U00002702-\U000027B0"
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            u"\U0001f926-\U0001f937"
                            u"\U00010000-\U0010ffff"
                            u"\u2640-\u2642"
                            u"\u2600-\u2B55"
                            u"\u200d"
                            u"\u23cf"
                            u"\u23e9"
                            u"\u231a"
                            u"\ufe0f"  # dingbats
                            u"\u3030"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def nums_to_words(self, text):
        new_text = []
        for word in text.split():
            if word.isdigit():
                word_in_indonesian = num2words(int(word), lang='id', to='year')
                new_text.append(word_in_indonesian)
            else:
                new_text.append(word)
        return " ".join(new_text)

    def remove_punctuation(self, text):
        no_punct = [char for char in text if char not in string.punctuation]
        words_wo_punct = ''.join(no_punct)
        return words_wo_punct

    def preprocess_text(self, text):
        text = re.sub('\S*@\S*\s?', '', text)  # Remove emails
        text = re.sub('\S*(http[s]?://|www\.)\S*', '', text)  # Remove URL links
        text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
        text = re.sub("[^a-zA-Z]", " ", text)  # Remove special characters and numbers
        text = re.sub(r"\b\w{1,2}\b", "", text)  # Remove too short (2- characters) words
        text = re.sub(r"\b\w{17,}\b", "", text)  # Remove too long (17+ characters) words
        text = re.sub(' +', ' ', text).strip()  # Remove multiple spaces
        text = text.lower()  # Convert to lowercase
        text = self.remove_punctuation(text)
        text = self.nums_to_words(text)
        text = self.remove_emoji(text)
        return text

    def load_models(self):
        # Load SVM model and TF-IDF vectorizer from the tuple
        try:
            with open("svm_model.pkl", "rb") as svm_file:
                model_data = pickle.load(svm_file)
                self.svm_model = model_data[0]  # Assuming SVM model is at index 0
                self.tfidf_vectorizer = model_data[1]  # Assuming TF-IDF vectorizer is at index 1
        except Exception as e:
            messagebox.showerror("Error", f"Error loading SVM model and TF-IDF vectorizer: {str(e)}")
            self.svm_model = None
            self.tfidf_vectorizer = None

        # Load Word2Vec model
        try:
            self.knn_model = Word2Vec.load("w2v_model.bin")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading Word2Vec model: {str(e)}")
            self.knn_model = None

        # Load the Naive Bayes model
        try:
            with open("Naive_model.pkl", "rb") as naive_file:
                self.naive_model = pickle.load(naive_file)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading Naive Bayes model: {str(e)}")
            self.naive_model = None

    # Fungsi untuk Deteksi Spam menggunakan SVM:
    def detect_svm(self):
        self.selected_model = "svm"
        preprocessed_text = self.preprocess_text(self.entry.get())
        self.detect_spam(preprocessed_text, self.selected_model)

    # Fungsi untuk Deteksi Spam menggunakan KNN:
    def detect_knn(self):
        self.selected_model = "knn"
        preprocessed_text = self.preprocess_text(self.entry.get())
        self.detect_spam(preprocessed_text, self.selected_model)

    # Fungsi untuk Deteksi Spam menggunakan Naive Bayes:
    def detect_naive_bayes(self):
        self.selected_model = "naive_bayes"
        preprocessed_text = self.preprocess_text(self.entry.get())
        self.detect_spam(preprocessed_text, self.selected_model)

    def detect_svm_logic(self, preprocessed_text):
        print("Preprocessed Text:", preprocessed_text)
        if self.svm_model is None or self.tfidf_vectorizer is None:
            messagebox.showerror("Error", "SVM model or TF-IDF vectorizer not loaded.")
            return

        try:
            text_vectorized = self.tfidf_vectorizer.transform([preprocessed_text])
            decision_function_scores = self.svm_model.decision_function(text_vectorized)
            threshold = 0.0
            predictions = [1 if score > threshold else 0 for score in decision_function_scores]
            prediction = max(set(predictions), key=predictions.count)

            result_message = f"Text Email: {preprocessed_text}\nPrediction: {'Spam' if prediction == 1 else 'Not Spam'}"
            messagebox.showinfo("Spam Detection Result", result_message)

            self.save_to_csv(preprocessed_text, prediction)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def get_word2vec_vector(self, preprocessed_text):
        words = [word for word in preprocessed_text.split() if self.knn_model.wv.has_index_for(word)]
        if not words:
            return None  # Jika tidak ada kata yang ada dalam vektor Word2Vec, kembalikan None
        vectors = [self.knn_model.wv.get_vector(word) for word in words]
        return sum(vectors) / len(vectors)

    def detect_knn_logic(self, preprocessed_text):
        print("Preprocessed Text:", preprocessed_text)
        try:
            text_vector = self.get_word2vec_vector(preprocessed_text)

            if text_vector is None:
                messagebox.showerror("Error", "Word2Vec vector not found for preprocessed text.")
                return 0

            similar_words = [word[0] for word in self.knn_model.wv.most_similar(positive=[text_vector], topn=5)]

            # Memastikan kata yang ada dalam vektor Word2Vec sebelum melakukan evaluasi
            similar_words = [word for word in similar_words if self.knn_model.wv.has_index_for(word)]

            if any(value > 0.5 for word in similar_words for value in self.knn_model.wv[word]):
                return 1  # Spam terdeteksi
            else:
                return 0  # Bukan spam

        except Exception as e:
            # Menampilkan pesan kesalahan jika terjadi kesalahan saat deteksi KNN
            messagebox.showerror("Error", f"An error occurred during KNN detection: {str(e)}")
            return 0

    def detect_selected_method(self):
        preprocessed_text = self.preprocess_text(self.entry.get("1.0", "end-1c"))

        try:
            if self.selected_method_var.get() == "SVM":
                self.detect_svm_logic(preprocessed_text)
            elif self.selected_method_var.get() == "KNN":
                prediction = self.detect_knn_logic(preprocessed_text)  # Fix the parameter passing
                self.handle_prediction_result(preprocessed_text, prediction)
            elif self.selected_method_var.get() == "Naive Bayes":
                self.detect_naive_bayes_logic(preprocessed_text)
            else:
                raise ValueError("Invalid model type")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def handle_prediction_result(self, preprocessed_text, prediction):
        if prediction == 1:
            result_message = f"Text Email: {preprocessed_text}\nPrediction: Spam"
        else:
            result_message = f"Text Email: {preprocessed_text}\nPrediction: Not Spam"

        messagebox.showinfo("Spam Detection Result", result_message)
        self.save_to_csv(preprocessed_text, prediction)


    def detect_naive_bayes_logic(self, preprocessed_text):
        print("Preprocessed Text:", preprocessed_text)
        try:
            prediction = self.naive_model.predict([preprocessed_text])[0]
            result_message = f"Text Email: {preprocessed_text}\nPrediction: {'Spam' if prediction == 1 else 'Not Spam'}"
            messagebox.showinfo("Spam Detection Result", result_message)

            self.save_to_csv(preprocessed_text, prediction)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during Naive Bayes detection: {str(e)}")

    def save_to_csv(self, email_text, prediction):
        try:
            with open("detection_result.csv", mode="a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(["Text Email", "Prediction", "Detection Method"])
                writer.writerow([email_text, "Spam" if prediction == 1 else "Not Spam", self.selected_method_var.get()])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving to CSV: {str(e)}")

    def clear_entry(self):
        self.entry.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SpamDetectorApp(root)
    root.mainloop()