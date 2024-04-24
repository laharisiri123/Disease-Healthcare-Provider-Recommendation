import React from "react";

import "./DoctorList.css";

const DoctorList = ({ doctors }) => {
  return (
    <div>
      <h2 className="doctor-result-title">
        Top doctors based on Experience and User Ratings
      </h2>
      <ol className="doctor-list">
        {doctors.map((doctor, index) => (
          <li key={index} className="doctor-item">
            <p className="doctor-details">
              <span className="doctor-detail-name">Name:</span> {doctor.name}
            </p>
            <p className="doctor-details">
              <span className="doctor-detail-name">Hospital:</span>
              {doctor.hospital}
            </p>
            <p className="doctor-details">
              <span className="doctor-detail-name"> City:</span> {doctor.city}
            </p>
            <p className="doctor-details">
              <span className="doctor-detail-name">Experience:</span>
              {doctor.experience} years
            </p>
            <p className="doctor-details">
              <span className="doctor-detail-name">Rating:</span>
              {doctor.rating}
            </p>
          </li>
        ))}
      </ol>
    </div>
  );
};

export default DoctorList;
