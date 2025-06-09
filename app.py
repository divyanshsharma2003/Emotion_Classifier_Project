import streamlit as st
import joblib

# Load model
model = joblib.load("svm_emotion_model.pkl")

emoji_dict = {
    "anger": "😠",
    "fear": "😨",
    "joy": "😄",
    "love": "❤️",
    "sadness": "😢",
    "surprise": "😲",
}

# Title and description
def main():
    st.title("Emotion Classifier")
    st.write("Enter text and get the underlying emotion (e.g., Happy, Sad, Angry, etc.)")

    # Text input
    text_input = st.text_area("Enter text here:")

    # Predict button
    if st.button("Predict"):
        if text_input.strip() != "":
            prediction = model.predict([text_input])[0]
            emoji = emoji_dict.get(prediction, "")
            st.success(f"Predicted Emotion: **{prediction.capitalize()}** {emoji}")
        else:
            st.warning("Please enter some text.")

    # Show accuracy and evaluation
    st.markdown("---")
    st.markdown("### Model Evaluation")
    st.write("✅ Accuracy: **88%**")

if __name__ == '__main__':
    main()