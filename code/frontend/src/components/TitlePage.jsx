import "./TitlePage.css";

const TitlePage = () => {
  return (
    <div className="title-page">
      <h1 className="title-name">MedAssist: AI-Powered Medical Guidance</h1>
      <h3 className="title-subtitle">
        Empowering Accurate Disease Prediction and Personalized Healthcare
        Provider Recommendations
      </h3>
      <p className="wesite-description">
        MedAssist uses AI to predict diseases from your symptoms and recommend
        specialized doctors based on the predicted disease, doctor expertise,
        user raings and your preferences.
      </p>
      <a href="#disease-pred" className="start-link">
        Let's start
      </a>
    </div>
  );
};

export default TitlePage;
