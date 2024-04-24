import React, { useState } from "react";
import DoctorList from "./DoctorList";
import "./DiseaseResult.css";

const DiseaseResult = ({ result, index }) => {
  const [showDoctors, setShowDoctors] = useState(false);

  const toggleDoctors = () => {
    setShowDoctors((prevState) => !prevState);
  };

  return (
    <div className="result-item">
      <h3 className="disease-name">{result.Disease}</h3>
      <p className="disease-details">
        <span className="disease-details-name"> Chances:</span> {result.Chances}
        %
      </p>
      <p className="disease-details">
        <span className="disease-details-name"> Description:</span>{" "}
        {result.Description}
      </p>
      <p className="disease-details">
        <span className="disease-details-name"> Specialist:</span>{" "}
        {result.Specialist}
      </p>
      <button onClick={toggleDoctors} className="show-dctr-btn">
        {showDoctors ? "Hide Recommended Doctors" : "Show Recommended Doctors"}
      </button>
      {showDoctors && <DoctorList doctors={result.Doctors} />}
    </div>
  );
};

export default DiseaseResult;
