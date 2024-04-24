import React, { useState, useEffect } from "react";
import axios from "axios";
import InputContainer from "./components/InputContainer";
import ResultContainer from "./components/ResultContainer";
import "./App.css";
const App = () => {
  const [symptoms, setSymptoms] = useState([]);
  const [city, setCity] = useState([]);
  const [timings, setTimings] = useState([]);
  const [results, setResults] = useState([]);
  const [symptomOptions, setSymptomOptions] = useState([]);
  const [cityOptions, setCityOptions] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:5000/data");
        setSymptomOptions(response.data.symptoms);
        setCityOptions(response.data.cities);
      } catch (error) {
        console.error("Error:", error);
      }
    };

    fetchData();
  }, []);

  const handleSubmit = async () => {
    if (symptoms.length < 3) {
      alert("Please select at least 3 symptoms");
      return;
    }

    const selectedSymptoms = symptoms.map((symptom) => symptom.value);
    const selectedCity = city.map((city) => city.value);
    const selectedTimings = timings.map((timing) => timing.value);

    try {
      const response = await axios.post("http://localhost:5000/predict", {
        symptoms: selectedSymptoms,
        city: selectedCity,
        timings: selectedTimings,
      });

      setResults(response.data);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div>
      <InputContainer
        symptoms={symptoms}
        setSymptoms={setSymptoms}
        city={city}
        setCity={setCity}
        setTimings={setTimings}
        symptomOptions={symptomOptions}
        cityOptions={cityOptions}
        handleSubmit={handleSubmit}
      />
      <ResultContainer results={results} />
    </div>
  );
};

export default App;
