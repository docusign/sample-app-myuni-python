import React from "react";
import { Link } from "react-router-dom";
import image from "../../assets/img/img-01.svg";
import background from "../../assets/img/img-04.jpg";
import { useTranslation } from "react-i18next";
import parse from "html-react-parser";
export const Home = () => {
  const { t } = useTranslation("Home");

  return (
    <>
      <section
        className="hero-section bg-prop"
        style={{
          backgroundImage: `url(${background})`
        }}
      >
        <div className="container">
          <div className="hero-text">
            <h1 className="h1">{t("Header1")}</h1>
            <span className="sub-title">{t("Header2")}</span>
          </div>
        </div>
      </section>
      <section className="card-info-holder">
        <div className="container-fluid">
          <div className="row justify-content-md-center justify-content-lg-start">
            <div className="d-flex col-12 col-md-6 col-lg-4">
              <div className="card-info">
                <div className="card-info-image-holder">
                  <img src={image} alt=""></img>
                </div>
                <h3 className="card-info-title">{parse(t("Card1.Title"))}</h3>
                <span className="card-info-description">
                  {parse(t("Card1.Description"))}
                </span>
                <div className="card-info-button-holder">
                  <Link to="/requestMajorMinorChange">
                    <button className="btn btn-danger">
                      {t("Card1.Button")}
                    </button>
                  </Link>
                </div>
                <div className="card-info-list">
                  {parse(t("Card1.Features"))}
                </div>
              </div>
            </div>
            <div className="d-flex col-12 col-md-6 col-lg-4">
              <div className="card-info">
                <div className="card-info-image-holder">
                  <img src={image} alt=""></img>
                </div>
                <h3 className="card-info-title">{parse(t("Card2.Title"))}</h3>
                <span className="card-info-description">
                  {parse(t("Card2.Description"))}
                </span>
                <div className="card-info-button-holder">
                  <Link to="/requestTranscript">
                    <button className="btn btn-danger">
                      {t("Card2.Button")}
                    </button>
                  </Link>
                </div>
                <div className="card-info-list">
                  {parse(t("Card2.Features"))}
                </div>
              </div>
            </div>
            <div className="d-flex col-12 col-md-6 col-lg-4">
              <div className="card-info">
                <div className="card-info-image-holder">
                  <img src={image} alt=""></img>
                </div>
                <h3 className="card-info-title">{parse(t("Card3.Title"))}</h3>
                <span className="card-info-description">
                  {parse(t("Card3.Description"))}
                </span>
                <div className="card-info-button-holder">
                  <Link to="/requestExtracurricularActivity">
                    <button className="btn btn-danger">
                      {t("Card3.Button")}
                    </button>
                  </Link>
                </div>
                <div className="card-info-list">
                  {parse(t("Card3.Features"))}
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="cta-section text-center">
        <div className="container">
          <h2 className="h2 cta-title">{t("Footer1")}</h2>
          <div className="cta-button-holder">
            <a
              href="https://go.docusign.com/sandbox/productshot?elq=16799"
              target="_blank"
              rel="noopener noreferrer"
            >
              <button className="btn btn-danger">{t("SandBoxButton")}</button>
            </a>
            <a
              href="https://developers.docusign.com/"
              target="_blank"
              rel="noopener noreferrer"
            >
              <button className="btn btn-secondary">
                {t("LearnMoreButton")}
              </button>
            </a>
          </div>
          <div className="cta-description">{parse(t("Footer2"))}</div>
        </div>
      </section>
    </>
  );
};
