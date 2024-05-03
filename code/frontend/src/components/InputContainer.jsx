// InputContainer.js
import React from "react";
import Select from "react-select";
import "./InputContainer.css";

const timingOptions = [
  { value: "Monday", label: "Monday" },
  { value: "Tuesday", label: "Tuesday" },
  { value: "Wednesday", label: "Wednesday" },
  { value: "Thursday", label: "Thursday" },
  { value: "Friday", label: "Friday" },
  { value: "Saturday", label: "Saturday" },
  { value: "Sunday", label: "Sunday" },
];

const InputContainer = ({
  symptoms,
  setSymptoms,
  city,
  setCity,
  timings,
  setTimings,
  symptomOptions,
  cityOptions,
  handleSubmit,
}) => {
  const sortedSymptomOptions = [...symptomOptions].sort((a, b) =>
    a.label.localeCompare(b.label)
  );
  const sortedCityOptions = [...cityOptions].sort((a, b) =>
    a.label.localeCompare(b.label)
  );

  return (
    <div className="input__container" id="disease-pred">
      <div className="inputs">
        <h1 className="title_heading">Disease Prediction</h1>
        <div>
          <label className="input__label">
            Symptoms:{" "}
            <span className="symptom-suggestion">
              (Please provide atleast 3 syptoms for better Prediction)
            </span>
          </label>
          <Select
            className="input__field"
            isMulti
            options={sortedSymptomOptions}
            onChange={(selectedOptions) => setSymptoms(selectedOptions)}
          />
        </div>
        <div>
          <label className="input__label">City:</label>
          <Select
            className="input__field"
            isMulti
            options={sortedCityOptions}
            onChange={(selectedOptions) => setCity(selectedOptions)}
          />
        </div>
        <div>
          <label className="input__label">Timings:</label>
          <Select
            className="input__field"
            isMulti
            options={timingOptions}
            onChange={(selectedOptions) => setTimings(selectedOptions)}
          />
        </div>
        <a
          href="#predicted-results"
          onClick={handleSubmit}
          className="submit__btn"
        >
          SUBMIT
        </a>
      </div>
    </div>
  );
};

export default InputContainer;
