import numpy as np
import pickle
import streamlit as st

# Load your model
loaded_model = pickle.load(open('trained_model.sav','rb'))

def ride_price(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return f"Predicted Ride Fare: ₹{prediction[0]:.2f}"

def main():
    st.title("🚖 Dynamic Fare Prediction for Ride-Hailing Web App")

    Distance = st.text_input("Enter the Total Distance (km):")
    Demand = st.text_input("Enter the Demand (e.g., 1 for low, 10 for high):")
    Time_of_Day = st.text_input("Enter the Time of Day: \nAfternoon - 0 \nEvening - 1 \nMorning - 2 \nNight - 3")
    Weather = st.text_input("Enter the Weather Condition: \nClear - 0 \nRainy - 1 \nSnowy - 2")

    Predicted_Ride_Price = ""
    if st.button("Predict Price"):
        try:
            Predicted_Ride_Price = ride_price([Distance, Demand, Time_of_Day, Weather])
        except:
            Predicted_Ride_Price = "⚠️ Please enter valid numeric values."
    
    st.success(Predicted_Ride_Price)

if __name__ == '__main__':
    main()