// ResultContainer.js
import React from "react";
import DiseaseResult from "./DiseaseResult";

import "./ResultContainer.css";

const ResultContainer = ({ results }) => {
  return (
    <div className="result-container" id="predicted-results">
      <h2 className="result-title">
        Predicted Diseases and Recommended Doctors
      </h2>
      {Array.isArray(results) && results.length > 0 ? (
        results.map((result, index) => (
          <DiseaseResult key={index} result={result} index={index} />
        ))
      ) : (
        <p className="no-results">No results found.</p>
      )}
    </div>
  );
};

export default ResultContainer;
